#  Drakkar-Software OctoBot-Commons
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
import pytest

import numpy as np


from tentacles.Meta.DSL_operators.exchange_operators.tests import (
    historical_prices,
    historical_volume,
    exchange_manager_with_candles,
    interpreter,
)


@pytest.mark.asyncio
async def test_close_operator(interpreter, historical_prices):
    # no param, use context values: SYMBOL, TIME_FRAME: BTC/USDT, 1h
    close = await interpreter.interprete("close")
    assert np.array_equal(close, historical_prices)
    # ensure symbol parameters are used when provided
    assert np.array_equal(await interpreter.interprete("close('ETH/USDT')"), historical_prices / 2) # 1h ETH
    assert np.array_equal(await interpreter.interprete("close('BTC/USDT')"), historical_prices) # 1h BTC

    # ensure time frame is used when provided
    assert np.array_equal(await interpreter.interprete("close(None, '4h')"), historical_prices * 2) # 4h BTC
    assert np.array_equal(await interpreter.interprete("close(None, '1h')"), historical_prices) # 1h BTC

    # ensure symbol and time frame are used when provided
    assert np.array_equal(await interpreter.interprete("close('BTC/USDT', '1h')"), historical_prices) # 4h BTC rsi value
    assert np.array_equal(await interpreter.interprete("close('BTC/USDT', '4h')"), historical_prices * 2) # 4h BTC rsi value
    assert np.array_equal(await interpreter.interprete("close('ETH/USDT', '1h')"), historical_prices / 2) # 1h ETH rsi value
    with pytest.raises(KeyError): # no 4h ETH candles
        await interpreter.interprete("close('ETH/USDT', '4h')")
