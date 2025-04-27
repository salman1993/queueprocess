from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .db import engine
from .models import Base
from .queue import RedisQueue
from .store import PostgresItemStore
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()

queue = RedisQueue()
store = PostgresItemStore()

Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    name: str

@app.post("/items/")
def create_item(item: ItemCreate):
    item_obj = store.create_item(name=item.name)
    logger.info(f"Item created with id={item_obj.id}, status={item_obj.status}")

    # Enqueue job
    job_data = {"item_id": item_obj.id}
    queue.enqueue(job_data)
    logger.info(f"Enqueued job for item {item_obj.id}")

    return {"id": item_obj.id, "status": item_obj.status}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    logger.info(f"Getting item {item_id}")
    item_obj = store.get_item(item_id)
    if not item_obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": item_obj.id,
        "name": item_obj.name,
        "status": item_obj.status,
        "result": item_obj.result,
    }
