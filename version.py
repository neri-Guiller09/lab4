from fastapi import FastAPI, APIRouter, HTTPException, Header, Depends
from typing import Optional
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Validate if the API_KEY is set in the .env file
if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set in the .env file.")

# Task Databases for Versioning
apiv1_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

apiv2_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# Helper Function to Get Task
def find_task(task_db, task_id: int):
    return next((task for task in task_db if task["task_id"] == task_id), None)

# Helper Function for API Key Validation
def validate_api_key(x_api_key: str = Header(None)):
    if not x_api_key or x_api_key != neripogi:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid or missing API key.")
    return True

# Task Model for Pydantic Validation
class Task(BaseModel):
    task_title: str
    task_desc: Optional[str] = ""
    is_finished: bool = False

# Version 1 Router
apiv1_router = APIRouter()

@apiv1_router.get("/task/{task_id}")
def get_task_apiv1(task_id: int, x_api_key: str = Depends(validate_api_key)):
    task = find_task(apiv1_db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    return {"task": task}

@apiv1_router.post("/task")
def create_task_apiv1(task: Task, x_api_key: str = Depends(validate_api_key)):
    task_id = len(apiv1_db) + 1
    new_task = task.dict()
    new_task["task_id"] = task_id
    apiv1_db.append(new_task)
    return {"message": "Task successfully created.", "task": new_task}

@apiv1_router.patch("/task/{task_id}")
def update_task_apiv1(task_id: int, task: Task, x_api_key: str = Depends(validate_api_key)):
    task_db_entry = find_task(apiv1_db, task_id)
    if not task_db_entry:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    task_db_entry.update(task.dict())
    return {"message": "Task successfully updated.", "task": task_db_entry}

@apiv1_router.delete("/task/{task_id}")
def delete_task_apiv1(task_id: int, x_api_key: str = Depends(validate_api_key)):
    task = find_task(apiv1_db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    apiv1_db.remove(task)
    return {"message": "Task successfully deleted."}

# Version 2 Router
apiv2_router = APIRouter()

@apiv2_router.get("/task/{task_id}", dependencies=[Depends(validate_api_key)])
def get_task_apiv2(task_id: int):
    task = find_task(apiv2_db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    return {"task": task}, 200  # OK

@apiv2_router.post("/task", dependencies=[Depends(validate_api_key)], status_code=201)
def create_task_apiv2(task: Task):
    task_id = len(apiv2_db) + 1
    new_task = task.dict()
    new_task["task_id"] = task_id
    apiv2_db.append(new_task)
    return {"message": "Task successfully created.", "task": new_task}

@apiv2_router.patch("/task/{task_id}", dependencies=[Depends(validate_api_key)])
def update_task_apiv2(task_id: int, task: Task):
    task_db_entry = find_task(apiv2_db, task_id)
    if not task_db_entry:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

    # Update only provided fields
    updated_fields = task.dict(exclude_unset=True)
    task_db_entry.update(updated_fields)
    
    return {"message": "Task successfully updated."}, 204  # No Content with message



@apiv2_router.delete("/task/{task_id}", dependencies=[Depends(validate_api_key)], status_code=200)
def delete_task_apiv2(task_id: int):
    task = find_task(apiv2_db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
    
    apiv2_db.remove(task)
    return {"message": "Task successfully deleted."}  # You can include a message here



# Main Application
app = FastAPI()
app.include_router(apiv1_router, prefix="/apiv1", tags=["API Version 1"])
app.include_router(apiv2_router, prefix="/apiv2", tags=["API Version 2"])
