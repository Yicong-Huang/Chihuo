from flask import render_template, request

from app import app
from app.models import Restaurant


@app.route('/')
def hello_world():
    return render_template('hello.html', name="hello")


@app.route('/dev')
def index():
    RCs = Restaurant.query.all()
    entries = [dict(
        name=r.name,
        imageurl=r.imageurl,
        phone=phone_display(r.phone),
        rating=rating_display(r.rating),
        cuisine=r.cuisine,
        subcategory=r.subcategory
    ) for r in RCs]
    return render_template('index.html', name="develop page", entries=entries)


@app.route('/login', method=['GET', 'POST'])
def login():
    pass

@app.route('/search', methods=['GET', 'POST'])
def search():
    pattern = request.args.get("q")

    RCs = list()
    if pattern:
        RCs.extend(Restaurant.query.filter(Restaurant.name.like("%" + pattern + "%")).all())
        RCs.extend(Restaurant.query.filter(Restaurant.cuisine.like("%" + pattern + "%")).all())
        RCs.extend(Restaurant.query.filter(Restaurant.subcategory.like("%" + pattern + "%")).all())
        RCs.extend(Restaurant.query.filter(Restaurant.city.like("%" + pattern + "%")).all())

        entries = [dict(
            name=r.name,
            imageurl=r.imageurl,
            phone=phone_display(r.phone),
            rating=rating_display(r.rating),
            cuisine=r.cuisine,
            subcategory=r.subcategory
        ) for r in RCs]

    return render_template('index.html', entries=entries)


def phone_display(phone: str) -> str:
    if phone:
        return "(" + phone[:3] + ")-" + phone[3:6] + "-" + phone[6:]
    else:
        return ""


def rating_display(rating: float):
    return {'integer': range(int(rating)), 'decimal': 0 if (rating - int(rating)) < 0.5 else 1,
            'empty': range(5 - int(rating) - (0 if (rating - int(rating)) < 0.5 else 1))}
