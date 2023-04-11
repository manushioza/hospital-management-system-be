from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase import db

app = FastAPI()

class Room(BaseModel):
    room_id: int
    room_type: str
    room_number: int
    room_availability: bool


@app.get('/rooms')
async def get_rooms():
    rooms_db = {}
    rooms_ref = db.collection(u'rooms')
    docs = rooms_ref.stream()
    for doc in docs:
        rooms_db[doc.id] = doc.to_dict()
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
