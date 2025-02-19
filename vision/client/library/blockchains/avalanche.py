"""Module for Avalanche-specific clients and errors. Since the
Avalanche C-Chain is Ethereum-compatible, the client implementation
inherits from the vision.client.library.blockchains.ethereum module.

"""
from vision.common.blockchains.base import Blockchain

from vision.client.library.blockchains import BlockchainClientError
from vision.client.library.blockchains.ethereum import EthereumClient
from vision.client.library.blockchains.ethereum import EthereumClientError


class AvalancheClientError(EthereumClientError):
    """Exception class for all Avalanche client errors.

    """
    pass


class AvalancheClient(EthereumClient):
    """Avalanche-specific blockchain client.

    """
    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.AVALANCHE

    @classmethod
    def get_error_class(cls) -> type[BlockchainClientError]:
        # Docstring inherited
        return AvalancheClientError
