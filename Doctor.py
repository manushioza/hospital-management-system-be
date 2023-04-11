from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    pager_number: int
    department: str


doctors_db = [
    Doctor(id=1, first_name='John', last_name='Doe', age=35, email='johndoe@example.com', pager_number=12345, department='Cardiology'),
    Doctor(id=2, first_name='Jane', last_name='Smith', age=45, email='janesmith@example.com', pager_number=67890, department='Neurology'),
]


@app.get('/doctors')
async def get_doctors():
    return doctors_db

@app.get('/doctors/{doctor_id}')
async def get_doctor(doctor_id: int):
    for doctor in doctors_db:
        if doctor.id == doctor_id:
            return doctor
    return {'message': 'Doctor not found.'}

@app.post('/doctors')
async def create_doctor(doctor: Doctor):
    doctors_db.append(doctor)
    return {'message': 'Doctor created.'}

@app.put('/doctors/{doctor_id}')
async def update_doctor(doctor_id: int, doctor: Doctor):
    for i, d in enumerate(doctors_db):
        if d.id == doctor_id:
            doctors_db[i] = doctor
            return {'message': 'Doctor updated.'}
    return {'message': 'Doctor not found.'}

@app.delete('/doctors/{doctor_id}')
async def delete_doctor(doctor_id: int):
    for i, doctor in enumerate(doctors_db):
        if doctor.id == doctor_id:
            doctors_db.pop(i)
            return {'message': 'Doctor deleted.'}
    return {'message': 'Doctor not found.'}