"""Top-level package of the Vision client library.

"""

import threading

import semantic_version as _semantic_version  # type: ignore
from vision.common.configuration import ConfigError as _ConfigError

from vision.client.library.configuration import config as _config
from vision.client.library.configuration import load_config as _load_config
from vision.client.library.exceptions import \
    ClientLibraryError as _ClientLibraryError
from vision.client.library.protocol import \
    is_supported_protocol_version as _is_supported_protocol_version


class ConfigurationEntrypoint:
    _instance = None
    _lock = threading.Lock()
    _is_initialized = False

    def __new__(self):
        if self._instance is None:
            with self._lock:
                if not self._instance:
                    self._instance = super().__new__(self)
        return self._instance

    def is_initialized(self) -> bool:
        with self._lock:
            toReturn = self._is_initialized
        return toReturn

    def initialize(self, mainnet: bool):
        if self._is_initialized:
            # already initialized
            return

        try:
            _load_config()
        except _ConfigError:
            raise _ClientLibraryError('error loading config')
        environment = 'mainnet' if mainnet else 'testnet'
        protocol_version = _semantic_version.Version(
            _config['protocol'][environment])
        if not _is_supported_protocol_version(protocol_version):
            raise _ClientLibraryError('unsupported Vision protocol version',
                                      protocol_version=protocol_version)
        self._is_initialized = True


_configurationSingleton: ConfigurationEntrypoint = ConfigurationEntrypoint()


def initialize_library(mainnet: bool) -> None:
    """Initialize the Vision client library. The function is thread-safe
    and performs the initialization only once at the first invocation.

    Parameters
    ----------
    mainnet : bool
        If True, the client library is initialized for mainnet
        operation. Otherwise, it is initialized for testnet operation.

    Raises
    ------
    ClientLibraryError
        If the library cannot be initialized.

    """

    # No matter how many times this object is initialized, it will only
    # be initialized once.
    _configurationSingleton.initialize(mainnet)

    # with _initialized.get_lock():
    #     if not _initialized.value:
    #         try:
    #             _load_config()
    #         except _ConfigError:
    #             raise _ClientLibraryError('error loading config')
    #         environment = 'mainnet' if mainnet else 'testnet'
    #         protocol_version = _semantic_version.Version(
    #             _config['protocol'][environment])
    #         if not _is_supported_protocol_version(protocol_version):
    #             raise _ClientLibraryError(
    #                 'unsupported Vision protocol version',
    #                 protocol_version=protocol_version)
    #         _initialized.value = True
