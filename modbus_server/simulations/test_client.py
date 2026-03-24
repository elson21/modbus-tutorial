import asyncio
from pymodbus.client import AsyncModbusTcpClient

async def run_client() -> None:
    client = AsyncModbusTcpClient('127.0.0.1', port=5020)
    print("Connecting to local Modbus Server...")
    await client.connect()
    
    if client.connected:
        print("Connected! Reading holding registers...")
        # Read 10 registers starting at address 0
        response = await client.read_holding_registers(address=0, count=10)
        if not response.isError():
            print(f"Registers values: {response.registers}")
        else:
            print(f"Error reading registers: {response}")
            
        print("Writing value 42 to holding register 1...")
        write_res = await client.write_register(address=1, value=42)
        if not write_res.isError():
            print("Write successful. Reading again...")
            new_val = await client.read_holding_registers(address=1, count=1)
            print(f"New register 1 value: {new_val.registers}")
        else:
            print("Error writing register.")
    else:
        print("Failed to connect.")
    client.close()

if __name__ == '__main__':
    asyncio.run(run_client())
