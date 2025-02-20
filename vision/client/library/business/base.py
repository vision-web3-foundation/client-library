"""Base classes for all business logic interactors and errors.

"""
import abc

from vision.client.library.exceptions import ClientLibraryError


class InteractorError(ClientLibraryError):
    """Base exception class for all interactor errors.

    """
    pass


class Interactor(abc.ABC):
    """Base class for all interactors.

    """
    pass
