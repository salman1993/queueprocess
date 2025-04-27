from sqlalchemy.orm import Session
from .models import Item
from .db import SessionLocal

class ItemStore:
    def create_item(self, name: str) -> Item:
        raise NotImplementedError

    def get_item(self, item_id: int) -> Item | None:
        raise NotImplementedError

    def update_item_status_and_result(self, item_id: int, status: str, result: str | None) -> None:
        raise NotImplementedError


class PostgresItemStore(ItemStore):
    def __init__(self):
        self.Session = SessionLocal

    def create_item(self, name: str) -> Item:
        db: Session = self.Session()
        item = Item(name=name, status="queued")
        db.add(item)
        db.commit()
        db.refresh(item)
        db.close()
        return item

    def get_item(self, item_id: int) -> Item | None:
        db: Session = self.Session()
        item = db.query(Item).filter(Item.id == item_id).first()
        db.close()
        return item

    def update_item_status_and_result(self, item_id: int, status: str, result: str | None) -> None:
        db: Session = self.Session()
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            item.status = status
            item.result = result
            db.commit()
        db.close()
