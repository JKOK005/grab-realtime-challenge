from elasticsearch import Elasticsearch


if __name__ == "__main__":
	es 		= Elasticsearch(["https://search-grab-geohash-6utb45rgz2b7527orod34kgwby.us-east-1.es.amazonaws.com"])

	mappings = {
				"mappings" 	: {
					"geohash": {
			        	"properties": {
				        	"name"  : {
			        			"type" : "string",
			        		},
		                    "location": {
		                        "type": "geo_point",
	    	            	},
		                },
					},
				}
	        }
			    
			
	es.indices.create(index='geodata', body=mappings, ignore=400)
	es_entries 	= {}
	es_entries	= { 'name' 		: "Chipotle Mexican Grill",
					'location'	: {
							"lat" 	: 40.00,
							"lon" 	: -74.12,
						},
					}

	es.index(index="geodata", doc_type="geohash", id=1 , body=es_entries)

	es_entries	= { 'name' 		: "Wendys",
					'location'	: {
							"lat" 	: 20.00,
							"lon" 	: -24.12,
						},
					}

	es.index(index="geodata", doc_type="geohash", id=2 , body=es_entries)

	# query = {                             
 #    ...:   "query": {
 #    ...:     "bool": {
 #    ...:       "filter": {
 #    ...:         "geo_distance": {
 #    ...:           "distance": "10000km", 
 #    ...:           "location": [-24.13,20.00],
 #    ...:         }
 #    ...:       }
 #    ...:     } 
 #    ...:  }
 #    ...: }
 	# es.search(index="geodata", body=query)

	import IPython
	IPython.embed()

