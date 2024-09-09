from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_object_or_404(object_id: int, db: Session, data_table, text: str = "Object not found"):
    object = db.query(data_table).filter(data_table.id == object_id).first()
    if not object:
        raise HTTPException(status_code=404, detail=text)
    return object