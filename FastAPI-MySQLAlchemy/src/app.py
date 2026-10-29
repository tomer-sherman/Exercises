from fastapi import FastAPI
from uvicorn import run
from controller.product_controller import router as product_router
from middleware.error_middleware import register_exeption_handler

server = FastAPI()

server.include_router(product_router)

register_exeption_handler(server)

if __name__ == "__main__":
    run("app:server", port=4000, reload= True)



