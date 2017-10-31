package grab;

import java.nio.ByteBuffer;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;
import java.util.Random;

import org.json.JSONObject;

import com.amazonaws.services.kinesis.AmazonKinesis;
import com.amazonaws.services.kinesis.model.PutRecordRequest;

public class SupplyApp {	
	private String getTime(String time_zone) {
		SimpleDateFormat date_format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		date_format.setTimeZone(TimeZone.getTimeZone(time_zone));
		return date_format.format(new Date());
	}
	
	private JSONObject frameJson(int taxiId, int locationId) {
		JSONObject final_json = new JSONObject();
		JSONObject body = new JSONObject();
		body.put("taxiid", taxiId);
		body.put("locationid", locationId);
		body.put("timestamp", getTime("GMT+08:00"));
		final_json.put("data", body);
		return final_json;
	}
	
	private void sendPayload(JSONObject payload) {
		System.out.println("Sending to supply stream");
		try {
			AmazonKinesis kinesis_client = new KinesisClient().authenticate();
			
			// Send the json payload to Kinesis stream
			byte[] payload_byte = payload.toString().getBytes("utf-8");
			PutRecordRequest putRecord = new PutRecordRequest();
			putRecord.setStreamName("grab-supply-stream");
			putRecord.setPartitionKey("supply");
			putRecord.setData(ByteBuffer.wrap(payload_byte));
			kinesis_client.putRecord(putRecord);
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		System.out.println(payload.toString());
		System.out.println("Successfully sent to stream");
	}
	
	private int getTaxiCount(int avg, int std_dev) {
		Random random 	= new Random();
		int count 		= (int) Math.round(random.nextGaussian()*std_dev + avg);
		return Math.max(5, count);
	}
	
	public static void main(String[] args) throws Exception {
		SupplyApp supply 	= new SupplyApp();
		int sleepTime 		= 5000;
		int cycleDelay 		= 10*60*1000;
		
		while(true) {
			int count 			= supply.getTaxiCount(25, 5);
			int locationId 		= 237;
			int taxiId 			= 1;
			
			while(taxiId*sleepTime < cycleDelay) {
				JSONObject payload 	= supply.frameJson(taxiId % count, locationId);
				supply.sendPayload(payload);
				taxiId++;
				Thread.sleep(sleepTime);
			}
		}
	}
}
