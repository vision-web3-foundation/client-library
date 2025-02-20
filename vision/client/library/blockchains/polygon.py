"""Module for Polygon-specific clients and errors. Since Polygon is
Ethereum-compatible, the client implementation inherits from the
vision.client.library.blockchains.ethereum module.

"""
from vision.common.blockchains.base import Blockchain

from vision.client.library.blockchains import BlockchainClientError
from vision.client.library.blockchains.ethereum import EthereumClient
from vision.client.library.blockchains.ethereum import EthereumClientError


class PolygonClientError(EthereumClientError):
    """Exception class for all Polygon client errors.

    """
    pass


class PolygonClient(EthereumClient):
    """Polygon-specific blockchain client.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.POLYGON

    @classmethod
    def get_error_class(cls) -> type[BlockchainClientError]:
        # Docstring inherited
        return PolygonClientError
