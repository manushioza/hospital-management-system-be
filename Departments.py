from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase import db

app = FastAPI()

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