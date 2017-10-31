## Web Viewer 

### Description
Web viewer for visualization of realtime data and batch data query. We can query batch data for demand/supply and traffic log distribution. We can also
perform direct API queries to Weather Underground historical databases via the url: http://api.wunderground.com/api/"access_token"/history_20171024/q/ny/upper_east_side.json 

Be sure to obtain your access token by signing up for a pricing plan at Weather Underground's website. This token is used for API queries. Depending on your pricing plan,
the number of queries will be limited based on total monthly queries and queries per min. 

Communication with the RDS database is done through IAM instance user & password authentication. Be sure to store those variables as well as RDS host, port and database name in your
OS environment. 

Communication between frontend client and backend server is done through JSON Http protocols. As such, any frontend client which knows the suitable routes can request data from the 
backend, provided that it has the appropriate CSRF token. 

### Dependencies
Backend stack:
* Python Django 
* Boto library 
* Request library 

Frontend stack:
* HTML + CSS + JQuery 

### Execution
At the root folder, run the command
```python

python manage.py runserver

```

If you have not sync your webapp with RDS, run 
```python

python manage.py makemigrations
python manage.py migrate

```

