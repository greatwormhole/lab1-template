import os
from uvicorn import Config

server_settings = Config(
    app='app:app',
    host=os.environ['BACKEND_HOST'],
    port=int(os.environ['BACKEND_PORT']),
    reload=True,
)