package interfaces;

import java.util.ArrayList;
import org.json.JSONObject;

public interface PayloadInterface {
	public String[] getRequiredCols();
	public void sendStream(ArrayList<String> payload);
	public JSONObject frameJson(String[] headers, String[] data);
}
