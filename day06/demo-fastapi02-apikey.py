from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader, APIKey
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum


app = FastAPI()

# Define the Gender Enum
class Gender(str, Enum):
    male = "male"
    female = "female"
 

# Define the Role class
class Role(BaseModel):
    role_name: str

# Define the Employee class
class Employee(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

# Sample data storage
employees: List[Employee] = []

# Sample Employees
employees.append(Employee(first_name="Vineeth", last_name="Kumar", gender=Gender.male, roles=[Role(role_name="Developer")]))
employees.append(Employee(first_name="Kamala", last_name="Harris", gender=Gender.female, roles=[Role(role_name="Manager")]))
employees.append(Employee(first_name="Charles", last_name="Kobe", gender=Gender.male, roles=[Role(role_name="Designer")]))

# API Key Security
"""Replace this key with values from DB for each user maintain separate keys"""

API_KEY = "dell1234" 
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)


def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key or credentials")

# CRUD operations

# Create Employee
@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee, api_key: APIKey = Depends(get_api_key)):
    employees.append(employee)
    return employee

# Read all Employees
@app.get("/employees", response_model=List[Employee])
def read_employees(api_key: APIKey = Depends(get_api_key)):
    return employees

# Read Employee by ID
@app.get("/employees/{employee_id}", response_model=Employee)
def read_employee(employee_id: UUID, api_key: APIKey = Depends(get_api_key)):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Update Employee
@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: UUID, updated_employee: Employee, api_key: APIKey = Depends(get_api_key)):
    for i, emp in enumerate(employees):
        if emp.id == employee_id:
            employees[i] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete Employee
@app.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee(employee_id: UUID, api_key: APIKey = Depends(get_api_key)):
    for i, emp in enumerate(employees):
        if emp.id == employee_id:
            return employees.pop(i)
    raise HTTPException(status_code=404, detail="Employee not found")

# To run the app: `python -m uvicorn demo-fastapi02-apikey:app --reload` otherwise use 'fastapi dev demo-fastapi02-apikey.py'
