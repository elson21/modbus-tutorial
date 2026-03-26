# models/BESS.py

from models.MicrogridAssets import MicrogridAssets

class BESS(MicrogridAssets):
    """
    BESS class defines the BESS asset.
    It inherits from the MicrogridAssets class.
    """
    def __init__(
        self,
        name,
        ip_address,
        port,
        unit_id,
        data_bank,          # Memory storage for the modbus server. Holds the mapped values.
        string_count: int,  # Number of strings in the BESS
        pack_count: int,    # Number of packs in each string        
        cluster_count: int  # Number of clusters in each pack
    ):
        super().__init__(
            name,
            ip_address,
            port,
            unit_id,
            data_bank
        )

        # Initialize BESS strings
        self.bess_strings = [
            BESSString(i, data_bank, pack_count, cluster_count) 
            for i in range(string_count)
        ]

    def update(self) -> None:
        """
        Update the BESS data.
        """
        # TODO: Implement update logic for voltage, current, and power

        for string in self.bess_strings:
            string.update()


class BESSString:
    """
    BESSString class defines the BESS strings.
    Each string has a base address of 30000 + (index-1 * 5000).

    For example:
        String 1: Modbus address 30000
        String 2: Modbus address 35000
        String 3: Modbus address 40000
    """
    def __init__(
        self,
        index: int,
        data_bank: DataBank,
        pack_count: int,
        cluster_count: int
    ):
        self.index = index  # String index
        self.db = data_bank

        # Base address for string: 30000 + (index * 5000)
        self.base_address = 30000 + (index * 5000)  # TODO: Abstract this to receive data from manufacturer modbus map

        # Initialize BESS packs: SSppcc
        # SS: String index
        # pp: Pack index
        # cc: Cluster index
        self.bess_packs = [
            BESSPack(i, self.index, self.base_address, self.db, cluster_count)
            for i in range(pack_count)
        ]

    def update(self) -> None:
        """
        Update the BESS strin data
        """
        # TODO: Implement update logic for voltage.

        for pack in self.bess_packs:
            pack.update()

class BESSPack:
    """
    BESSPack class defines the BESS packs
    """
    def __init__(
        self,
        index: int,
        data_bank: DataBank,
        base_address: int,
        cluster_count: int
    ):
        self.index = index
        self.db = data_bank
        self.base_address = base_address
        self.cluster_count = cluster_count

        # Initialize BESS clusters: SSppcc
        # SS: String index
        # pp: Pack index
        # cc: Cluster index
        self.bess_clusters = [
            BESSCluster(i, self.index, self.base_address, self.db, cluster_count)
            for i in range(cluster_count)
        ]
    
    def update(self) -> None:
        """
        Update the BESS pack data
        """
        #TODO: Implement update logic for max cell voltage, min cell voltage,
        # max cell temperature, min cell temperature, and pack voltage.

        for cluster in self.bess_clusters:
            cluster.update()

class BESSCluster:
    pass