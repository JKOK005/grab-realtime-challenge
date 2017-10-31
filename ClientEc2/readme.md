## Demand & Traffic logs simulator

### Description
Used to generate demand and traffic logs data from a .csv file in S3 storage to AWS Kinesis demand and traffic logs stream. The original data is
taken from NYC Taxi & Limousine Commission taxi data, for Yellow taxis in the month of June, 2017. 

We assume a demand count is generated when the user makes a booking request. As such, each pick up time field denotes a user demand at a given location ID. 
We will send a payload in the format to the demand stream for AWS Kinesis: 
```
data = {
	“timestamp” 	: Current date time in UTC
	“locationId” 	: Location as specified by the row
	}
```

At the same time, we can generate a traffic log stream payload of the format:
```
data = {
	“timestamp” 	: Time stamp after addition of trip time to start time (in DD payload)
	“locationId” 	: Location as specified by the row
	“distance” 		: Distance as specified by the row
	“travelTime” 	: Travel duration calculated by DropoffTime - PickupTime (In seconds)
}
```

A **delay** is placed before each payload is sent for a given location ID. We first sort the entries for a location ID in ascending timestamp. To simulate
realtime data, each dispatch of payload is delayed by a duration between the ith and i+1th entry. 

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

