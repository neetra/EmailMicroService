from email.policy import HTTP
from flask import Flask, jsonify, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
menuitems = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    print(sse)
    return "Message sent!"





@app.route('/menuItem',methods = ['POST', 'GET'] )
def add_menuItem():
    if(request.method == 'POST'):
        items = request.args.get('item')
        menuitems.append(items)
        sse.publish({"message": items}, type='menuItem')
        print(sse)
        return jsonify({"items" : menuitems})  
    else:
        return jsonify({"items" : menuitems})  