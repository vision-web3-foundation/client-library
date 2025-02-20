"""Common exceptions for the Vision client.

"""
from vision.common.exceptions import BaseError


class ClientError(BaseError):
    """Base exception class for all Vision client errors.

    """
    pass


class ClientLibraryError(ClientError):
    """Base exception class for all Vision client library errors.

    """
    pass
