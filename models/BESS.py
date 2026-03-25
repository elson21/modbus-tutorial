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
        data_bank,
        string_count: int,
        pack_count: int,  # Number of packs in each string        
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
        self.bess_strings = [BESSString(i, data_bank) for i in range(string_count)]


class BESSString:
    """
    BESSString class defines the BESS strings.
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

        # Base address for string: 30000 + (index * 2000)
        self.base_address = 30000 + (index * 2000)

        # Initialize BESS packs: SSppcc
        # SS: String index
        # pp: Pack index
        # cc: Cluster index
        self.bess_packs = [
            BESSPack(i, self.index, self.base_address, self.db, cluster_count)
            for i in range(pack_count)
        ]

class BESSPack:
    pass

class BESSCluster:
    pass