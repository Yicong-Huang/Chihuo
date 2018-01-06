from app import db


class Restaurant(db.Model):
    __tablename__ = "Restaurants"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    cuisine = db.Column(db.String, nullable=False)
    subcategory = db.Column(db.String, nullable=False)
    tested = db.Column(db.Boolean, nullable=False)
    imageurl = db.Column(db.String)
    phone = db.Column(db.String)

    def __init__(self, id: int, name: str, city: str, rating: float, price: float, cuisine: str, subcategory: str,
                 tested: bool, imageurl: str, phone: str):
        self.id = id
        self.name = name
        self.city = city
        self.rating = rating
        self.price = price
        self.cuisine = cuisine
        self.subcategory = subcategory
        self.tested = tested
        self.imageurl = imageurl
        self.phone = phone
