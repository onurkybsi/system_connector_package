from system_connector_package.client.utilities.arrowhead_helper import get_arrowhead_helper


def say_n_times_something(what, times):
    get_arrowhead_helper().add_orchestration_rule("say-n-times-something", "GET")
    response = get_arrowhead_helper().consume_service("say-n-times-something")
    print(response)
    return None
