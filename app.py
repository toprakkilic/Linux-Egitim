from flask import Flask, request, redirect, Response
from datetime import datetime
import base64
import gzip

app = Flask(__name__)

winners = []

@app.route("/start")
def start():
    r = Response("The path is hidden in the headers.")
    r.headers["X-Next"] = "/forest"
    return r

@app.route("/forest")
def forest():
    ua = request.headers.get("User-Agent", "")
    if "Mozilla" in ua:
        return "Next:\n/cave"
    return "Only travelers from Mozilla lands may continue."

@app.route("/cave")
def cave():
    return redirect("/river", code=302)

@app.route("/river")
def river():
    encoded = base64.b64encode(b"/mountain").decode()
    return f"Encoded path:\n{encoded}"

@app.route("/mountain")
def mountain():
    key = request.args.get("key")
    if key == "eagle":
        return "Vault path:\n/vault"
    return "A key is required.\nUse ?key="

@app.route("/secret")
def secret():
    return "gold"

@app.route("/vault")
def vault():
    auth = request.authorization

    if not auth:
        return Response(
            "Authentication required",
            401,
            {"WWW-Authenticate": 'Basic realm="Vault"'}
        )

    if auth.username == "hunter" and auth.password == "gold":
        return "Final endpoint:\n/final"

    return "Wrong credentials", 403

@app.route("/final", methods=["GET", "POST"])
def final():

    if request.method == "GET":
        return """
To claim the treasure:

Send a POST request with:
name=<your_name>
flag=linux_master_2026
"""

    name = request.form.get("name")
    flag = request.form.get("flag")

    if flag != "linux_master_2026":
        return "Wrong flag", 403

    winners.append({
        "name": name,
        "time": datetime.now().isoformat()
    })

    return "Treasure accepted.\nTimestamp recorded."

@app.route("/scoreboard")
def scoreboard():

    output = ""

    for i, w in enumerate(winners, start=1):
        output += f"{i}. {w['name']} - {w['time']}\n"

    return output or "No winners yet."

app.run(host="0.0.0.0", port=8080)
