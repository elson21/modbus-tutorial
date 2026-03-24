import asyncio
import logging

from .config import ServerConfig
from .datastore import create_datastore
from .server import run_server

def setup_logging() -> None:
    """Configures the root logger using ServerConfig logging settings."""
    logging.basicConfig(
        level=ServerConfig.LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

async def main() -> None:
    """Main application entry point."""
    setup_logging()
    
    # 1. Provide datastore logic isolated per SRP
    context = create_datastore()
    
    # 2. Start running the server
    await run_server(context)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user.")
