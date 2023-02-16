from __future__ import annotations

import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "energy_metrics"


@asyncio.coroutine
def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.async_set('energy_metrics.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True
