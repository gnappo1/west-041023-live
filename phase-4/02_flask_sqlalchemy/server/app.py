from flask import (
    Flask,
    request,
    g,
    session,
    json,
    jsonify,
    abort,
    render_template,
    redirect,
    url_for,
    make_response,
)
from flask_migrate import Migrate
from models import db, Production, CrewMember
import os
from time import time
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "theater.db"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)
# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = 'BAD_SECRET_KEY'

@app.before_request
def before_request():
    # look into g using pop, get, __dict__
    g.request_start_time = time()
    session["user_id"]= 1 if "user_id" not in session else session["user_id"]
    # import ipdb; ipdb.set_trace()

@app.after_request
def after_request(response):
    response.headers["X-Request-Time"] = str(time() - g.request_start_time)
    return response

@app.teardown_request
def teardown_request(exception):
    print("teardown_request")

@app.route("/")
def root():
    return "<h1>Welcome to the Theater!</h1>"


@app.route("/productions", methods=["GET", "POST"])
def get_productions():
    if request.method == "GET":
        productions = Production.query.all()
        serialized_productions = [p.to_dict() for p in productions]
        return serialized_productions, 200 #invokes jsonify automatically for lists or dicts
        # return json.dumps(serialized_productions), 200  #explicitly invokes json.dumps
        # return jsonify(serialized_productions), 200 #explicitly invokes jsonify
        # return make_response(jsonify(serialized_productions), 200) #use the flexible make_response to set headers
        # return render_template("productions.html", productions=serialized_productions), 200 #use the flexible make_response to set headers
    else:
        try:
            title = request.form.get("title")
            genre = request.form.get("genre")
            director = request.form.get("director")
            description = request.form.get("description")
            budget = request.form.get("budget")
            image = request.form.get("image")
            ongoing = request.form.get("ongoing")
            prod = Production(title=title, genre=genre, director=director, description=description, budget=budget, image=image, ongoing=ongoing)
            db.session.add(prod)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
@app.route("/crew_members", methods=["GET"])
def get_crew_members():
    crew_members = CrewMember.query.all()
    serialized_crew_members = [c.to_dict() for c in crew_members]
    return jsonify(serialized_crew_members)


@app.route("/productions", methods=["POST"])
def create_production():
    data = request.get_json()
    production = Production(title=data["title"], director=data["director"])
    db.session.add(production)
    db.session.commit()
    return jsonify(production.to_dict()), 201


@app.route("/crew_members", methods=["POST"])
def create_crew_member():
    data = request.get_json()
    production_id = data["production_id"]
    production = Production.query.get(production_id)
    if not production:
        return jsonify({"error": "Production not found."}), 404
    crew_member = CrewMember(
        name=data["name"], position=data["position"], production=production
    )
    db.session.add(crew_member)
    db.session.commit()
    return jsonify(crew_member.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True, port=5555)
