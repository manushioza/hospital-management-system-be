from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase import db

app = FastAPI()

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
async def get_patient():
    patient_db = {}
    patient_ref = db.collection(u'patients')
    docs = patient_ref.stream()
    for doc in docs:
        patient_db[doc.id] = doc.to_dict()
    return patient_db


@app.get('/patients/{patient_id}')
async def get_room(patient_id: str):
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
