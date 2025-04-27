import httpx
import time

BASE_URL = "http://localhost:8000"

# 1. Create an item (enqueue it)
print("Creating item...")
response = httpx.post(f"{BASE_URL}/items/", json={"name": "Test Item"})
item = response.json()
item_id = item["id"]

print(f"Item created with id={item_id}, initial status={item['status']}")

# 2. Poll the item status until it's done
while True:
    time.sleep(1)
    status_response = httpx.get(f"{BASE_URL}/items/{item_id}")
    status_data = status_response.json()

    print(f"Polled status: {status_data['status']}")

    if status_data["status"] == "done":
        print(f"Result: {status_data['result']}")
        break
