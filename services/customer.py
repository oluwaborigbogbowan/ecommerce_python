from fastapi import HTTPException
from schema.customer import customers,CustomerCreate


class CustomerService:

    @staticmethod
    def validate_username(payload: CustomerCreate):
        username = payload.username
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail='customer already exists')
        return payload
    

customer_service = CustomerService()