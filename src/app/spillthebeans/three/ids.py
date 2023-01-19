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
