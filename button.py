import logging

from homeassistant.components.button import (
    ButtonEntity,
)

from wakeonlan import send_magic_packet

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    _LOGGER.warn("Adding entities")
    entities = [TimandesButton()]
    add_entities(entities)

class TimandesButton(ButtonEntity):
    def press(self) -> None:
        """Handle the button press."""
        _LOGGER.warn("Sending packets")
        send_magic_packet("00.24.1d.86.bf.58", ip_address="192.168.31.255")