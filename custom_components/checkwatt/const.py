"""Constants for the Checkwatt integration."""
from typing import Final

DOMAIN = "checkwatt"
CONF_MONITORED_SITES = "monitored_sites"
CONF_UPDATE_INTERVAL = 15
ATTRIBUTION = "Data provided by Checkwwatt EnergyInBalance"
MANUFACTURER = "Checkwatt"

CONF_DETAILED_SENSORS: Final = "show_details"
CONF_DETAILED_ATTRIBUTES: Final = "show_detailed_attributes"


# Misc
P_UNKNOWN = "Unknown"

# Plant Sensor Attributes
CHECKWATT_MODEL = "Checkwatt"
C_ADR = "Street Address"
C_ZIP = "Zip Code"
C_CITY = "City"
C_TOMORROW = "Tomorrow revenue"
C_UPDATE_TIME = "Last update"
C_NEXT_UPDATE_TIME = "Next update"
C_FCRD_STATUS = "FCR-D Status"
C_FCRD_STATE = "FCR-D State"
C_FCRD_DATE = "FCR-D Date"
