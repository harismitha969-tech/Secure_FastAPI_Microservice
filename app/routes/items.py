
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item, User
from app.schemas import ItemCreate, ItemResponse
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


# CREATE ITEM
@router.post("/", response_model=ItemResponse,
             status_code=status.HTTP_201_CREATED)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_item = Item(
        title=item_data.title,
        description=item_data.description,
        owner_id=current_user.id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


# READ ALL ITEMS
@router.get("/", response_model=list[ItemResponse])
def get_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Item).filter(
        Item.owner_id == current_user.id
    ).all()


# READ SINGLE ITEM
@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    item = db.query(Item).filter(
        Item.id == item_id,
        Item.owner_id == current_user.id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# UPDATE ITEM
@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item_data: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    item = db.query(Item).filter(
        Item.id == item_id,
        Item.owner_id == current_user.id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    item.title = item_data.title
    item.description = item_data.description

    db.commit()
    db.refresh(item)

    return item


# DELETE ITEM
@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    item = db.query(Item).filter(
        Item.id == item_id,
        Item.owner_id == current_user.id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    db.delete(item)
    db.commit()

    return {"message": "Item deleted successfully"}
