from fastapi import FastAPI , Request, HTTPException, status
from fastapi.responses import JSONResponse

def register_exeption_handler(server: FastAPI):

    @server.exception_handler(HTTPException)
    def http_handler(request: Request, err: HTTPException):
        print("Error: " + str(err))
        return JSONResponse(status_code= err.status_code, content= {"message": err.detail})

    @server.exception_handler(Exception)
    def unhandled_exeption_handler(request: Request, err: Exception):
        print("Error: " + str(err))
        return JSONResponse(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, content= {"message": str(err)})