from django.db import models

class Category:
    id: int
    name: str
    desc: str

class Meal:
    id: int
    name: str
    img: str
    desc: str