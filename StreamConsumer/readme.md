## Kinesis stream consumer + RDS storeage

### Description
This repository contains SurgePrice and Traffic logs stream consumers. We will spin 2 instances of Ec2 that perpetually process the streams at **10 min** intervals. 
The data gathered will be processed and thereafter stored into tables in the RDS. 

The nodes that we will set up are: 
* SurgePriceNode.py - Consumes Demand and Supply stream in realtime. Aggregates all counts obtained and stores them in the database.
* TrafficLogNode.py - Consumes Traffic log stream in realtime. Calculates average speed for a location and stores the data in the database.

Be sure to include your AWS Access, Secret key and Region to access your Kinesis stream. This information can be added to your KinesisClient.py file
or in a separate config file in XML forat. You will have to configure the path to that config file. 

### Dependencies
Python 
* boto3
* psycopg2
* xmltodict	

### Deployment
Deploy the file to your Ec2 instance

* Run SCP to transfer the file into the Ec2 instance [ref](https://stackoverflow.com/questions/11388014/using-scp-to-copy-a-file-to-amazon-ec2-instance)
* SSH into the Ec2 instance via a an access-key.pem file
* Execute the relevant node using
``` python
python SurgePriceNode.py 

```

or

``` python
python TrafficLogNode.py 

```


