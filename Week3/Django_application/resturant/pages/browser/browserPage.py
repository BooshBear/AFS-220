from django.shortcuts import render
from ...models import *
from ...api.apihandler import *

def BrowserPage(req):
    cate = categories()
    rand1 = randommeal()
    
    # Objects

    category1 = Category()
    category1.name = cate['categories'][0]["strCategory"]

    category2 = Category()
    category2.name = cate['categories'][1]["strCategory"]

    category3 = Category()
    category3.name = cate['categories'][2]["strCategory"]

    category4 = Category()
    category4.name = cate['categories'][3]["strCategory"]

    category5 = Category()
    category5.name = cate['categories'][4]["strCategory"]

    category6 = Category()
    category6.name = cate['categories'][5]["strCategory"]

    category7 = Category()
    category7.name = cate['categories'][6]["strCategory"]

    category8 = Category()
    category8.name = cate['categories'][7]["strCategory"]

    category9 = Category()
    category9.name = cate['categories'][8]["strCategory"]

    category10 = Category()
    category10.name = cate['categories'][9]["strCategory"]

    category11 = Category()
    category11.name = cate['categories'][10]["strCategory"]

    category12 = Category()
    category12.name = cate['categories'][11]["strCategory"]

    category13 = Category()
    category13.name = cate['categories'][12]["strCategory"]

    # Arrays for objects
    categorys = [category1, category2, category3, category4, 
    category5, category6, category7, category8, category9, category10,
    category11, category12, category13
    ]


    # dic = {
    #     "random1": rand1["meals"][0],
    #     "random1thumbnail": rand1["meals"][0]["strMealThumb"],
    #     "random2": rand2["meals"][0],
    #     "random2thumbnail": rand2["meals"][0]["strMealThumb"],
    #     "random3": rand3["meals"][0],
    #     "random3thumbnail": rand3["meals"][0]["strMealThumb"],
    # }
    
    # Render
    return render(req, 'browserPage.html', {
        "category": categorys,
        "randommeal": rand1,
        })