#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev_test_cex_too_long_uri_test.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import threading
import os


# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            print(oldest_stream_data_from_stream_buffer)
            #pass


binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com")

# start a worker process to move the received stream_data from the stream_buffer to a print function
worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
worker_thread.start()

markets = ['bnbbtc', 'ethbtc', 'btcusdt', 'bchabcusdt', 'xrpusdt', 'rvnbtc', 'ltcusdt', 'adausdt', 'eosusdt',
           'neousdt', 'bnbusdt', 'adabtc', 'ethusdt', 'trxbtc', 'trxbtc', 'bchabcbtc', 'ltcbtc', 'xrpbtc',
           'ontbtc', 'bttusdt', 'eosbtc', 'xlmbtc', 'bttbtc', 'tusdusdt', 'xlmusdt', 'qkcbtc', 'zrxbtc',
           'neobtc', 'adaeth', 'icxusdt', 'btctusd', 'icxbtc', 'btcusdc', 'wanbtc', 'zecbtc', 'wtcbtc',
           'batbtc', 'adabnb', 'etcusdt', 'qtumusdt', 'xmrbtc', 'trxeth', 'adatusd', 'trxxrp', 'trxbnb',
           'dashbtc', 'rvnbnb', 'bchabctusd', 'etcbtc', 'bnbeth', 'ethpax', 'nanobtc', 'xembtc', 'xrpbnb',
           'bchabcpax', 'xrpeth', 'bttbnb', 'ltcbnb', 'agibtc', 'zrxusdt', 'xlmbnb', 'ltceth', 'eoseth',
           'ltctusd', 'polybnb', 'scbtc', 'steembtc', 'trxtusd', 'npxseth', 'kmdbtc', 'polybtc', 'gasbtc',
           'engbtc', 'zileth', 'xlmeth', 'eosbnb', 'xrppax', 'lskbtc', 'npxsbtc', 'xmrusdt', 'ltcpax', 'xmrusdt',
           'ethtusd', 'batusdt', 'mcobtc', 'neoeth', 'bntbtc', 'eostusd', 'lrcbtc', 'funbtc', 'zecusdt',
           'bnbpax', 'linkusdt', 'hceth', 'zrxeth', 'icxeth', 'xmreth', 'neobnb', 'etceth', 'zeceth', 'xmrbnb',
           'wanbnb', 'zrxbnb', 'agibnb', 'funeth', 'arketh', 'engeth']

channels = ['trade', 'kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_12h', 'depth5']

stream_id = binance_websocket_api_manager.create_stream(channels, markets)


while True:
    #binance_websocket_api_manager.print_summary()
    #binance_websocket_api_manager.print_stream_info(stream_id)
    binance_websocket_api_manager.get_stream_subscriptions(stream_id)
    time.sleep(3)