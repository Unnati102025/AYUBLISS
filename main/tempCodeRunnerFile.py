class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    address = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    pastcondition = db.Column(db.String(80), nullable=False)
