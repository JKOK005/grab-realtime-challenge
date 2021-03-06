package grab;

import java.util.ArrayList;
import java.util.Arrays;

import interfaces.PayloadInterface;

public class FileStreamMediator {
	private String[] headers;
	private PayloadInterface[] payloads_container = {new DemandStreamGenerator(), 
													 new TrafficLogStreamGenerator()};
	private DelayAgent payload_releaser = new DelayAgent();
	
	private int getHeaderLocation(String[] headers, String columnName) {
	   return Arrays.asList(headers).indexOf(columnName);
	}
 
	public void sendPayload(String[] str) {
		String pick_up_time 	= str[getHeaderLocation(headers, "tpep_pickup_datetime")];
		payload_releaser.delayReleaseUntilTime(pick_up_time);
	
		for(PayloadInterface payload : payloads_container) {
			String[] required_cols 	= payload.getRequiredCols();
			
			ArrayList<String> required_data = new ArrayList<String>();  
			for(String each_header : required_cols) {
				String tmp 			= str[getHeaderLocation(headers, each_header)];
				required_data.add(tmp);
			}	
			payload.sendStream(required_data);
		}
	}
	
	public FileStreamMediator(String[] str) {
		headers = str;
	}	
}
