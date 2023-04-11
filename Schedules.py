from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase import db
from datetime import datetime

app = FastAPI()

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