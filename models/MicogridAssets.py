"""
The MicrogridAssets class is a base class for all microgrid assets.
It provides a common interface for all microgrid assets.
"""

from pyModbusTCP.server import DataBank

class MicrogridAssets:
    def __init__(
        self,
        name: str,
        ip_address: str,
        port: int,
        unint_id: int,
        data_bank: DataBank
    ):
        self.name = name
        self.ip_address = ip_address
        self.port = port
        self.unit_id = unit_id
        self.data_bank = data_bank
    
    def update(self) -> None:
        # This is a placeholder for the update method
        # Specific assets should override this method
        pass