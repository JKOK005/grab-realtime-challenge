package grab;

import java.nio.ByteBuffer;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.TimeZone;

import org.json.JSONObject;

import com.amazonaws.services.kinesis.AmazonKinesis;
import com.amazonaws.services.kinesis.model.PutRecordRequest;

import interfaces.PayloadInterface;

public class DemandStreamGenerator implements PayloadInterface{
	private String[] required_cols 	= {"tpep_pickup_datetime", "PULocationID"};

	private JSONObject frameJsonData(String[] data) {
		JSONObject json = new JSONObject();
		json.put("timestamp", getTime("GMT+08:00")); 		
		json.put("locationId", data[1]); 				// Refractor: Hardcoding of data location
		return json;
	}
	
	private String getTime(String time_zone) {
		SimpleDateFormat date_format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		date_format.setTimeZone(TimeZone.getTimeZone(time_zone));
		return date_format.format(new Date());
	}
	
	@Override
	public String[] getRequiredCols() {
		return required_cols;
	}

	@Override
	public JSONObject frameJson(String[] headers, String[] data) {
		JSONObject final_json = new JSONObject();
		final_json.put("data", frameJsonData(data));
		return final_json;
	}

	@Override
	public void sendStream(ArrayList<String> payload) {
		try {
			AmazonKinesis kinesis_client = new KinesisClient().authenticate();
			JSONObject json = frameJson(required_cols, payload.toArray(new String[payload.size()]));
			
			// Send the json payload to Kinesis stream
			byte[] payload_byte = json.toString().getBytes("utf-8");
			PutRecordRequest putRecord = new PutRecordRequest();
			putRecord.setStreamName("grab-supply-stream");
			putRecord.setPartitionKey("demand");
			putRecord.setData(ByteBuffer.wrap(payload_byte));
			kinesis_client.putRecord(putRecord);
		}catch(Exception ex) {
			ex.printStackTrace();
		}
	}	
}
