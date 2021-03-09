from homeassistant.components.vacuum import (
    PLATFORM_SCHEMA,
    STATE_CLEANING,
    STATE_DOCKED,
    STATE_ERROR,
    STATE_IDLE,
    STATE_PAUSED,
    STATE_RETURNING,
    SUPPORT_BATTERY,
    SUPPORT_FAN_SPEED,
    SUPPORT_LOCATE,
    SUPPORT_PAUSE,
    SUPPORT_RETURN_HOME,
    SUPPORT_SEND_COMMAND,
    SUPPORT_START,
    SUPPORT_STATE,
    VacuumEntity,
)

DOMAIN = "deebot"
CONF_COUNTRY = "country"
CONF_CONTINENT = "continent"
CONF_DEVICEID = "deviceid"
CONF_LIVEMAPPATH = "livemappath"
CONF_LIVEMAP = "live_map"
CONF_SHOWCOLORROOMS = "show_color_rooms"
DEEBOT_DEVICES = "deebot_devices"
STATE_CODE_TO_STATE = {
    "STATE_IDLE": STATE_IDLE,
    "STATE_CLEANING": STATE_CLEANING,
    "STATE_RETURNING": STATE_RETURNING,
    "STATE_DOCKED": STATE_DOCKED,
    "STATE_ERROR": STATE_ERROR,
    "STATE_PAUSED": STATE_PAUSED,
}