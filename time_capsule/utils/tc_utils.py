from datetime import datetime as dt
from datetime import timedelta as td
from time_capsule.common.slack_objs import User


def get_time():
    """
    Gets the UTC timestamp string for now and 24 hours earlier

    :return: a String for the current timestamp and a String for 24 hours ago
    """
    yesterday = dt.strftime(dt.utcnow() - td(days=1),
                            "%Y-%m-%d %H:%M:%S")
    now = dt.strftime(dt.utcnow(),
                      "%Y-%m-%d %H:%M:%S")

    return yesterday, now


def update_users(users, user_id):
    """
    Updates a list of User Class objects if the new user_id is not already
    included in this list

    :param users: a list of User Class objects
    :param user_id: a Integer of the user ID
    :return: the User Class object corresponding to the input user_id and
    and updated User Class object list
    """
    if not any(x for x in users if x.user_id == user_id):
        user = User(user_id)
        user.get_name()
        users.append(user)
    else:
        user = [x for x in users if x.user_id == user_id][0]

    return user, users


def get_date_str(unix_ts):
    """
    Converts the pin's unix timestamp to a datetime String

    :param unix_ts: Integer unix timestamp
    :return: String of the pin's created on timestamp
    """
    return dt.utcfromtimestamp(unix_ts).strftime('%Y-%m-%d %H:%M:%S')
