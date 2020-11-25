"""
Routes and views for the flask application.
"""

from flask import *
from PythonFlaskAPIForBlazorCln import app, db
from PythonFlaskAPIForBlazorCln.models import *

employee = Blueprint('employee', __name__)
department = Blueprint('department', __name__)

colsemp = ['EmployeeId', 'FirstName', 'LastName', 'Email', 'PhotoPath']
colsdept = ['DepartmentId', 'DepartmentName']

@employee.route('/api/employees', methods=['GET', 'POST'])
def employees():
    try:
        if request.method == 'GET':
            data = Employee.query.all()
            result = [{col: getattr(d, col) for col in colsemp} for d in data]
            return jsonify(result)
        elif request.method == 'POST':
            fname = request.json['FirstName']
            lname = request.json['LastName']
            emailid = request.json['Email']
            existing_employee = Employee.query.filter(Employee.FirstName == fname).filter(Employee.LastName == lname).filter(Employee.Email == emailid).one_or_none()
            if existing_employee is None:
                emp = Employee(fname, lname, emailid, request.json['Gender'], request.json['DepartmentId'], request.json['DateOfBirth'], request.json['PhotoPath'])
                db.session.add(emp)
                db.session.commit()
                return {"message": f"Employee {fname} {lname} successfully inserted."}
            else:
                return {"message": f"Employee {fname} {lname} already exists."}
    except Exception as e:
        return e

@employee.route('/api/employees/<int:emp_id>', methods=['GET', 'PUT', 'DELETE'])
def employee_by_id(emp_id):
	try:
		print(emp_id)
		data_by_id = Employee.query.filter_by(Employee.EmployeeId == emp_id).first()
		if data_by_id is None:
				return 'Incorrect ID'
		else:
			if request.method == 'GET':
				result = [{col: getattr(d, col) for col in colsemp} for d in data_by_id]
				return jsonify(result)
			elif request.method == 'PUT':
				data_by_id.FirstName = request.json['FirstName']
				data_by_id.LastName = request.json['LastName']
				data_by_id.Email = request.json['Email']
				data_by_id.PhotoPath = request.json['PhotoPath']
				db.session.add(data_by_id)
				db.session.commit()
				return {"message": f"Employee {data_by_id.FirstName} successfully updated."}
			elif request.method == 'DELETE':
				db.session.delete(data_by_id)
				db.session.commit()
				return {"message": f"Employee {data_by_id.FirstName} successfully deleted."}
	except Exception as e:
		return e

@department.route('/api/departments', methods=['GET', 'POST'])
def departments():
    try:
        if request.method == "GET":
            data = Department.query.all()
            result = [{col: getattr(d, col) for col in colsdept} for d in data]
            return jsonify(result)
        elif request.method == "POST":
            deptname = request.json['DepartmentName']
            existing_department = Department.query.filter(Department.DepartmentName == deptname).one_or_none()
            if existing_department is None:
                dept = Department(deptname)
                db.session.add(dept)
                db.session.commit()
                return {"message": f"Department {deptname} successfully inserted."}
            else:
                return {"message": f"Department {deptname} already exists."}
    except Exception as e:
        return e

@department.route('/api/departments/<int:dept_id>', methods=['GET', 'PUT', 'DELETE'])
def department_by_id(dept_id):
	try:		
		data_by_id = Department.query.filter_by(Department.DepartmentId == dept_id).first()
		if data_by_id is None:
				return 'Incorrect ID'
		else:
			if request.method == 'GET':
				result = [{col: getattr(d, col) for col in colsdept} for d in data_by_id]
				return jsonify(result)
			elif request.method == 'PUT':
				data_by_id.DepartmentName = request.json['DepartmentName']	
				db.session.add(data_by_id)
				db.session.commit()
				return {"message": f"Department {data_by_id.DepartmentName} successfully updated."}
			elif request.method == 'DELETE':
				db.session.delete(data_by_id)
				db.session.commit()
				return {"message": f"Department {data_by_id.DepartmentName} successfully deleted."}
	except Exception as e:
		return e

@employee.route("/hello")
def hello():
     return 'Hello Srijib, Welcome to AWS!'
