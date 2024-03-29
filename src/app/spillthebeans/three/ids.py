# A set of functions that create pattern-matching callbacks of the subcomponents
class Ids:

    # Moon
    moon = lambda aio_id: {
        "component": "MoonAIO",
        "subcomponent": "moon",
        "aio_id": aio_id,
    }

    # PagenotfoundThreejs
    pagenotfound = lambda aio_id: {
        "component": "PagenotfoundThreejsAIO",
        "subcomponent": "pagenotfound",
        "aio_id": aio_id,
    }

    # Wind
    wind = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "wind",
        "aio_id": aio_id,
    }
    map_toggle = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "map_toggle",
        "aio_id": aio_id,
    }
    env_toggle = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "env_toggle",
        "aio_id": aio_id,
    }
    tooltip_toggle = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "tooltip_toggle",
        "aio_id": aio_id,
    }
    stats_toggle = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "stats_toggle",
        "aio_id": aio_id,
    }
    results_toggle = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "results_toggle",
        "aio_id": aio_id,
    }
    set_limits = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "set_limits",
        "aio_id": aio_id,
    }
    show_limits_input = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "show_limits_input",
        "aio_id": aio_id,
    }
    minimum = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "minimum",
        "aio_id": aio_id,
    }
    maximum = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "maximum",
        "aio_id": aio_id,
    }
    toast_wind = lambda aio_id: {
        "component": "WtgviewerAIO",
        "subcomponent": "toast_wind",
        "aio_id": aio_id,
    }