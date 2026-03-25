import time
from random import uniform
from pyModbusTCP.server import ModbusServer, DataBank

host = "127.0.0.1"
port = 5020

# Create an instance of the server
server = ModbusServer(host=host, port=port, no_block=True)

# Modbus configuration
db = DataBank()

try:
    print(f"Starting Modbus Server on port {port}...")
    server.start()
    print("Server is online.")

    while True:
        i = 0
        db.set_holding_registers(0, [uniform(0, 100)])
        value = db.get_holding_registers(i)
        print(f"Holding register (03): {value}")
        i += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("Server closed by keyboard interrupt.")
except Exception as e:
    print(f"Server error: {e}")
finally:
    print("Server stopped.")
    server.stop()
