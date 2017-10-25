var randomScalingFactor = function(){ return Math.round(Math.random()*1000)};
	
var demandAndSupplyData = {
	labels : [],
	datasets : [
		{
			label: "Demand",
			fillColor : "rgba(225,48,164,0.2)",
			strokeColor : "rgba(225,0,0,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(220,220,220,1)",
			data : []
		},
		{
			label: "Supply",
			fillColor : "rgba(48, 164, 255, 0.2)",
			strokeColor : "rgba(48, 164, 255, 1)",
			pointColor : "rgba(48, 164, 255, 1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(48, 164, 255, 1)",
			data : []
		}
	]

}
	
var trafficData = {
	labels : [],
	datasets : [
		{
			label: "Supply",
			fillColor : "rgba(48, 164, 255, 0.2)",
			strokeColor : "rgba(48, 164, 255, 1)",
			pointColor : "rgba(48, 164, 255, 1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(48, 164, 255, 1)",
			data : []
		},
	]

}

var weatherData = {
	labels : [],
	datasets : [
		{
			label: "windspeed",
			fillColor : "rgba(225, 48, 164, 0.2)",
			strokeColor : "rgba(225, 0, 0, 1)",
			pointColor : "rgba(220, 220, 220, 1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(220, 220, 220, 1)",
			data : []
		},
		{
			label: "temp",
			fillColor : "rgba(48, 164, 255, 0.2)",
			strokeColor : "rgba(48, 164, 255, 1)",
			pointColor : "rgba(48, 164, 255, 1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(48, 164, 255, 1)",
			data : []
		},
		{
			label: "humidity",
			fillColor : "rgba(48, 225, 164, 0.2)",
			strokeColor : "rgba(48, 225, 164, 1)",
			pointColor : "rgba(48, 225, 164, 1)",
			pointStrokeColor : "#fff",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(100, 100, 100, 1)",
			data : []
		},
	]

}