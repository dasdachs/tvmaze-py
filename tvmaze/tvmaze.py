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
    if type == "episode":
        episode = Episode(

            id
            1079686
            url
            "http://www.tvmaze.com/episodes/1079686/girls-6x10-latching"
            name
            "Latching"
            season
            6
            number
            10
            airdate
            "2017-04-16"
            airtime
            "22:00"
            airstamp
            "2017-04-16T22:00:00-04:00"
            runtime
            30
            image
            medium
            "http://static.tvmaze.com/uploads/images/medium_landscape/107/268862.jpg"
            original
            "http://static.tvmaze.com/uploads/images/original_untouched/107/268862.jpg"
            summary
            "<p>Marnie surprises Hannah at her home upstate. Admitting that she doesn't have much going on in her life since her band dissolved, Marnie explains she'd like to help Hannah raise the baby. Hannah accepts the offer.</p>"
            _links
            self
            href
            "http://api.tvmaze.com/episodes/1079686"