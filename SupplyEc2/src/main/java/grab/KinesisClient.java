package grab;

import java.io.InputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;

import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.kinesis.AmazonKinesis;
import com.amazonaws.services.kinesis.AmazonKinesisClientBuilder;
import com.amazonaws.internal.StaticCredentialsProvider;

@SuppressWarnings("deprecation")
public class KinesisClient {
	private AmazonKinesis kinesis;
	private String access_key;
	private String secret_key;
	private String region;
	
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
		region	 	= doc.getElementsByTagName("region").item(0).getTextContent();
	}
	
	@SuppressWarnings("deprecation")
	public AmazonKinesis authenticate() {
		BasicAWSCredentials cred = new BasicAWSCredentials(access_key, secret_key);	
		AmazonKinesisClientBuilder clientBuilder = AmazonKinesisClientBuilder.standard();
		clientBuilder.setRegion(region);
		clientBuilder.setCredentials(new StaticCredentialsProvider(cred));
		kinesis 	= clientBuilder.build();
		return kinesis;
	}
}
