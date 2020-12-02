## Creating a test client Web Application based on ASP.NET Core 3.1 Blazor Server which calls Restful Python Flask API and deploying in AWS ec2 instance using Jenkins as continuous delivery tool

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
Now, to insert sample data, go inside git repo and open Python terminal and type the following:
###### from BlazorTestWebApp.PythonFlaskAPIForBlazorCln.PythonFlaskAPIForBlazorCln import db
###### from BlazorTestWebApp.PythonFlaskAPIForBlazorCln.PythonFlaskAPIForBlazorCln.models import Department, Employee, Gen
###### from datetime import datetime
###### dp1 = Department(DepartmentName='DEPT1')
###### db.session.add(dp1)
###### dp2 = Department(DepartmentName='DEPT2')
###### db.session.add(dp2)
###### dp3 = Department(DepartmentName='DEPT3')
###### db.session.add(dp3)
###### dp4 = Department(DepartmentName='DEPT4')
###### db.session.add(dp4)
###### dp5 = Department(DepartmentName='DEPT5')
###### db.session.add(dp5)
###### db.session.commit()
###### emp1 = Employee(FirstName='Srijib', LastName='Bhattacharyya', Email='srijibb@xmail.com', Gender=Gen.Male, DepartmentId=1, DateOfBirth=datetime.strptime('08/07/81 09:08:23', '%d/%m/%y %H:%M:%S'), PhotoPath='images/srijib.jpg')
###### db.session.add(emp1)
###### emp2 = Employee(FirstName='John', LastName='Lenon', Email='johnl@jmail.com', Gender=Gen.Male, DepartmentId=2, DateOfBirth=datetime.strptime('13/11/82 19:08:21', '%d/%m/%y %H:%M:%S'), PhotoPath='images/john.png')
###### db.session.add(emp2)
###### emp3 = Employee(FirstName='Mary', LastName='Love', Email='maryl@xmail.com', Gender=Gen.Female, DepartmentId=1, DateOfBirth=datetime.strptime('15/10/90 20:07:33', '%d/%m/%y %H:%M:%S'), PhotoPath='images/mary.png')
###### db.session.add(emp3)
###### emp4 = Employee(FirstName='Sara', LastName='Gery', Email='saragl@xmail.com', Gender=Gen.Female, DepartmentId=1, DateOfBirth=datetime.strptime('08/02/80 20:07:33', '%d/%m/%y %H:%M:%S'), PhotoPath='images/sara.png')
###### db.session.add(emp4)
###### emp5 = Employee(FirstName='Sam', LastName='Bogo', Email='samb@cmail.com', Gender=Gen.Male, DepartmentId=4, DateOfBirth=datetime.strptime('23/12/87 22:07:55', '%d/%m/%y %H:%M:%S'), PhotoPath='images/sam.jpg')
###### db.session.add(emp5)
###### db.session.commit()

---------------------------------------------------------------------------------------
Now, to run the flask server app (temporarily), type the following in **shell** terminal:
###### export FLASK_APP=BlazorTestWebApp/PythonFlaskAPIForBlazorCln/runserver.py
###### flask run --port=5555

Then check the endpoints by browsing in
1. http://localhost:5555/api/employees (also can view the deployed one in aws ec2 instance by clicking: http://ec2-18-223-187-60.us-east-2.compute.amazonaws.com/api/employees) --> **few of the fields are not showing due to some difficulty**
2. http://localhost:5555/api/departments (also can view the deployed one in aws ec2 instance by clicking: http://ec2-18-223-187-60.us-east-2.compute.amazonaws.com/api/departments)

After this you can run the Blazor Server project from VS. Enjoy ! :)

### stay tuned for updates
