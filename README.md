## Creating a test client Web Application based on ASP.NET Core 3.1 Blazor Server which calls Restful Python Flask API

Before executing BlazorServer project, make sure to run the flask server i.e Restful Python Flask API
To do so, go inside git repo and open Python terminal and type the following (one-time):
###### from BlazorTestWebApp.PythonFlaskAPIForBlazorCln.PythonFlaskAPIForBlazorCln import db
###### db.create_all()
This creates the schemas written in models.py as per database configured stated in settings.ini

---------------------------------------------------------------------------------------
Now, to run the flask server app (temporarily), type the following in shell terminal:
###### export FLASK_APP=BlazorTestWebApp/PythonFlaskAPIForBlazorCln/runserver.py
###### flask run --port=5555

Then check the endpoints by browsing in
1. http://localhost:5555/api/employees
2. http://localhost:5555/api/departments

After this you can run the Blazor Server project from VS. Enjoy ! :)

### stay tuned for updates
