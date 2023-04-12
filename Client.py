import requests
import json

base_url = "http://127.0.0.1:8000"

def get_doctors():
    response = requests.get(f"{base_url}/doctors")
    if response.status_code == 200:
        doctors = response.json()
        print(json.dumps(doctors, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_doctor(doctor_id):
    response = requests.get(f"{base_url}/doctors/{doctor_id}")
    if response.status_code == 200:
        doctor = response.json()
        print(json.dumps(doctor, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_doctor(first_name, last_name, email, age, pager_number, department_id):
    payload = {
        "d_first_name": first_name,
        "d_last_name": last_name,
        "d_email": email,
        "d_age": age,
        "d_pager_number": pager_number,
        "d_department_id": department_id
    }
    response = requests.post(f"{base_url}/doctors", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def update_doctor(doctor_id, first_name, last_name, email, age, pager_number, department_id):
    payload = {
        "d_first_name": first_name,
        "d_last_name": last_name,
        "d_email": email,
        "d_age": age,
        "d_pager_number": pager_number,
        "d_department_id": department_id
    }
    response = requests.put(f"{base_url}/doctors/{doctor_id}", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def delete_doctor(doctor_id):
    response = requests.delete(f"{base_url}/doctors/{doctor_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_rooms():
    response = requests.get(f"{base_url}/rooms")
    if response.status_code == 200:
        rooms = response.json()
        print(json.dumps(rooms, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_room(room_id):
    response = requests.get(f"{base_url}/rooms/{room_id}")
    if response.status_code == 200:
        room = response.json()
        print(json.dumps(room, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_room(room_number, room_type):
    payload = {
        "r_num": room_number,
        "r_type": room_type,
    }
    response = requests.post(f"{base_url}/rooms", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def update_room(room_id, room_number, room_type, room_availability):
    payload = {
        "r_availability": room_availability
    }
    response = requests.put(f"{base_url}/rooms/{room_id}", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def delete_room(room_id):
    response = requests.delete(f"{base_url}/rooms/{room_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")


def get_patients():
    response = requests.get(f"{base_url}/patients")
    if response.status_code == 200:
        patients = response.json()
        print(json.dumps(patients, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_patient(patient_id):
    response = requests.get(f"{base_url}/patients/{patient_id}")
    if response.status_code == 200:
        patient = response.json()
        print(json.dumps(patient, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_patient(first_name, last_name, email, age, phone_number,emergency_contact_name,emergency_contact_phone_number, emergency_contact_relationship, department_id):
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email":email,
        "phone_number":phone_number,
        "emergency_contact_name":emergency_contact_name,
        "emergency_contact_phone_number":emergency_contact_phone_number,
        "emergency_contact_relationship":emergency_contact_relationship,
        "department":department_id
    }
    response = requests.post(f"{base_url}/patients", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def update_patient(first_name, last_name, email, age, phone_number,emergency_contact_name,emergency_contact_phone_number, emergency_contact_relationship,  department_id):
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email":email,
        "phone_number":phone_number,
        "emergency_contact_name":emergency_contact_name,
        "emergency_contact_phone_number":emergency_contact_phone_number,
        "emergency_contact_relationship":emergency_contact_relationship,
        "department":department_id
    }
    response = requests.put(f"{base_url}/patients/{doctor_id}", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def delete_patient(patient_id):
    response = requests.delete(f"{base_url}/patients/{patient_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_departments():
    response = requests.get(f"{base_url}/departments")
    if response.status_code == 200:
        departments = response.json()
        print(json.dumps(departments, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_department(department_id):
    response = requests.get(f"{base_url}/departments/{department_id}")
    if response.status_code == 200:
        department = response.json()
        print(json.dumps(department, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_department(department_name):
    payload = {
        "department_name": department_name
    }
    response = requests.post(f"{base_url}/departments", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def update_department(department_id, department_name):
    payload = {
        "department_name": department_name,
        "department_id": department_id
    }
    response = requests.put(f"{base_url}/departments/{department_id}", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def delete_department(department_id):
    response = requests.delete(f"{base_url}/departments/{department_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")


def get_schedules():
    response = requests.get(f"{base_url}/schedules")
    if response.status_code == 200:
        schedules = response.json()
        print(json.dumps(schedules, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_schedule(event_id):
    response = requests.get(f"{base_url}/schedules/{event_id}")
    if response.status_code == 200:
        schedule = response.json()
        print(json.dumps(schedule, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_schedule(department_id, room_id,patient_id, doctor_id, start_date, end_date):
    payload = {
        "department_id": department_id,
        "room_id": room_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "start_date": start_date, 
        "end_date": end_date
    }
    response = requests.post(f"{base_url}/schedules", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def update_schedule(event_id,department_id, room_id,patient_id, doctor_id, start_date, end_date):
    payload = {
        "event_id": event_id,
        "department_id": department_id,
        "room_id": room_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "start_date": start_date, 
        "end_date": end_date
    }
    response = requests.put(f"{base_url}/schedules/{event_id}", params=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

def delete_schedule(event_id):
    response = requests.delete(f"{base_url}/schedules/{event_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")


while True:
    print("Choose a management option:")
    print("1: Doctor")
    print("2: Room")
    print("3: Patient")
    print("4: Department")
    print("5: Schedule")
    print("6: Exit")
    
    choiceManagement = input("Enter the number corresponding to your choice: ")

    if choiceManagement == "1":
        print("\nOptions:")
        print("1: Get all doctors")
        print("2: Get a specific doctor")
        print("3: Create a new doctor")
        print("4: Update a doctor")
        print("5: Delete a doctor")
        print("6: Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            get_doctors()
        elif choice == "2":
            doctor_id = input("Enter the doctor ID: ")
            get_doctor(doctor_id)
        elif choice == "3":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            email = input("Enter the email: ")
            age = int(input("Enter the age: "))
            pager_number = int(input("Enter the pager number: "))
            department_id = input("Enter the department ID: ")
            create_doctor(first_name, last_name, email, age, pager_number, department_id)
        elif choice == "4":
            doctor_id = input("Enter the doctor ID: ")
            first_name = input("Enter the new first name (-1 to keep the same): ")
            last_name = input("Enter the new last name (-1 to keep the same): ")
            email = input("Enter the new email (-1 to keep the same): ")
            age = int(input("Enter the new age (-1 to keep the same): "))
            pager_number = int(input("Enter the new pager number (-1 to keep the same): "))
            department_id = input("Enter the new department ID (-1 to keep the same): ")
            update_doctor(doctor_id, first_name, last_name, email, age, pager_number, department_id)
        elif choice == "5":
            doctor_id = input("Enter the doctor ID: ")
            delete_doctor(doctor_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    elif choiceManagement == "2":
        print("\nRoom Management Menu:")
        print("1. Get all rooms")
        print("2. Get room details")
        print("3. Create a new room")
        print("4. Update a room")
        print("5. Delete a room")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_rooms()
        elif choice == "2":
            room_id = input("Enter the room ID: ")
            get_room(room_id)
        elif choice == "3":
            room_number = int(input("Enter the room number: "))
            room_type = input("Enter the room type: ")
            create_room(room_number, room_type)
        elif choice == "4":
            room_id = input("Enter the room ID: ")
            room_number = int(input("Enter the new room number: "))
            room_type = input("Enter the new room type: ")
            room_availability = input("Enter the new room availability (True/False): ")
            room_availability = True if room_availability.lower() == "true" else False
            update_room(room_id, room_number, room_type, room_availability)
        elif choice == "5":
            room_id = input("Enter the room ID: ")
            delete_room(room_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    elif choiceManagement == "3":
        print("\nOptions:")
        print("1: Get all Patients")
        print("2: Get a specific Patient")
        print("3: Create a new Patient")
        print("4: Update a Patient")
        print("5: Delete a Patient")
        print("6: Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            get_patients()
        elif choice == "2":
            patient_id = input("Enter the Patients ID: ")
            get_patient(patient_id)
        elif choice == "3":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            email = input("Enter the email: ")
            age = int(input("Enter the age: "))
            phone_number = int(input("Enter the pager number: "))
            emergency_contact_name = input("Enter the emergency contact name: ")
            emergency_contact_phone_number = int(input("Enter the emergency contact phone number: "))
            emergency_contact_relationship = input("Enter the emergency contact relationship: ")
            department_id = input("Enter the department ID: ")
            create_patient(first_name, last_name, email, age, phone_number,emergency_contact_name,emergency_contact_phone_number, emergency_contact_relationship,  department_id)
        elif choice == "4":
            patient_id = input("Enter patient id: ")
            first_name = input("Enter the first name (-1 to keep the same): ")
            last_name = input("Enter the last name (-1 to keep the same): ")
            email = input("Enter the email (-1 to keep the same): ")
            age = int(input("Enter the age (-1 to keep the same): "))
            phone_number = int(input("Enter the pager number (-1 to keep the same): "))
            emergency_contact_name = input("Enter the emergency contact name (-1 to keep the same): ")
            emergency_contact_phone_number = int(input("Enter the emergency contact phone number (-1 to keep the same): "))
            emergency_contact_relationship = input("Enter the emergency contact relationship (-1 to keep the same): ")
            department_id = input("Enter the department ID (-1 to keep the same): ")
            update_patient(patient_id, first_name, last_name, email, age, phone_number,emergency_contact_name,emergency_contact_phone_number, emergency_contact_relationship,  department_id)
        elif choice == "5":
            patient_id = input("Enter the patient ID: ")
            delete_patient(patient_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    elif choiceManagement == "4":
        print("\nOptions:")
        print("1: Get all departments")
        print("2: Get a specific department")
        print("3: Create a new department")
        print("4: Update a department")
        print("5: Delete a department")
        print("6: Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            get_departments()
        elif choice == "2":
            department_id = input("Enter the Department ID: ")
            get_department(department_id)
        elif choice == "3":
            department_name = input("Enter the department name: ")
            create_department(department_name)
        elif choice == "4":
            department_id = input("Enter the Department ID: ")
            department_name = input("Enter the department name: ")
            update_department(department_id, department_name)
        elif choice == "5":
            department_id = input("Enter the Department ID: ")
            delete_department(department_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    elif choiceManagement == "5":
        print("\nOptions:")
        print("1: Get all Schedules")
        print("2: Get a specific Schedule")
        print("3: Create a new Schedule")
        print("4: Update a Schedule")
        print("5: Delete a Schedule")
        print("6: Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            get_schedules()
        elif choice == "2":
            event_id = input("Enter the Schedule ID: ")
            get_schedule(event_id)
        elif choice == "3":
            department_id = input("Enter the Department ID: ")
            room_id = input("Enter the Room ID: ")
            patient_id = input("Enter the Patient ID: ")
            doctor_id = input("Enter the Doctor ID: ")
            start_date = input("Enter the Start Date(format: dd/mm/yyyy): ")
            end_date = input("Enter the End Date(format: dd/mm/yyyy): ")
            create_schedule(department_id, room_id,patient_id, doctor_id, start_date, end_date)
        elif choice == "4":
            event_id = input("Enter patient id: ")
            department_id = input("Enter the Department ID: ")
            room_id = input("Enter the Room ID: ")
            patient_id = input("Enter the Patient ID: ")
            doctor_id = input("Enter the Doctor ID: ")
            start_date = input("Enter the Start Date(format: dd/mm/yyyy): ")
            end_date = input("Enter the End Date(format: dd/mm/yyyy): ")
            update_schedule(event_id,department_id, room_id,patient_id, doctor_id, start_date, end_date)
        elif choice == "5":
            event_id = input("Enter the schedule ID: ")
            delete_schedule(event_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")            

    elif choiceManagement == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
    
