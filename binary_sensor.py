import logging
import subprocess

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    _LOGGER.warn("Adding entities")
    entities = [TimandesBinarySensor()]
    add_entities(entities)

class TimandesBinarySensor(BinarySensorEntity):
    def update(self):
        _LOGGER.warn("Updating sensor states")
        exit_code = subprocess.call(["ping", "-c", "1", "192.168.31.111"])

        self._attr_is_on = exit_code == 0
