from flask import (
    Flask,
    request,
    g,
    session,
    json,
    jsonify,
    render_template,
    make_response,
    url_for,
    redirect
)

from flask_migrate import Migrate
from models import db, Production, CrewMember
from time import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def welcome():
    return "<h1>Welcome to our Theater!</h1>"

@app.route("/productions", methods=["GET", "POST"])
def productions():
    if request.method == "GET":
        # first retrieve from the db all my produtions
        # format them in a way that allows us to send them in JSON format
        # import ipdb; ipdb.set_trace()
        productions = [p.as_dict() for p in Production.query.all()]
        # return json.dumps(productions), 200
        # return jsonify(productions), 200
        return make_response(jsonify(productions), 200)
    else:
        title = request.json.get('title')
        genre = request.json.get('genre')
        director = request.json.get('director')
        budget = request.json.get('budget')
        image = request.json.get('image')
        ongoing = request.json.get('ongoing')
        description = request.json.get('description')
        
        try:
            prod = Production(title=title, genre=genre, director=director, budget=budget, image=image, ongoing=ongoing, description=description)
            db.session.add(prod)
            db.session.commit()
            return prod.as_dict(), 201
        
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

@app.route("/productions/<int:id>", methods=["GET"])
def production_by_id(id):
    if prod := Production.query.get(id):
        # return make_response(prod, 200)
        return render_template("production.html", prod=prod)
    else:
        return jsonify({"error": "Not found"}), 404
    
# 17.✅ Request Hooks
# @app.before_request: runs a function before each request.
# @app.before_first_request: runs a function before the first request (but not subsequent requests).
# @app.after_request: runs a function after each request.
# @app.teardown_request: runs a function after each request, even if an error has occurred.
# Functions marked with before_request() are called before a request and passed no arguments. Functions marked with after_request() are called after a request and passed the response that will be sent to the client. They have to return that response object or a different one. They are however not guaranteed to be executed if an exception is raised, this is where functions marked with teardown_request() come in. They get called after the response has been constructed. They are not allowed to modify the request, and their return values are ignored. If an exception occurred while the request was being processed, it is passed to each function; otherwise, None is passed in.
@app.before_request
def before_request():
    g.time = time()

@app.after_request
def after_request(response):
    diff = time() - g.time
    print(f"Request took {diff} seconds")
    response.headers["X-Response-Time"] = str(diff)
    return response

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.session.close()
        
if __name__ == "__main__":
    app.run(debug=True, port=5555)