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
import octobot.enums

import tentacles.Services.Interfaces.web_interface.controllers.octobot_authentication as octobot_authentication
import tentacles.Services.Interfaces.web_interface.controllers.community_authentication as community_authentication
import tentacles.Services.Interfaces.web_interface.controllers.backtesting as backtesting
import tentacles.Services.Interfaces.web_interface.controllers.commands as commands
import tentacles.Services.Interfaces.web_interface.controllers.about as about
import tentacles.Services.Interfaces.web_interface.controllers.community as community
import tentacles.Services.Interfaces.web_interface.controllers.configuration as configuration
import tentacles.Services.Interfaces.web_interface.controllers.tentacles_config as tentacles_config
import tentacles.Services.Interfaces.web_interface.controllers.dashboard as dashboard
import tentacles.Services.Interfaces.web_interface.controllers.errors as errors
import tentacles.Services.Interfaces.web_interface.controllers.octobot_help as octobot_help
import tentacles.Services.Interfaces.web_interface.controllers.home as home
import tentacles.Services.Interfaces.web_interface.controllers.interface_settings as interface_settings
import tentacles.Services.Interfaces.web_interface.controllers.logs as logs
import tentacles.Services.Interfaces.web_interface.controllers.medias as medias
import tentacles.Services.Interfaces.web_interface.controllers.terms as terms
import tentacles.Services.Interfaces.web_interface.controllers.trading as trading
import tentacles.Services.Interfaces.web_interface.controllers.portfolio as portfolio
import tentacles.Services.Interfaces.web_interface.controllers.profiles as profiles
import tentacles.Services.Interfaces.web_interface.controllers.automation as automation
import tentacles.Services.Interfaces.web_interface.controllers.reboot as reboot
import tentacles.Services.Interfaces.web_interface.controllers.welcome as welcome
import tentacles.Services.Interfaces.web_interface.controllers.robots as robots
import tentacles.Services.Interfaces.web_interface.controllers.distributions.market_making as market_making
import tentacles.Services.Interfaces.web_interface.controllers.dsl as dsl


def register(blueprint, distribution: octobot.enums.OctoBotDistribution):
    if distribution is octobot.enums.OctoBotDistribution.DEFAULT:
        community_authentication.register(blueprint)
        backtesting.register(blueprint)
        about.register(blueprint)
        community.register(blueprint)
        configuration.register(blueprint)
        tentacles_config.register(blueprint)
        dashboard.register(blueprint)
        octobot_help.register(blueprint)
        home.register(blueprint)
        interface_settings.register(blueprint)
        logs.register(blueprint)
        trading.register(blueprint)
        portfolio.register(blueprint)
        profiles.register(blueprint)
        automation.register(blueprint)
        welcome.register(blueprint)
        dsl.register(blueprint)
    elif distribution is octobot.enums.OctoBotDistribution.MARKET_MAKING:
        market_making.register(blueprint)
    # common routes
    octobot_authentication.register(blueprint)
    robots.register(blueprint)
    reboot.register(blueprint)
    terms.register(blueprint)
    errors.register(blueprint)
    commands.register(blueprint)
    medias.register(blueprint)


__all__ = [
    "register",
]
