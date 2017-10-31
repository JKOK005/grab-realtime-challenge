## Supply simulator

### Description
Used to generate taxi data to the Supply stream of Kinesis. We assume a taxi reports its location via Geopoint coordinates every 5 sec. Each taxi will be given a unique ID.

We will send a payload in the format: 
```
data = {
	“timestamp” 	: date time stamp
	“taxiId” 		: unique taxi id for different vehicle
	“locationId” 	: Geopoint coordinates in [long, lat]
}

```

### Kinesis streams
Our architecture uses 3 Kinesis streams
* Demand stream 
* Traffic log stream
* Supply stream 

Each stream can be scaled up / down based on the shards allocated. This allows the system to handle varying amount of incoming traffic data. 

### Dependencies
* Eclipse IDE + AWS toolkit support
* Java 

### Deployment
First, generate the executable JAR file by compiling the code

Thereafter, deploy the JAR on your Ec2 instance. 
* Run SCP to transfer the JAR file into the Ec2 instance [ref](https://stackoverflow.com/questions/11388014/using-scp-to-copy-a-file-to-amazon-ec2-instance)
* SSH into the Ec2 instance via a an access-key.pem file
* Execute the file using
``` java
java -jar runnable.jar
```

