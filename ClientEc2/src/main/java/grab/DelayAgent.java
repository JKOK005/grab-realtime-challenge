package grab;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DelayAgent {
	private Date last_date; 
	
	public DelayAgent() {
		last_date 	= null;
	}
	
	public Date getLastDate() {
		return last_date;
	}
	
	public void setLastDate(Date new_date) {
		last_date 	= new_date;
	}
	
	public void delayReleaseUntilTime(String new_time) {
		SimpleDateFormat format_in = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		try {
			delayReleaseUntilTime(format_in.parse(new_time));
		}
		catch(Exception ex) {
			ex.printStackTrace();
		}
	}
	
	public void delayReleaseUntilTime(Date new_time) {
		long diff = 0;
		
		if(last_date != null) {
			diff 	= new_time.getTime() - last_date.getTime();
			// Pause thread execution here
		}
		last_date 	= new_time;
		try {
			Thread.sleep(diff);
		}catch(Exception ex) {
			System.out.println(ex);
		}
	}
}
