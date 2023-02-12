import requests

def categories():
    res = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php").json()
    return res

def randommeal():
    res = requests.get("https://www.themealdb.com/api/json/v1/1/random.php").json()
    return res

def chosenCategory(category):
    res = requests.get(f"www.themealdb.com/api/json/v1/1/filter.php?c={category}").json
    return res