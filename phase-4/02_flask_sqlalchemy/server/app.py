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

if __name__ == "__main__":
    app.run(debug=True, port=5555)