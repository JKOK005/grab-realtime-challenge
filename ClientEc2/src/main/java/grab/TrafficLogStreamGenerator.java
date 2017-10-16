package grab;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.TimeZone;

import org.json.JSONObject;

import interfaces.PayloadInterface;

public class TrafficLogStreamGenerator implements PayloadInterface{
	private String[] required_cols 	= {"tpep_pickup_datetime", "tpep_dropoff_datetime", "PULocationID", 
										"trip_distance"};
	
	private JSONObject frameJsonData(String[] data) {
		JSONObject json 	= new JSONObject();
		long travel_time 	= getTravelTime(data[0], data[1]);
		json.put("travelTime", travel_time);
		json.put("timestamp", getTime("GMT+08:00"));
		json.put("locationId", data[2]);
		json.put("distance", data[3]);
		return json;
	}
	
	private long getTravelTime(String start, String end) {
		SimpleDateFormat format_in = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		long diff = 0;
		try {
			Date d_start 	= format_in.parse(start);
			Date d_end 		= format_in.parse(end);
			diff 			= d_end.getTime() - d_start.getTime();
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		return diff / 1000;		// Returns seconds
	}
	
	private String getTime(String time_zone) {		
		SimpleDateFormat format_out = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		format_out.setTimeZone(TimeZone.getTimeZone(time_zone));
		return format_out.format(new Date());
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
		JSONObject json = frameJson(required_cols, payload.toArray(new String[payload.size()]));
		// Send the json payload to Kinesis stream
		System.out.println(json.toString());
	}
}
