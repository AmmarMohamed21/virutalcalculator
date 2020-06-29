from sympy import expand,nsimplify
from flask import Flask,render_template,request

app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def Calculate(expr):
    return round(nsimplify(expand(expr)),5)


@app.route("/")
def index():
    if not request.args.get("equation"):
        answer=""
    else:
        equation = request.args.get("equation")
        answer = Calculate(equation)
    return render_template("index.html",answer=answer)


