import os, json
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils
INDEX = "./pages/index.html"

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@get("/browse")
def browse():
    sectionTemplate = "./templates/browse.tpl"
    result = []
    try:
        for show in utils.AVAILABE_SHOWS:
            article = json.loads(utils.getJsonFromFile(show))
            result.append(article)
        return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=result)
    except Exception as e:
        return repr(e)

run(host='localhost', port=os.environ.get('PORT', 5000), debug=True, reloader=True)
