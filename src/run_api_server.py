from _path import *
import uvicorn
import logging
from api_server.service.api_server import app


logging.basicConfig(level=logging.DEBUG)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="5000")
