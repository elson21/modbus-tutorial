import logging
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext,
)

logger = logging.getLogger(__name__)

def create_datastore() -> ModbusServerContext:
    """
    Initializes and returns a ModbusServerContext populated with placeholder data.
    """
    logger.info("Initializing Modbus dummy datastore...")
    # Initialize data blocks with default values
    # block size: 100 registers/coils starting at address 0.
    coils = ModbusSequentialDataBlock(0, [False] * 100)
    discrete_inputs = ModbusSequentialDataBlock(0, [False] * 100)
    holding_registers = ModbusSequentialDataBlock(0, [0] * 100)
    input_registers = ModbusSequentialDataBlock(0, [0] * 100)
    
    # Store them in a slave context.
    slave_context = ModbusDeviceContext(
        di=discrete_inputs,
        co=coils,
        hr=holding_registers,
        ir=input_registers
    )
    
    # Return a single context server
    return ModbusServerContext(devices=slave_context, single=True)
