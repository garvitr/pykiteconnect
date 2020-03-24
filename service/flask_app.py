import os
import json
import logging
import subprocess
import time
from datetime import date, datetime
from decimal import Decimal

import flask

from constants import login_template, index_template, PORT, HOST, api_key, api_secret, error_message, login_url, \
    console_url, redirect_url, trade_url, stop_trade_url, trade_template

from flask import Flask, request, jsonify, session
from kiteconnect import KiteConnect
from service import ticker_service

serializer = lambda obj: isinstance(obj, (date, datetime, Decimal)) and str(obj)  # noqa

# App
app = Flask(__name__)
app.secret_key = os.urandom(24)

access_token = ""
kws = ""


def get_kite_client():
    kite = KiteConnect(api_key=api_key)
    if "access_token" in session:
        kite.set_access_token(session["access_token"])
    return kite


@app.route("/")
def index():
    return index_template.format(
        api_key=api_key,
        redirect_url=redirect_url,
        console_url=console_url,
        login_url=login_url,
        trade_url=trade_url
    )


@app.route("/login")
def login():
    # TODO: add accessToken fetch from DB

    request_token = request.args.get("request_token")

    if not request_token:
        return error_message

    kite = get_kite_client()
    data = kite.generate_session(request_token, api_secret=api_secret)
    session["access_token"] = data["access_token"]

    return login_template.format(
        access_token=data["access_token"],
        user_data=json.dumps(
            data,
            indent=4,
            sort_keys=True,
            default=serializer
        )
    )


@app.route("/algo")
def algo():
    global kws
    kws = ticker_service()

    return trade_template.format(
        indent=4,
        sort_keys=True,
        default=serializer
    )


@app.route("/stopalgo")
def stop_algo():
    kws.stop()
    return index_template.format(
        api_key=api_key,
        redirect_url=redirect_url,
        console_url=console_url,
        login_url=login_url,
        trade_url=trade_url
    )


@app.route("/holdings.json")
def holdings():
    kite = get_kite_client()
    return jsonify(holdings=kite.holdings())


@app.route("/orders.json")
def orders():
    kite = get_kite_client()
    return jsonify(orders=kite.orders())


if __name__ == "__main__":
    logging.info("Starting server: http://{host}:{port}".format(host=HOST, port=PORT))
    app.run(host=HOST, port=PORT, debug=True)
