
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item, User
from app.schemas import ItemCreate, ItemResponse
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


# 1. CREATE ITEM
@router.post("/", response_model=ItemResponse)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_item = Item(
        title=item.title,
        description=item.description,
        owner_id=current_user.id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


# 2. READ ALL USER ITEMS
@router.get("/", response_model=list[ItemResponse])
def get_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Item).filter(
        Item.owner_id == current_user.id
    ).all()


# 3. READ SINGLE ITEM
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


# 4. UPDATE ITEM
@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    updated_item: ItemCreate,
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

    item.title = updated_item.title
    item.description = updated_item.description

    db.commit()
    db.refresh(item)

    return item


# 5. DELETE ITEM
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

    return {
        "message": "Item deleted successfully"
    }
