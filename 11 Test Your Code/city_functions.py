#coding=utf-8

def formatted_city(city, country, population = ""):
    if population:
        result = city + ", " + country + " - population " + str(population)
    else:
        result = city + ", " + country
    return result