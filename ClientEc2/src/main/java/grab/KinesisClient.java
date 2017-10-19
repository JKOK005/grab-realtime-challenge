package grab;

import java.io.InputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;

import com.amazonaws.services.kinesis.AmazonKinesisClient;

public class KinesisClient {
	private AmazonKinesisClient kinesis;
	private static String access_key;
	private static String secret_key;
	
	public KinesisClient() throws Exception{
		Document doc;
		
		try {
			InputStream config_xml = ClassLoader.getSystemResourceAsStream("config.xml");
			
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory
	                .newInstance();
	        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();    
	        doc = dBuilder.parse(config_xml);    
		}catch(Exception ex) {
			ex.printStackTrace();
			throw new Exception();
		}
		access_key 	= doc.getElementsByTagName("access-key").item(0).getTextContent();
		secret_key 	= doc.getElementsByTagName("secret-key").item(0).getTextContent();
	}
	
	public void authenticate() {
		
	}
}
