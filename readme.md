## Grab real time price surge and traffice density calculator

### Description
This repository contains the scripts needed to simulate a real time scenario for a given Geohash lvl 6. The Geohash choosen is in the Upper East Coast, Manhattan, New York city
and has a plot diameter of 600m x 1200m. In this geohash, we will need to simulate demand and supply of taxis at any given point of the day. We will also need to evaluate
traffic densities by factoring in information such as time and distance of travel. Finally, we will need to query for weather data to see how demand is affected by certain 
conditions of the weather. 

### Dataset
We will use the following datasets:
* [NYC Taxi and Limousine Commission](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) 	- Yellow taxi data for the the month of June, 2017
* [Weather Underground API](https://www.wunderground.com/history/airport/KJFK/2014/1/2/DailyHistory.html?MR=1) - Historical weather data API 

### Architecture
Our approach uses mainly AWS services to simulate, stream and process data into databases. We will be using the following AWS services:
* S3 storage 				- Used to store .csv scripts for generating customer demand
* Kinesis streaming 		- Used to queue incoming data 
* Ec2 instances (3 total)	- Amazon Linux environments used to perpetually generate to and consume from kinesis pipeline
* PostgreSQL RDS 			- SQL database to store processed results after consuming from the stream
* Elasticsearch 			- NoSQL database used for mapping Geopoint coordinates ([long, lat]) to nearest Geohash location ID

In addition, we will have a front end client App and backend server developed using Django

A high level overview of the architecture is given below:
![Architecture](/pics/Architecture.png)

### Services
This repository contains several services listed below
* ClientEc2 		- Spins a client node on an Ec2 instance to generate demand data to the Kinesis demand & Traffic log stream
* SupplyEc2 		- Spins a supply node on an Ec2 instance to generate taxi supply to the Kinesis supply stream
* StreamConsumer 	- Spins nodes on Ec2 instances to consume from all Kinesis streams and stores data into PostgreSQL tables
* ClientAppViewer 	- Frontend and backend services for querying database and displaying data (realtime and batch)