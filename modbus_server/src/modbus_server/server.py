import logging
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusServerContext

from .config import ServerConfig

logger = logging.getLogger(__name__)

async def run_server(context: ModbusServerContext) -> None:
    """
    Starts the asynchronous Modbus TCP server given a datastore context.
    """
    address = (ServerConfig.HOST, ServerConfig.PORT)
    logger.info(f"Starting async Modbus TCP Server on {ServerConfig.HOST}:{ServerConfig.PORT}")
    
    await StartAsyncTcpServer(
        context=context,
        address=address
    )
