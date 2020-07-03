# Imports
from slacker import Slacker
from .utils import google_utils as gu
from .utils import slack_utils as su

def run_backup():
    """
    Collects all pinned messages from the last day and saves them to a
    Google doc.

    :return: prints to a Google document
    """

    # Get channels
    # For each channel, pull pins from the last day
    # Write pins to a google doc for the last day

    return