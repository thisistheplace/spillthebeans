# A set of functions that create pattern-matching callbacks of the subcomponents
class Ids:

    # Moon
    moon = lambda aio_id: {
        "component": "MoonAIO",
        "subcomponent": "moon",
        "aio_id": aio_id,
    }
