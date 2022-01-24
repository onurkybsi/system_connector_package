from arrowhead_client.client.implementations import SyncClient
from arrowhead_client.constants import OrchestrationFlags
from system_connector_package.client.utilities.models import ArrowheadHelperSettings


class _ArrowheadHelper:
    """
    Provides various utilities to use of Arrowhead services.

    The arguments given to ``__init__`` which are stored as-is:

    Args:
        settings: Values to configure ArrowheadHelper
    """

    def __init__(self, settings: ArrowheadHelperSettings):
        self.__init_client(settings)

    def __init_client(self, settings: ArrowheadHelperSettings):
        self._client = SyncClient.create(
            system_name=settings.system_name,
            address=settings.system_address,
            port=settings.system_port
        )
        self._client.setup()

    def add_orchestration_rule(
            self,
            service_definition: str,
            method: str,
            protocol: str = '',
            access_policy: str = '',
            payload_format: str = '',
            orchestration_flags: OrchestrationFlags = OrchestrationFlags.OVERRIDE_STORE,
            **kwargs,
    ) -> None:
        return self._client.add_orchestration_rule(service_definition, method, protocol, access_policy, payload_format,
                                                   orchestration_flags, **kwargs)

    def consume_service(
            self,
            service_definition: str,
            **kwargs
    ):
        return self._client.consume_service(service_definition, **kwargs)


_arrowhead_helper = None


def build_arrowhead_helper(settings: ArrowheadHelperSettings):
    global _arrowhead_helper
    _arrowhead_helper = _ArrowheadHelper(settings)


def get_arrowhead_helper() -> _ArrowheadHelper:
    if _arrowhead_helper is None:
        raise RuntimeError("It should be built first!")
    else:
        return _arrowhead_helper
