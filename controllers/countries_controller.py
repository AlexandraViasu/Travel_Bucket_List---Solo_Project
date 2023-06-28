from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
countries_blueprint = Blueprint("travelbucketlist", __name__)

@countries_blueprint.route("/travelbucketlist/visited")
def countries_visited():
    countries = country_repository.select_all()

    visited = []
    country_to_cities = {}
    for country in countries:
        if country.visited:
            visited.append(country)
            cities = city_repository.cities_for_countries(country)
            country_to_cities[country.id] = cities
    return render_template("countries/index.html", countries = visited, cities=country_to_cities)

@countries_blueprint.route("/travelbucketlist/notvisited")
def countries_notvisited():
    countries = country_repository.select_all()    
    notvisited = []
    country_to_cities = {}
    for country in countries:
        if country.visited == False:
            notvisited.append(country)
            cities = city_repository.cities_for_countries(country)
            country_to_cities[country.id] = cities
    return render_template("countries/indexNOT.html", countries = notvisited, cities=country_to_cities)

@countries_blueprint.route("/travelbucketlist/visited", methods=['POST'])
def add_new_countries():
    country_name = request.form['name']
    country_rating = request.form['rating']
    country_visited = True
    new_country = Country(country_name, country_rating, country_visited)
    country_repository.save(new_country)
    return redirect("/travelbucketlist/visited")

@countries_blueprint.route("/travelbucketlist/notvisited", methods=['POST'])
def add_new_countries_notvisited():
    country_name = request.form['name']
    country_rating = request.form['rating']
    country_visited = False
    new_country = Country(country_name, country_rating, country_visited)
    country_repository.save(new_country)
    return redirect("/travelbucketlist/notvisited")

@countries_blueprint.route("/travelbucketlist/visited/delete/<id>", methods = ["POST"])
def remove(id):
     country_repository.delete(id)
     return redirect("/travelbucketlist/visited")

@countries_blueprint.route("/travelbucketlist/notvisited/delete/<id>", methods = ["POST"])
def remove_notvisited(id):
     country_repository.delete(id)
     return redirect("/travelbucketlist/notvisited")

@countries_blueprint.route("/travelbucketlist/visited/<id>/edit", methods=['GET'])
def edit_task(id):
    country = country_repository.select(id)
    return render_template("countries/update.html", country = country)

@countries_blueprint.route("/travelbucketlist/notvisited/<id>/edit", methods=['GET'])
def edit_task_notvisited(id):
    country = country_repository.select(id)
    return render_template("countries/updateNOT.html", country = country)

@countries_blueprint.route("/travelbucketlist/visited/<id>", methods=['POST'])
def update_country(id):
    country_name = request.form['name']
    country_rating = request.form['rating']
    country_visited = True
    country_repository.select(id)
    country = Country(country_name, country_rating, country_visited, id)
    country_repository.update(country)
    return redirect("/travelbucketlist/visited")

@countries_blueprint.route("/travelbucketlist/notvisited/<id>", methods=['POST'])
def update_country_notvisited(id):
    country_name = request.form['name']
    country_rating = request.form['rating']
    country_visited = False
    country_repository.select(id)
    country = Country(country_name, country_rating, country_visited, id)
    country_repository.update(country)
    return redirect("/travelbucketlist/notvisited")



