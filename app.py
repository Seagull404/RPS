from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")
    #return "<p>Hell world</p>"

@app.route("/calclove", methods = ["POST"])
def calclove():
    tmp = (dict(request.form))
    prijatelj = ["jošt", "matic", "aljaž", "voranc", "maks", "nika"]
    ime1 = tmp.get("ime1").lower()
    ime2 = tmp.get("ime2").lower()
    r = f"{ime1} + {ime2} = {random.randint(0, 100)}%"

    if len(ime1) == 0 or len(ime2) == 0:
        r = f"{ime1} + {ime2} = 0%"
    
    elif ime1 == "david" or ime2 == "david":
        r = f"{ime1} + {ime2} = {random.randint(90, 100)}%"

    
    for i in prijatelj:
        if ime1 in prijatelj or ime2 in prijatelj:
            r = f"{ime1} + {ime2} = {random.randint(0, 5)}%"

    return render_template("index.html", rezultat = r)
    # return f"{ime1} + {ime2} = {random.randint(0, 100)}%"
app.run(debug= True)