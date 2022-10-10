from flask import Flask, jsonify
from functions import getEczane

app = Flask(__name__)

@app.route("/")
def index():
    return """
SiberAtay Nöbetçi Eczaneler Api<br><br>
#Author : Nemesis<br><br>
 --- SiberAtay ---
"""

@app.route("/eczaneler/<string:il>")
def eczaneler(il : str = ...):
    return jsonify({
        "il":il,
        "eczaneler":getEczane(il=il),
        

    })


if __name__ == "__main__":
    app.run(debug=True)