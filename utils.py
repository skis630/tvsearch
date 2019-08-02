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

def getShow(showId):
    try:
        # if str(id) in utils.AVAILABE_SHOWS:
        show = [show for show in AVAILABE_SHOWS if show == str(showId)]
        show = show[0]
        result = json.loads(getJsonFromFile(show))
        print(result['name'])
        return result
    except Exception as e:
        print(result)
        return repr(e)