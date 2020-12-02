## Creating a test client Web Application based on ASP.NET Core 3.1 Blazor Server which calls Restful Python Flask API

WIP: Dockerfile has been created which is used build images and run the container in docker host - an AWS ec2 linux instance. Nginx will configured to make it accessible over internet.

Pre-requisites: Type the following in shell terminal (assuming Python3.7 and pip i.e. package manager is pre-installed in the system)-
###### pip install -r BlazorTestWebApp/PythonFlaskAPIForBlazorCln/requirement.txt
This downloads and install the python dependencies to execute the python scripts below. (must have admin privileges and internet connection)

---------------------------------------------------------------------------------------
Before executing BlazorServer project, make sure to run the flask server i.e Restful Python Flask API
To do so, go inside git repo and open Python terminal and type the following (one-time):
###### from BlazorTestWebApp.PythonFlaskAPIForBlazorCln.PythonFlaskAPIForBlazorCln import db
###### db.create_all()
This creates the schemas written in models.py as per database configured stated in settings.ini

---------------------------------------------------------------------------------------
Now, to run the flask server app (temporarily), type the following in **shell** terminal:
###### export FLASK_APP=BlazorTestWebApp/PythonFlaskAPIForBlazorCln/runserver.py
###### flask run --port=5555

Then check the endpoints by browsing in
1. http://localhost:5555/api/employees (also can view the deployed one in aws ec2 instance by clicking: http://ec2-18-189-27-121.us-east-2.compute.amazonaws.com/api/employees) --> **few of the fields are not showing due to some difficulty**
2. http://localhost:5555/api/departments (also can view the deployed one in aws ec2 instance by clicking: http://ec2-18-189-27-121.us-east-2.compute.amazonaws.com/api/departments)

After this you can run the Blazor Server project from VS. Enjoy ! :)

### stay tuned for updates
