from bottle import template, static_file
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

def getVersion():
    return "0.0.1"

def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"

def getShows():
    result = []
    try:
        for show in AVAILABE_SHOWS:
            article = json.loads(getJsonFromFile(show))
            result.append(article)
        return result
    except Exception as e:
        return repr(e)

def getShow(showId):
    try:
        show = [show for show in AVAILABE_SHOWS if show == str(showId)]
        show = show[0]
        result = json.loads(getJsonFromFile(show))
        return result
    except Exception as e:
        return repr(e)

def getEpisode(showId, episodeId):
    try:
        show = getShow(showId)
        episodes = show["_embedded"]["episodes"]
        episode = [episode for episode in episodes if episode["id"] == episodeId]
        episode = episode[0]
        return episode
    except Exception as e:
        return repr(e)

def searchEpisodes(query):
    shows = getShows()
    shows_episodes = [show["_embedded"]["episodes"] for show in shows]
    results = []
    for i in range(len(shows)):    
        for episode in shows_episodes[i]:
            try:
                name = episode["name"]
                summary = episode["summary"]
                if query in name or query in summary:
                    result = {
                        "showid": shows[i]["id"],
                        "episodeid": episode["id"],
                        "text": shows[i]["name"] + ": " + episode["name"]
                    }
                    results.append(result)
            except Exception as e:
                print(e)
    return results