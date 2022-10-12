# A set of functions that create pattern-matching callbacks of the subcomponents
class Ids:

    # SpillthebeansAIO
    three = lambda aio_id: {
        "component": "SpillthebeansAIO",
        "subcomponent": "three",
        "aio_id": aio_id
    }

    sidebar_open = lambda aio_id: {
        "component": "SpillthebeansAIO",
        "subcomponent": "sidebar_open",
        "aio_id": aio_id
    }

    card_row = lambda aio_id: {
        "component": "SpillthebeansAIO",
        "subcomponent": "card_row",
        "aio_id": aio_id
    }

    card = lambda aio_id: {
        "component": "CardAIO",
        "subcomponent": "card",
        "aio_id": aio_id
    }

    popover = lambda aio_id: {
        "component": "CardAIO",
        "subcomponent": "popover",
        "aio_id": aio_id
    }