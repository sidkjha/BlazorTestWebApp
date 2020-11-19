import enum
from PythonFlaskAPIForBlazorCln import db

class Gen(enum.Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

class Employee(db.Model):
    EmployeeId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(120), nullable=False, unique=True)
    LastName = db.Column(db.String(120), nullable=False, unique=True)
    Email = db.Column(db.String(250), nullable=False, unique=True)
    Gender = db.Column(db.Enum(Gen), nullable=False)
    DepartmentId = db.Column(db.Integer, db.ForeignKey('department.DepartmentId'),nullable=False)
    Department = db.relationship('Department',backref=db.backref('posts', lazy=True))
    DateOfBirth = db.Column(db.DateTime, nullable=False)
    PhotoPath = db.Column(db.String(250))

    def __repr__(self):
        return '<Employee %r>' % self.FirstName

    def to_dict(self):
        data = {
            'EmployeeId': self.EmployeeId,
            'FirstName': self.FirstName,
            'LastName':  self.LastName,
            'Email': self.Email,
            'Gender': self.Gender,
            'Department': Department.DepartmentName,
            'DateOfBirth': self.DateOfBirth,
            'PhotoPath': self.PhotoPath
            }
        return data

class Department(db.Model):
    DepartmentId = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return '<Department %r>' % self.DepartmentName

    def to_dict(self):
        data = {
            'DepartmentId': self.DepartmentId,
            'DepartmentName': self.DepartmentName            
            }
        return data