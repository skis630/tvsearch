import os, json
from bottle import (get, post, redirect, error, request, route, run, static_file,
                    template)
import utils
INDEX = "./pages/index.html"
SECTION_TEMPLATE = "./pages/"

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
    result = utils.getShows()
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=result) 

@get("/ajax/show/<id:int>")
def get_show(id):
    sectionTemplate = "./templates/show.tpl"
    result = utils.getShow(id)
    return template(sectionTemplate, result=result)

@get("/show/<id:int>")
def get_show(id):
    sectionTemplate = "./templates/show.tpl"
    result = utils.getShow(id)
    return template(INDEX, version=utils.getVersion() , sectionTemplate=sectionTemplate, sectionData=result)

@get("/ajax/show/<show_id:int>/episode/<episode_id:int>")
def get_episode(show_id, episode_id):
    sectionTemplate = "./templates/episode.tpl"
    episode = utils.getEpisode(show_id, episode_id)
    return template(sectionTemplate, result=episode)

@get("/show/<show_id:int>/episode/<episode_id:int>")
def get_episode(show_id, episode_id):
    sectionTemplate = "./templates/episode.tpl"
    episode = utils.getEpisode(show_id, episode_id)
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=episode)

@get("/search")
def get_search_page():
    sectionTemplate = "./templates/search.tpl"
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@post("/search")
def get_search_results():
    sectionTemplate = "./templates/search_result.tpl"
    query = request.forms.get("q")
    results = utils.searchEpisodes(query)  
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=results, query=query)

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


run(host='localhost', port=7000, debug=True, reloader=True)
