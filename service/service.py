import logging
from pprint import pprint

from constants import access_token, api_key
from kiteconnect import KiteConnect, KiteTicker


def ticker_service():
    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)

    kws = KiteTicker(api_key, access_token)

    tokens = [3050241]

    received_ticks = []

    # Callback for tick reception.
    def on_ticks(ws, ticks):
        pprint(ticks)
        received_ticks = ticks

    # Callback for successful connection.
    def on_connect(ws, response):
        logging.info("Successfully connected. Response: {}".format(response))
        ws.subscribe(tokens)
        ws.set_mode(ws.MODE_FULL, tokens)
        logging.info("Subscribe to tokens in Full mode: {}".format(tokens))

    # Callback when current connection is closed.
    def on_close(ws, code, reason):
        logging.info("Connection closed: {code} - {reason}".format(code=code, reason=reason))

    # Callback when connection closed with error.
    def on_error(ws, code, reason):
        logging.info("Connection error: {code} - {reason}".format(code=code, reason=reason))

    # Callback when reconnect is on progress
    def on_reconnect(ws, attempts_count):
        logging.info("Reconnecting: {}".format(attempts_count))

    # Callback when all reconnect failed (exhausted max retries)
    def on_noreconnect(ws):
        logging.info("Reconnect failed.")

    # Assign the callbacks.
    kws.on_ticks = on_ticks
    kws.on_close = on_close
    kws.on_error = on_error
    kws.on_connect = on_connect
    kws.on_reconnect = on_reconnect
    kws.on_noreconnect = on_noreconnect

    # Infinite loop on the main thread. Nothing after this will run.
    # You have to use the pre-defined callbacks to manage subscriptions.
    kws.connect(threaded=True)

    yield received_ticks


if __name__ == "__main__":
    ticker_service()
