package grab;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.ClassLoader;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;

import au.com.bytecode.opencsv.CSVReader;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.S3Object;

public class ClientApp {
	private String access_key;
	private String secret_key;
	private String bucket_name;
	private String bucket_path;
	private String region;
	
	public ClientApp() throws Exception{
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
		bucket_name = doc.getElementsByTagName("bucket-name").item(0).getTextContent();
		bucket_path	= doc.getElementsByTagName("bucket-path").item(0).getTextContent();
		region	 	= doc.getElementsByTagName("region").item(0).getTextContent();
	}
	
	public AmazonS3 authenticate() {
		AmazonS3 s3_client 	= null;
		try {
			BasicAWSCredentials cred = new BasicAWSCredentials(access_key, secret_key);		
			s3_client = AmazonS3ClientBuilder.standard()
							.withCredentials(new AWSStaticCredentialsProvider(cred))
							.withRegion(region)
							.build();
			
		}catch(AmazonServiceException ase_ex) {
			ase_ex.printStackTrace();
		}
		catch(AmazonClientException ace_ex) {
			ace_ex.printStackTrace();
		}
		return s3_client;
	}
	
	public String getBucketName() {
		return bucket_name;
	}
	
	public String getBucketPath() {
		return bucket_path;
	}
	
	public static void main(String[] args) throws Exception {
        String [] nextLine;

		ClientApp client 	= new ClientApp();
		AmazonS3 s3_client 	= client.authenticate();
		
		S3Object s3_obj 	= s3_client.getObject(client.getBucketName(), client.getBucketPath());
		InputStream in_strm = s3_obj.getObjectContent();
        InputStreamReader in_strm_rdr = new InputStreamReader(in_strm);
        CSVReader csv 		= new CSVReader(in_strm_rdr, ',');
        
        FileStreamMediator fs = new FileStreamMediator(csv.readNext());
        csv.readNext(); // Discard empty row
        
        while ((nextLine = csv.readNext()) != null) {
        	fs.sendPayload(nextLine);
         }
        
        csv.close();
        s3_obj.close();
	}
}
