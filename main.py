from fastapi import FastAPI
from agents import CustomerAgent, ProductAgent
from recommender import recommend_products
from database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/view/{user_id}/{product_id}")
def view_product(user_id: int, product_id: int):
    agent = CustomerAgent(user_id)
    agent.view_product(product_id)
    return {"message": f"User {user_id} viewed product {product_id}"}

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    product_ids = recommend_products(user_id)
    products = [ProductAgent(pid).get_details() for pid in product_ids]
    return {"recommendations": products}
