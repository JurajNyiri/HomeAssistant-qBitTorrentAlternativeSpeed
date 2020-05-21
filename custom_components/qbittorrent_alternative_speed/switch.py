__version__ = "1.3.1"

import logging
import voluptuous as vol

from qbittorrentapi import Client

try:
    from homeassistant.components.switch import (
        SwitchEntity, PLATFORM_SCHEMA)
except ImportError:
    from homeassistant.components.switch import (
        SwitchDevice as SwitchEntity, PLATFORM_SCHEMA)


from homeassistant.const import (
    CONF_PROTOCOL, CONF_NAME, CONF_PORT, CONF_HOST, CONF_USERNAME, CONF_PASSWORD)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_PORT, default="8080"): cv.string,
    vol.Required(CONF_USERNAME): cv.string,
    vol.Optional(CONF_PROTOCOL, default="http"): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
    vol.Optional(CONF_NAME, default="qbittorrent_alternative_speed"): cv.string
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    host = config.get(CONF_PROTOCOL)+"://" + \
        config.get(CONF_HOST)+":"+config.get(CONF_PORT)
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)
    name = config.get(CONF_NAME)

    add_devices([qbittorrent_alternative_speed(
        host, username, password, name)], True)


class qbittorrent_alternative_speed(SwitchEntity):

    def __init__(self, host, username, password, name):
        self.host = host
        self.username = username
        self.password = password
        self._name = name
        self.qb = Client(host=self.host, username=self.username,
                         password=self.password)
        self.signin()

    def signin(self):
        self.qb.auth_log_in()
        self._state = int(self.qb.transfer.speed_limits_mode)

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return (self._state == 1)

    def update(self):
        try:
            self._state = int(self.qb.transfer.speed_limits_mode)
        except:
            self.signin()
        return

    def turn_on(self):
        self.update()
        if(self._state == 0):
            self.qb.transfer.toggle_speed_limits_mode()

    def turn_off(self):
        self.update()
        if(self._state == 1):
            self.qb.transfer.toggle_speed_limits_mode()
