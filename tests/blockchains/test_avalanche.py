import unittest.mock

import pytest
from vision.common.blockchains.base import Blockchain

from vision.client.library.blockchains.avalanche import AvalancheClient
from vision.client.library.blockchains.avalanche import AvalancheClientError


@pytest.fixture(scope='module')
@unittest.mock.patch.object(AvalancheClient, '__init__', lambda self: None)
def avalanche_client():
    return AvalancheClient()


def test_get_blockchain_correct(avalanche_client):
    assert avalanche_client.get_blockchain() is Blockchain.AVALANCHE
    assert AvalancheClient.get_blockchain() is Blockchain.AVALANCHE


def test_get_error_class_correct(avalanche_client):
    assert avalanche_client.get_error_class() is AvalancheClientError
    assert AvalancheClient.get_error_class() is AvalancheClientError
