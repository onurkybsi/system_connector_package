from configparser import ConfigParser
import os

from system_connector_package.client.utilities import arrowhead_helper
from system_connector_package.client.utilities.models import ArrowheadHelperSettings


def __init_configuration_values(configuration_values_file_path: str):
    config_parser = ConfigParser()
    # TO-DO: Are we sure ? How can we get the URI of .ini file ?
    config_parser.read(os.path.abspath(os.path.join(
        os.getcwd(), configuration_values_file_path)))
    return config_parser["client-info"]["system_name"], config_parser["client-info"]["address"], int(
        config_parser["client-info"]["port"])


##
system_name, system_address, system_port = __init_configuration_values("system_connector_package.ini")

arrowhead_helper.build_arrowhead_helper(ArrowheadHelperSettings(
    system_name=system_name,
    system_address=system_address,
    system_port=system_port
))
