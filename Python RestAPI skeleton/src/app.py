from fastapi import FastAPI
from uvicorn import run
from controller.product_controller import router as product_router
from middleware.error_middleware import register_exeption_handler

server = FastAPI()

server.include_router(product_router)

register_exeption_handler(server)

if __name__ == "__main__":
    run("app:server", port=4000, reload= True)


# Setup:
# enviorment setup 
# py -m venv env 
# srouce env/scripts/activate
# pip install -r requirements.txt

# Make sure the env is setup:
# With the proper connection string, for me change in the end the DB name

# Create a db sql query inside the Database file then when you finish building and you seeded the data properly then, export and make sure the seeded data is inside the database folder

# Runing:
#py src/app.py 


