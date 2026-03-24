import time
from pyModbusTCP.server import ModbusServer, DataBank

host = "127.0.0.1"
port = 5020

# Create an instance of the server
server = ModbusServer(host=host, port=port, no_block=True)

try:
    print(f"Starting Modbus Server on port {server.port}...")
    server.start()
    print("Server is online. Waiting for connections...")

    while True:
        time.sleep(3)
        print("Waiting for connections...")
        continue
except Exception as e:
    print(f"{e}")
    server.stop()
    print("Server is offline")

