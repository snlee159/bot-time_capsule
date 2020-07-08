import pandas as pd
from .utils import tc_utils as tu
from .utils import slack_utils as su


def run_backup(run_full):
    """
    Collects all pinned messages from public channels from the last day
    and saves them to a Google doc

    :param run_full: Boolean to know whether to pull full look back or not
    :return: prints to a Google document
    """

    yesterday, now = tu.get_time()
    channels = su.get_channels()

    # Initialize df
    pin_df = pd.DataFrame(columns=['channel_id',
                                   'channel_name',
                                   'created_on',
                                   'pinned_by',
                                   'pin_message'])

    i = 0
    for channel in channels:
        # Have the bot join the public channel so that it can read pins
        # in that channel
        su.join_channel(channel)
        pins = su.get_pins(channel)

        for pin in pins:
            if (yesterday <= pin.created_on < now) or run_full:
                pin_df.loc[i] = [pin.channel.channel_id,
                                 pin.channel.name,
                                 pin.created_on,
                                 pin.user.name,
                                 pin.text]
                i += 1

    # Save the new pins to today's csv
    pin_df.to_csv(f"""pin_backup_{(yesterday.replace(' ', '_')
                                            .replace(':', '_')
                                            .replace('-', '_'))}.csv""",
                  index=False)

    return

