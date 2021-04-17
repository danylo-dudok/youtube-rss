from typing import List

from rss import read_channels, get_channels
from settings import CHANNEL_ARGUMENT_PREFIX, LAST_CHECK_ARGUMENT_PREFIX, DEFAULT_LAST_CHECK, LOCATION_ARGUMENT_PREFIX
from tools import str_to_date, serialize, read_argument
import dataclasses


def main(arguments: List[str]):
    channel_ids = read_argument(arguments, CHANNEL_ARGUMENT_PREFIX)
    channels_file_path = read_argument(arguments, LOCATION_ARGUMENT_PREFIX)
    if not channels_file_path and not channel_ids:
        raise Exception('Invalid input arguments')

    ids = channel_ids.replace(' ', '').replace('[', '').replace(']', '').split(',')\
        if channel_ids else read_channels(channels_file_path)
    last_check = read_argument(arguments, LAST_CHECK_ARGUMENT_PREFIX)
    last_check = str_to_date(last_check) if last_check else DEFAULT_LAST_CHECK
    channels = get_channels(ids, last_check)

    posts_count = 0
    dict_channels = []
    for channel in channels:
        dict_channels.append(dataclasses.asdict(channel))
        posts_count += len(channel.posts)

    print(serialize({
        'amount': posts_count,
        'channels': dict_channels,
    }))


if __name__ == '__main__':
    from sys import argv
    main(argv)
