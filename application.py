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

def multiplydivide(n): 
    SSTranslation = str.maketrans("×÷","*/")
    n=n.translate(SSTranslation)
    return n

def Calculate(expr):
    n = len(expr)
    for i in range(n-1):
        if expr[i] == "×" or expr[i] == "÷":
            expr = expr[0:i] + multiplydivide(expr[i]) + expr[i+1:n]
    return round(nsimplify(expand(expr)),5)


@app.route("/")
def index():
    if not request.args.get("equation"):
        answer=""
    else:
        equation = request.args.get("equation")
        try:
            answer = Calculate(equation)
        except:
            answer = "Error"
    return render_template("index.html",answer=answer)


