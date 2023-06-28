from db.run_sql import run_sql
from models.city import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities ( name, countries_id ) VALUES ( %s, %s ) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['id'] )
    return city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['id'])
        cities.append(city)
    return cities

def cities_for_countries(country):
    cities = []
    sql = """SELECT cities.*
    FROM cities
    INNER JOIN countries
    ON countries.id = cities.countries_id
    WHERE cities.countries_id = %s"""
    values = [country.id]
    results = run_sql(sql, values)
    for row in results:
        city = City(row["name"], row["id"])
        cities.append(city)
    return cities

def cities_visited(visited):
    cities = []
    sql = """SELECT cities.*
    FROM cities
    INNER JOIN countries
    ON countries.id = cities.countries_id
    WHERE countries.visited is %s"""
    values = [visited]
    results = run_sql(sql, values)
    for row in results:
        country = country_repository.select(row['countries_id'])
        city = City(row["name"], country, row["id"])
        cities.append(city)
    return cities

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)