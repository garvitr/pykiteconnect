login_template = """
    <h2 style="color: green">Success</h2>
    <a target="_blank" href="/algo"><h4>Start Trading</h4></a>
    <div>Access token: <b>{access_token}</b></div>
    <h4>User login data</h4>
    <pre>{user_data}</pre>
    <a target="_blank" href="/holdings.json"><h4>Fetch user holdings</h4></a>
    <a target="_blank" href="/orders.json"><h4>Fetch user orders</h4></a>
    <a target="_blank" href="https://kite.trade/docs/connect/v1/"><h4>Checks Kite Connect docs for other calls.</h4></a>"""

index_template = """
    <div>Make sure your app with api_key - <b>{api_key}</b> has set redirect to <b>{redirect_url}</b>.</div>
    <a href="{login_url}"><h1>Login</h1></a>"""

error_message = """
            <span style="color: red">
                Error while generating request token.
            </span>
            <a href='/'>Try again.<a>"""

api_key = "00mywyvyrt2hm2uj"
api_secret = "vmt9up15kmwj2uwoei7dlyc8gya48slq"
access_token = "rO7PvCzx3v0lk7su2iZ04u0MQIXNAHj1"
PORT = 5010
HOST = "127.0.0.1"
login_url = "https://kite.trade/connect/login?api_key={api_key}".format(api_key=api_key)
console_url = "https://developers.kite.trade/apps/{api_key}".format(api_key=api_key)