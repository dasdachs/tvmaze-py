"""Classes corresponding to the response JSONs"""


# Exports
__all__ = ['Show']

class Show(object):
    def __init__(
        self, id_=0, url="", api_url="", name="",type="",
        language="", genres=[], status="",runtime=0,
        premiered="", schedule={}, rating=0.0, weight=0,
        network={}, webChannel={}, externals={}, image={},
        summary="", updated=0, previous_episode="", next_episode=""
    ):
        """
        The response for show is

        Args:
            id: the TVMaze API ID, int
            url: url to the tv maze page, str
            name: the name of the show,str
            type:
            language:
            genres:
            status:
            runtime:
            premiered:
            schedule:
            rating:
            weight:
            network:
            webChannel:
            externals:
            image:
            summary:
            updated:
            _links:
        """
        self.id_ = id_
        self.url = url
        self.api_url = api_url
        self.name = name
        self.type = type
        self.language = language
        self.genres = genres
        self.status = status
        self.runtime = runtime
        self.premiered = premiered
        self.schedule = schedule
        self.rating = rating
        self.weight = weight
        self.network = network
        self.webChannel = webChannel
        self.externals = externals
        self.image = image
        self.summary = summary
        self.updated = updated
        self._previous_episode = previous_episode
        self._next_episode = next_episode

    @property
    def next_episode(self):
        pass

    @property
    def previous_episode(self):
        pass



class Episode(object):
    def __init__(self):
        """
        id=data["id"],
        url=data["url"],
        api_url=data["_links"]["self"]["href"],
        name=data["name"],
        season=data["season"],
        episode=data["number"],
        airdate=datetime.strptime(data["airdate"], "%Y-%m-%d"),
        # airtime "22:00"
        # airstamp "2017-04-16T22:00:00-04:00"
        runtime=data["runtime"],
        images=[data.get("medium"), data.get("original")],
        summary=data["summary"]
        """
        self.id_ = id_
        self.url = url
        self.api_url = api_url
        self.name = name
        self.season = season
        self.episode = episode # Number
        self.airdate = airdate # Datetime.datetime
        self.airtime = airtime
        self.airstamp = airstamp
        self.runtime = runtime
        self.images = images
        self.summary = summary