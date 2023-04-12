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

class Schedule(BaseModel):
    event_id: int
    department_id: str
    room_id: str
    patient_id: str
    doctor_id: str
    start_date: str
    end_date: int


@app.get('/schedules')
async def get_schedules():
    schedules_db = {}
    schedules_ref = db.collection(u'schedule')
    docs = schedules_ref.stream()
    for doc in docs:
        schedules_db[doc.id] = doc.to_dict()
    return schedules_db


@app.get('/schedules/{event_id}')
async def get_schedule(event_id: str):
    schedule = {}
    schedule_ref = db.collection(u'schedule').document(event_id)
    schedule_doc = schedule_ref.get()
    if schedule_doc.exists:
        schedule = schedule_doc.to_dict()  
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule

from datetime import datetime

@app.post('/schedules')
async def create_schedule(department_id:str, room_id:str,patient_id:str, doctor_id:str, start_date:str, end_date:str):
    
    # Check if doctor, patient, or room is already booked
    schedules = db.collection(u'schedule').where(u'start_date', u'<=', end_date).where(u'start_date', u'>=', start_date).stream()

    for schedule in schedules:
        schedule_data = schedule.to_dict()
        if schedule_data['doctor_id'] == doctor_id:
            return {'message': 'Doctor already booked during this time.'}
        elif schedule_data['patient_id'] == patient_id:
            return {'message': 'Patient already booked during this time.'}
        elif schedule_data['room_id'] == room_id:
            return {'message': 'Room already booked during this time.'}
    
    # Create new schedule
    new_schedule = {
        u'event_id': 0,
        u'department_id': department_id,
        u'room_id': room_id,
        u'patient_id': patient_id,
        u'doctor_id': doctor_id,
        u'start_date': start_date,
        u'end_date': end_date,
    }
    
    schedule_ref = db.collection(u'schedule').document()
    new_schedule['event_id'] = schedule_ref.id
    schedule_ref.set(new_schedule)

    return {'message': 'Schedule created.'}




@app.put('/schedules/{event_id}')
async def update_schedule(event_id: str,department_id:str = None, room_id:str = None,patient_id:str = None, doctor_id:str = None, start_date:str = None, end_date:str = None):
    
    schedule_ref = db.collection(u'schedule').document(event_id)
    schedule_doc = schedule_ref.get()

    if start_date is None:
            start_date = schedule_doc.get('start_date')
    if end_date is None:
            end_date = schedule_doc.get('end_date')        
            # Check if doctor, patient, or room is already booked
    schedules = db.collection(u'schedule').where(u'start_date', u'<=', end_date).where(u'start_date', u'>=', start_date).stream()

    for schedule in schedules:
        schedule_data = schedule.to_dict()
        if schedule_data['doctor_id'] == doctor_id:
            return {'message': 'Doctor already booked during this time.'}
        elif schedule_data['patient_id'] == patient_id:
            return {'message': 'Patient already booked during this time.'}
        elif schedule_data['room_id'] == room_id:
            return {'message': 'Room already booked during this time.'}
        
    if schedule_doc.exists:
        if department_id is not None:
            schedule_ref.update({u'department_id': department_id})
        if room_id is not None:
            schedule_ref.update({u'room_id': room_id})
        if patient_id is not None:
            schedule_ref.update({u'patient_id': patient_id})
        if doctor_id is not None:
            schedule_ref.update({u'doctor_id': doctor_id})
        if start_date is not None:
            schedule_ref.update({u'start_date': start_date})
        if end_date is not None:
            schedule_ref.update({u'end_date': end_date})                                
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {'message': 'Schedule Updated.'}


@app.delete('/schedules/{event_id}')
async def delete_schedule(event_id: str):
    schedule_ref = db.collection(u'schedule').document(event_id)
    schedule_doc = schedule_ref.get()
    if schedule_doc.exists:
        schedule_ref.delete()
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {'message': 'Schedule Deleted.'}

class Department(BaseModel):
    department_id: int
    department_name: str


@app.get('/departments')
async def get_department():
    departments_db = {}
    departments_ref = db.collection(u'departments')
    docs = departments_ref.stream()
    for doc in docs:
        departments_db[doc.id] = doc.to_dict()
    return departments_db


@app.get('/departments/{department_id}')
async def get_department(department_id: str):
    department = {}
    department_ref = db.collection(u'departments').document(department_id)
    department_doc = department_ref.get()
    if department_doc.exists:
        department = department_doc.to_dict()  
    else:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@app.post('/departments')
async def create_department(department_name:str):
    new_department = {
        u'department_id': 0,
        u'department_name': department_name,
    }

    department_ref = db.collection(u'departments').document()
    new_department['department_id'] = department_ref.id
    department_ref.set(new_department)

    return {'message': 'Department created.'}


@app.put('/departments/{department_id}')
async def update_department(department_id: str, department_name: str):
    department_ref = db.collection(u'departments').document(department_id)
    department_doc = department_ref.get()
    if department_doc.exists:
        department_ref.update({ u'department_name': department_name})
    else:
        raise HTTPException(status_code=404, detail="Department not found")
    return {'message': 'Department Updated.'}


@app.delete('/departments/{department_id}')
async def delete_department(department_id: str):
    department_ref = db.collection(u'departments').document(department_id)
    department_doc = department_ref.get()
    if department_doc.exists:
        department_ref.delete()
    else:
        raise HTTPException(status_code=404, detail="Department not found")
    return {'message': 'Department Deleted.'}

class Patient(BaseModel):
    patient_id:str
    first_name:str
    last_name:str
    age:int
    email:str
    phone_number:int
    emergency_contact_name:str
    emergency_contact_phone_number:int
    emergency_contact_relationship:str
    department:str



@app.get('/patients')
async def get_patients():
    patient_db = {}
    patient_ref = db.collection(u'patients')
    docs = patient_ref.stream()
    for doc in docs:
        patient_db[doc.id] = doc.to_dict()
    return patient_db


@app.get('/patients/{patient_id}')
async def get_patient(patient_id: str):
    patient = {}
    patient_ref = db.collection(u'patients').document(patient_id)
    patient_doc = patient_ref.get()
    if patient_doc.exists:
        patient = patient_doc.to_dict()  
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post('/patients')
async def create_patient(f_n:str, l_n:str, a:int, e:str, p_n:int, e_c_n:str, e_c_p_n:int, e_c_r:str, d:str):
    new_patient = {
        u'patient_id': 0,
        u'first_name': f_n,
        u'last_name':l_n,
        u'age': a,
        u'email':e,
        u'phone_number': p_n,
        u'emergency_contact_name': e_c_n,
        u'emergency_contact_phone_number': e_c_p_n,
        u'emergency_contact_rlationship':e_c_r,
        u'department':d
    }

    patient_ref = db.collection(u'patients').document()
    new_patient['patient_id'] = patient_ref.id
    patient_ref.set(new_patient)
    return {'message': 'Patient created.'}


@app.put('/patients/{patient_id}')
async def update_patient(patient_id:str, f_n:str, l_n:str, a:int, e:str, p_n:int, e_c_n:str, e_c_p_n:int, e_c_r:str, d:str):
    patient_ref = db.collection(u'patients').document(patient_id)
    patient_doc = patient_ref.get()
    if patient_doc.exists:
        if(f_n != "-1"):
            patient_ref.update({
            u'first_name': f_n})
        if(l_n != "-1"):
            patient_ref.update({
            u'last_name': l_n})
        if(e != "-1"):
            patient_ref.update({
            u'email': e})
        if(a != -1):
            patient_ref.update({
            u'age': a})
        if(p_n != -1):
            patient_ref.update({
            u'phone_number': p_n})
        if(e_c_n != "-1"):
            patient_ref.update({
            u'emergency_contact_name': e_c_n})
        if(e_c_p_n != -1):
            patient_ref.update({
            u'emergency_contact_phone_number': e_c_p_n})
        if(e_c_r != "-1"):
            patient_ref.update({
            u'emergency_contact_rlationship': e_c_r})
        if(d != "-1"):
            patient_ref.update({
            u'department_id': d})
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {'message': 'Patient Updated.'}


@app.delete('/patients/{patient_id}')
async def delete_room(patient_id: str):
    patient_ref = db.collection(u'patients').document(patient_id)
    patient_doc = patient_ref.get()
    if patient_doc.exists:
        patient_ref.delete()
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {'message': 'Patient Deleted.'}

class Room(BaseModel):
    room_id: int
    room_type: str
    room_number: int
    room_availability: bool


@app.get('/rooms')
async def get_rooms():
    rooms_db = {}
    rooms_ref = db.collection(u'rooms')
    rooms = rooms_ref.stream()
    for room in rooms:
        rooms_db[room.id] = room.to_dict()
    return rooms_db


@app.get('/rooms/{room_id}')
async def get_room(room_id: str):
    room = {}
    room_ref = db.collection(u'rooms').document(room_id)
    room_doc = room_ref.get()
    if room_doc.exists:
        room = room_doc.to_dict()  
    else:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.post('/rooms')
async def create_room(r_num:int, r_type:str):
    new_room = {
        u'room_id': 0,
        u'room_type': r_type,
        u'room_number': r_num,
        u'room_availability': True
    }

    room_ref = db.collection(u'rooms').document()
    new_room['room_id'] = room_ref.id
    room_ref.set(new_room)

    return {'message': 'Room created.'}


@app.put('/rooms/{room_id}')
async def update_room(room_id: str, r_num:int, r_type: str, r_availability:bool):
    room_ref = db.collection(u'rooms').document(room_id)
    room_doc = room_ref.get()
    if room_doc.exists:
        room_ref.update({ u'room_type': r_type,
                u'room_number': r_num,
                u'room_availability': r_availability})
    else:
        raise HTTPException(status_code=404, detail="Room not found")
    return {'message': 'Room Updated.'}


@app.delete('/rooms/{room_id}')
async def delete_room(room_id: str):
    room_ref = db.collection(u'rooms').document(room_id)
    room_doc = room_ref.get()
    if room_doc.exists:
        room_ref.delete()
    else:
        raise HTTPException(status_code=404, detail="Room not found")
    return {'message': 'Room Deleted.'}
