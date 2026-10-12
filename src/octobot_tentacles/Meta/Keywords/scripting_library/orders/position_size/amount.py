#  Drakkar-Software OctoBot-Tentacles
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

import octobot_trading.modes.script_keywords as script_keywords
import octobot_trading.errors as trading_errors
import octobot_trading.enums as trading_enums
import tentacles.Meta.Keywords.scripting_library.data.reading.exchange_private_data as exchange_private_data
import octobot_commons.constants as commons_constants


async def get_amount(
    context=None,
    input_amount=None,
    side=trading_enums.TradeOrderSide.BUY.value,
    reduce_only=True,
    is_stop_order=False,
    use_total_holding=False,
    unknown_portfolio_on_creation=False,
    target_price=None
):
    amount_type, position_percent = script_keywords.parse_quantity(input_amount)
    if (
        amount_type in (script_keywords.QuantityType.POSITION_PERCENT,
                        script_keywords.QuantityType.POSITION_PERCENT_ALIAS)
        and position_percent is not None and position_percent > 0
        and not context.exchange_manager.is_future
    ):
        # Spot positions are actual base-asset holdings, not futures contracts.
        # Keep the same position-percent syntax without constructing a synthetic
        # futures position over a spot portfolio.
        amount_value = abs(exchange_private_data.open_position_size(context)) * position_percent / 100
        amount_value = await script_keywords.adapt_amount_to_holdings(
            context, amount_value, side, use_total_holding, reduce_only,
            is_stop_order, target_price=target_price
        )
    else:
        amount_value = await script_keywords.get_amount_from_input_amount(
            context=context,
            input_amount=input_amount,
            side=side,
            reduce_only=reduce_only,
            is_stop_order=is_stop_order,
            use_total_holding=use_total_holding,
            target_price=target_price
        )
    if unknown_portfolio_on_creation:
        # no way to check if the amount is valid when creating order
        _, amount_value = script_keywords.parse_quantity(input_amount)
    return amount_value
