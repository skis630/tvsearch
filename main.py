import os, json
from bottle import (get, post, redirect, request, route, run, static_file,
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

@get("/ajax/show/<show_id:int>/episode/<episode_id:int>")
def get_episode(show_id, episode_id):
    sectionTemplate = "./templates/episode.tpl"
    episode = utils.getEpisode(show_id, episode_id)
    return template(sectionTemplate, result=episode)

@get("/search")
def get_search_page():
    sectionTemplate = "./templates/search.tpl"
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@post("/search")
def get_search_results():
    sectionTemplate = "./templates/search_result.tpl"
    query = request.forms.get("q")
    shows = utils.getShows()
  
    shows_episodes = [show["_embedded"]["episodes"] for show in shows]
    results = []
    for i in range(len(shows)):
      
        for episode in shows_episodes[i]:
            if episode["name"] is None or episode["summary"] is None:
                print(episode["name"],episode["summary"]) 
            try:
                name = "" if episode["name"] is None else episode["name"]
                summary = "" if episode["summary"] is None else episode["summary"]
                if query in name or query in summary:
                    result = {
                        "showid": shows[i]["id"],
                        "episodeid": episode["id"],
                        "text": shows[i]["name"] + ": " + episode["name"]
                    }
                    results.append(result)
                    print(result)
            except Exception as e:
                print(e)
    print(results)
    
      
   
    return template(INDEX, version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=results, query=query)
  
    


run(host='localhost', port=7000, debug=True, reloader=True)
