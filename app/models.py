from app import db


class Headphone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Headphone {self.name}>'
