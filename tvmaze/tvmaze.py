from datetime import datetime

import requests

from .Items import Show


# Exports
__all__ = ['get', 'get_actor', 'get_episodes', 'get_show', 'get_shows'] 

# Globals
URL =  'http://api.tvmaze.com'
SHOW = '/singlesearch/shows?q='
SHOWS = '/search/shows?q='
EPISODES = '/episodes/'


# Top level wrapper function
def get(name, id=None, show=None, actor=None):
    pass


def get_episodes(name):
    pass

def get_actor(name):
    pass


def get_show(name):
    data = requests.get(URL + SHOW + name)
    if not data.status_code == requests.codes.ok:
        pass  # Some exception
    data = data.json()
    show = _process_response(data)
    return show


def get_shows(name):
    data = requests.get(URL + SHOWS + name)
    if not data.status_code == requests.codes.ok:
        pass # Some exception
    data = data.json()
    shows = []
    for show in data:
        show_object = Show(show)
    return shows


def _process_response(data, type="show"):
    """
    The glue code between the API and the library. It
    cleans the response, uses the correct data types etc.

    Args:
        data:

    Returns:
    """
    if type == "show":
        show = Show(
            id_=data["id"],
            url=data["url"],
            api_url=data["_links"]["self"]["href"],
            name=data["name"],
            type=data["type"],
            language=data["language"],
            genres=data["genres"],
            status=data["status"],
            runtime=data["runtime"],
            premiered=datetime.strptime(data["premiered"], "%Y-%m-%d"),
            schedule=data["schedule"],
            rating=data["rating"]["average"],
            weight=data["weight"],
            network=data["network"],
            webChannel=data["webChannel"],
            externals=data["externals"],
            image=data["image"],
            summary=data["summary"],
            updated=data["updated"],
            previous_episode=data["_links"]["previousepisode"]["href"],
            next_episode=data["_links"]["nextepisode"]["href"],
        )
        return show

    elif type == "episode":
        episode = Episode(
            id = data["id"],
            url = data["url"],
            api_url=data["_links"]["self"]["href"],
            name = data["name"],
            season = data["season"],
            episode = data["number"],
            airdate = datetime.strptime(data["airdate"], "%Y-%m-%d"),
            # airtime "22:00"
            # airstamp "2017-04-16T22:00:00-04:00"
            runtime = data["runtime"],
            images = [data.get("medium"), data.get("original")],
            summary = data["summary"]
        )
        return episode