import time_capsule.configs as cfg


class Channel:
    """
    An object to represent a public channel in the slack workspace

    Attributes:
        channel_id: the ID associated with a given public channel
        name: the public channel's display name
        pins: a JSON object of the pins within a public channel
    """

    def __init__(self, channel_id, name):
        self.channel_id = channel_id
        self.name = name
        self.pins = {}

    def get_pins(self):
        """Find the pins within a given channel"""
        self.pins = (cfg.slack
                        .pins
                        .list(channel=self.channel_id)
                        .body['items'])


class User:
    """
    An object to represent a user in the slack workspace

    Attributes:
        user_id: the ID associated with a given user
        name: the user's display name
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.name = ""

    def get_name(self):
        """Get the user's display name"""
        self.name = (cfg.slack
                        .users
                        .info(user=self.user_id)
                        .body['user']['real_name'])


class Pin:
    """
    An object to represent a pin within the slack workspace

    Attributes:
        channel: the channel object associated with a pin
        user: the user object associated with a pin
        created_on: the timestamp String when the pin was posted
        text: the text content of the pin
    """
    def __init__(self, channel, user, created_on, text):
        self.channel = channel
        self.user = user
        self.created_on = created_on
        self.text = text
