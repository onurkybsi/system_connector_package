class ArrowheadHelperSettings:
    """
    Represents configuration values of ArrowheadHelper

    Args:
        system_name: System name of the client of system_connector_package
        system_address: System address of the client of system_connector_package
        system_port: System port of the client of system_connector_package
    """

    def __init__(self, system_name, system_address, system_port) -> None:
        self.system_name = system_name
        self.system_address = system_address
        self.system_port = system_port
