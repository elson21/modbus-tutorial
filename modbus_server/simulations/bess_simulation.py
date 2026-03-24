import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

async def run_bess_simulator():
    # Initializing registers: SoC=50%, Power=0kW
    # 30001 (Input Registers) for read-only data like SoC
    # 40001 (Holding Registers) for setpoints
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0,*100),
        co=ModbusSequentialDataBlock(0,*100),
        ir=ModbusSequentialDataBlock(0,), # Address 0=SoC, 1=Current Power
        hr=ModbusSequentialDataBlock(0,) # Address 1=Power Setpoint
    )
    context = ModbusServerContext(slaves=store, single=True)
    
    print("BESS Simulator started on localhost:5020")
    await StartAsyncTcpServer(context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    asyncio.run(run_bess_simulator())