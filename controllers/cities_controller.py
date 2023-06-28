from flask import Blueprint, Flask, render_template, request, redirect
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
cities_blueprint = Blueprint("visited/cities", __name__)

@cities_blueprint.route("/travelbucketlist/visited/cities")
def visited_cities():
    countries = country_repository.select_all()
    cities = city_repository.cities_visited(True)
    return render_template("cities/index.html", cities = cities, countries = countries)

@cities_blueprint.route("/travelbucketlist/notvisited/cities")
def view_cities_notvisited():
    countries = country_repository.select_all()
    notvisited = city_repository.cities_visited(False)
    return render_template("cities/indexNOT.html", cities = notvisited, countries = countries)

@cities_blueprint.route("/travelbucketlist/visited/cities", methods=['POST'])
def add_new_cities():
    city_name = request.form['name']
    city_country = request.form['country']
    country = country_repository.select(city_country)
    new_city = City(city_name, country)
    city_repository.save(new_city)
    return redirect("/travelbucketlist/visited/cities")

@cities_blueprint.route("/travelbucketlist/notvisited/cities", methods=['POST'])
def add_new_cities_notvisited():
    city_name = request.form['name']
    city_country = request.form['country']
    country = country_repository.select(city_country)
    new_city = City(city_name, country)
    city_repository.save(new_city)
    return redirect("/travelbucketlist/visited/cities")

@cities_blueprint.route("/travelbucketlist/visited/cities/delete/<id>", methods = ["POST"])
def remove(id):
     city_repository.delete(id)
     return redirect("/travelbucketlist/visited/cities")

@cities_blueprint.route("/travelbucketlist/notvisited/cities/delete/<id>", methods = ["POST"])
def remove_notvisited(id):
     city_repository.delete(id)
     return redirect("/travelbucketlist/notvisited/cities")
