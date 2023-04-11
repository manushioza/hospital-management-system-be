from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Room(BaseModel):
    id: int
    type: str
    number: int
    quarantine: bool

rooms_db = [
    Room(id=1, type='Patient', number=101, quarantine=False),
    Room(id=2, type='ER', number=102, quarantine=True),
    Room(id=3, type='Operating', number=201, quarantine=False),
    Room(id=4, type='Procedure', number=202, quarantine=False),
]

@app.get('/rooms')
async def get_rooms():
    return rooms_db

@app.get('/rooms/{room_id}')
async def get_room(room_id: int):
    for room in rooms_db:
        if room.id == room_id:
            return room
    return {'message': 'Room not found.'}

@app.post('/rooms')
async def create_room(room: Room):
    rooms_db.append(room)
    return {'message': 'Room created.'}

@app.put('/rooms/{room_id}')
async def update_room(room_id: int, room: Room):
    for i, r in enumerate(rooms_db):
        if r.id == room_id:
            rooms_db[i] = room
            return {'message': 'Room updated.'}
    return {'message': 'Room not found.'}

@app.delete('/rooms/{room_id}')
async def delete_room(room_id: int):
    for i, room in enumerate(rooms_db):
        if room.id == room_id:
            rooms_db.pop(i)
            return {'message': 'Room deleted.'}
    return {'message': 'Room not found.'}