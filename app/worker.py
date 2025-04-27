from .queue import RedisQueue
from .store import PostgresItemStore
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)

queue = RedisQueue()
store = PostgresItemStore()

logger.info("Worker started, listening to queue...")

while True:
    job_data = queue.dequeue()
    # Simulate a lag in processing
    time.sleep(3)
    if job_data:
        item_id = job_data["item_id"]
        
        logger.info(f"Processing item {item_id}")

        item = store.get_item(item_id)
        if item:
            store.update_item_status_and_result(item_id, status="processing", result=None)

            # Simulate work
            time.sleep(5)

            # Done processing
            store.update_item_status_and_result(item_id, status="done", result=f"Processed {item.name}")
            logger.info(f"Item {item_id} processed")
    else:
        time.sleep(1)  # No jobs, sleep a bit
