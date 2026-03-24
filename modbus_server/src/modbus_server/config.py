import logging

class ServerConfig:
    """Configuration settings for the Modbus TCP Server."""
    HOST: str = "0.0.0.0"
    PORT: int = 5020
    LOG_LEVEL: int = logging.INFO
