from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase import db

app = FastAPI()

class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    pager_number: int
    department_id: str

@app.get('/doctors')
async def get_doctors():
    doctors_db = {}
    doctors_ref = db.collection(u'doctor')
    docs = doctors_ref.stream()
    for doc in docs:
        doctors_db[doc.id] = doc.to_dict()
    return doctors_db

@app.get('/doctors/{doctor_id}')
async def get_doctor(doctor_id: str):
    doctor = {}
    doctor_ref = db.collection(u'doctor').document(doctor_id)
    doctor_doc = doctor_ref.get()
    if doctor_doc.exists:
        doctor = doctor_doc.to_dict()  
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.post('/doctors')
async def create_doctor(d_first_name:str, d_last_name:str, d_email:str, d_age:int, d_pager_number:int, d_department_id:str):
    new_doctor = {
        u'doctor_id': 0,
        u'first_name': d_first_name,
        u'last_name': d_last_name,
        u'email': d_email,
        u'age': d_age,
        u'pager_number': d_pager_number,
        u'department_id': d_department_id
    }

    doctor_ref = db.collection(u'doctor').document()
    new_doctor['doctor_id'] = doctor_ref.id
    doctor_ref.set(new_doctor)

    return {'message': 'Doctor created.'}

@app.put('/doctors/{doctor_id}')
async def update_doctor(doctor_id: str, d_first_name:str, d_last_name:str, d_email:str, d_age:int, d_pager_number:int, d_department_id:str):
    doctor_ref = db.collection(u'doctor').document(doctor_id)
    doctor_doc = doctor_ref.get()
    if doctor_doc.exists:
        if(d_first_name != "-1"):
            doctor_ref.update({
            u'first_name': d_first_name})
        if(d_last_name != "-1"):
            doctor_ref.update({
            u'last_name': d_last_name})
        if(d_email != "-1"):
            doctor_ref.update({
            u'email': d_email})
        if(d_age != -1):
            doctor_ref.update({
            u'age': d_age})
        if(d_pager_number != -1):
            doctor_ref.update({
            u'pager_number': d_pager_number})
        if(d_department_id != "-1"):
            doctor_ref.update({
            u'department_id': d_department_id})
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {'message': 'Doctor Updated.'}

@app.delete('/doctors/{doctor_id}')
async def delete_doctor(doctor_id: str):
    doctor_ref = db.collection(u'doctor').document(doctor_id)
    doctor_doc = doctor_ref.get()
    if doctor_doc.exists:
        doctor_ref.delete()
    else:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {'message': 'Doctor Deleted.'}