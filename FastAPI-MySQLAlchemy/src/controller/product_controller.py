from fastapi import APIRouter
from service.product_service import ProductService

router = APIRouter()

# @router.get("/api/products")
# def get_all_products():
#     with ProductService() as service:
#         products = service.get_all_products()
#         return products

# @router.get("/api/products/out-of-stock")
# def get_out_of_stock():
#     with ProductService() as service:
#         products = service.get_out_of_stock()
#         return products

# @router.get("/api/products/{id}")
# def get_one_product(id: int):
#     with ProductService() as service:
#         product = service.get_one_product(id)
#         return product

# @router.get("/api/products-by-range")
# def get_products_by_price_range(min: float, max: float):
#     with ProductService() as service:
#         products = service.get_products_by_range(min, max)
#         return products
    
@router.get("/api/cheapest-products")
def get_cheapest(limit: int):
    with ProductService() as service:
        products = service.get_cheapest(limit)
        return products

@router.get("/api/low-stock-products/{threshhold}")
def get_low_stock(threshhold: int):
    with ProductService() as service:
        products = service.get_low_stock(threshhold)
        return products

@router.get("/api/get-page/{page}/{size}")
def get_pag(page: int, size: int):
    with ProductService() as service:
        pagdata = service.get_page(page, size)
        return pagdata

