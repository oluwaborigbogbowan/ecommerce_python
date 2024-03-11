from typing import Union
from pydantic import BaseModel
from schema.customer import Customer
from enum import Enum

from schema.product import Product

class OrderStatus(Enum):
    completed = 'Completed'
    pending = 'Pending'

class Order(BaseModel):
    id: int
    customer_id: Union[int, Customer]
    items: list[int | Product]
    status: str = OrderStatus.pending.value

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

orders = [
    Order(id=1, customer_id=1, items=[1, 2])
]