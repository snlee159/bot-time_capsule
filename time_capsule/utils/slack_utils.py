import time_capsule.configs as cfg
from time_capsule.common.slack_objs import Channel, Pin
import time_capsule.utils.tc_utils as tu


def get_channels():
    """
    Make a list of channel objects for all public channels in the Slack
    workspace

    :return: a list of Channel Class objects
    """

    channels = []
    response = cfg.slack.conversations.list(exclude_archived=True,
                                            types=['public_channel'])
    channels_json = response.body['channels']
    for channel in channels_json:
        channels.append(Channel(channel['id'],
                                channel['name']))

    return channels


def join_channel(channel):
    """
    Makes the bot join a public channel so that it can read the pins
    in the channel

    :param channel: Channel Class object
    :return: bot joins channel
    """

    cfg.slack.conversations.join(channel=channel.channel_id)

    return


def get_pins(channel):
    """
    Make a list of pin objects in a given public channel

    :param channel: Channel Class object
    :return: a list of Pin Class objects
    """
    channel.get_pins()

    # Initialize a list for User Class objects for avoiding
    # repeat user name lookups
    users = []
    pins = []
    for pin in channel.pins:
        user, users = tu.update_users(users, pin['created_by'])
        date_str = tu.get_date_str(pin['created'])
        pins.append(Pin(channel,
                        user,
                        date_str,
                        pin['message']['text'].replace('\n', ' ')))

    return pins
