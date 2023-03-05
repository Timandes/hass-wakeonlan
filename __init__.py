import logging

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    _LOGGER.warn("Setting states")
    hass.states.set("timandes.hello_world", "Terrific")

    return True
