#  Drakkar-Software OctoBot-Interfaces
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import flask
import octobot.enums

import tentacles.Services.Interfaces.web_interface.api.config as config
import tentacles.Services.Interfaces.web_interface.api.exchanges as exchanges
import tentacles.Services.Interfaces.web_interface.api.feedback as feedback
import tentacles.Services.Interfaces.web_interface.api.metadata as metadata
import tentacles.Services.Interfaces.web_interface.api.trading as trading
import tentacles.Services.Interfaces.web_interface.api.user_commands as user_commands
import tentacles.Services.Interfaces.web_interface.api.bots as bots
import tentacles.Services.Interfaces.web_interface.api.webhook as webhook
import tentacles.Services.Interfaces.web_interface.api.tentacles_packages as tentacles_packages
import tentacles.Services.Interfaces.web_interface.api.dsl as dsl

from tentacles.Services.Interfaces.web_interface.api.webhook import (
    has_webhook,
    register_webhook
)



def register(distribution: octobot.enums.OctoBotDistribution):
    blueprint = flask.Blueprint('api', __name__, url_prefix='/api', template_folder="")
    if distribution is octobot.enums.OctoBotDistribution.DEFAULT:
        feedback.register(blueprint)
        bots.register(blueprint)
        webhook.register(blueprint)
        tentacles_packages.register(blueprint)

    elif distribution is octobot.enums.OctoBotDistribution.MARKET_MAKING:
        pass

    # common routes
    config.register(blueprint)
    exchanges.register(blueprint)
    metadata.register(blueprint)
    trading.register(blueprint)
    user_commands.register(blueprint)
    dsl.register(blueprint)
    return blueprint


__all__ = [
    "has_webhook",
    "register_webhook",
    "register",
]
