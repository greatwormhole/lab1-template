from uvicorn import Server

from settings import server_settings

server = Server(server_settings)

if __name__ == '__main__':
    server.run()