from utils.dal import Dal
from models.product_model import ProductModel as M
from sqlalchemy import text
from fastapi import HTTPException, status
from typing import cast
import math

class ProductService:

    def __init__(self) -> None:
        self.session = Dal.create_session()

    # def get_all_products(self):
    #     products = self.session.query(M).all()
    #     return products

    # def get_one_product(self, id: int):
    #     product = self.session.query(M).get(id)
    #     if not product:
    #         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Product {id} not found")
    #     return product

    # def get_out_of_stock(self):
    #     products = self.session.query(M).filter(M.stock == 0).all()
    #     return products

    # def get_products_by_range(self, min: float, max: float):
    #     if min > max :
    #         raise HTTPException(status_code=422, detail=f"Min must be bigger then max, fix the params in this section:?min={min}&max={max}")
    #     products = self.session.query(M).filter(M.price >= min, M.price <= max).all()
    #     return products

    def get_cheapest(self, limit: int):
        if limit < 1:
            raise HTTPException(status_code= status.HTTP_422_UNPROCESSABLE_CONTENT, detail= "The minimum limit is 1")
        products = self.session.query(M).order_by(M.price).limit(limit).all()
        return products

    def get_low_stock(self, threshhold: int):
        products = self.session.query(M).filter(M.stock <= threshhold, M.stock > 0).all()
        return products

    def get_page(self, page: int, size: int):

        offset = (page-1)*size
        total_count = self.session.query(M).count()
        items = self.session.query(M).offset(offset).limit(size).all()
        total_pages = math.ceil(total_count/size)

        return { "items": items , "total_items": total_count, "current_page": page, "total_pages": total_pages }

    


    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()