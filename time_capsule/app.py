# Imports
import pandas as pd
import slacker
from .utils import google_utils as gu
from .utils import slack_utils as su

def run_backup():
    """
    Collects all pinned messages from the last day and saves them to a
    Google doc.

    :return:
    """

    return