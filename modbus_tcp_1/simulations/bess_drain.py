from pyModbusTCP.server import ModbusServer, DataBank
import time

# 1. Setup DataBank (Start with SoC at 100%)
# Address 0: SoC, Address 1: Current Power (kW)
db = DataBank()
db.set_holding_registers(0,) 

# 2. Init Server
# We use port 5020 to avoid permission issues
server = ModbusServer(host='0.0.0.0', port=5020, data_bank=db, no_block=True)

try:
    server.start()
    print("BESS Simulator Online...")
    while True:
        # Get the power setpoint written by the student's script
        power_setpoint = db.get_holding_registers(1)
        
        # Simple logic: If power > 0, decrease SoC
        current_soc = db.get_holding_registers(0)
        if power_setpoint > 0 and current_soc > 0:
            db.set_holding_registers(0, [current_soc - 1])
            print(f"Discharging: SoC is now {current_soc}%")
            
        time.sleep(1)
except Exception:
    server.stop()