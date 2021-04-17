from datetime import datetime
from typing import Iterable, List, Dict

from models import YoutubePost, YoutubeChannel
from settings import RSS_URL_PREFIX
from tools import str_to_date


def read_channels(file_path: str) -> List[str]:
    from tools import deserialize

    with open(file_path, 'r') as channels_file:
        json_str = channels_file.read()
        return deserialize(json_str)


def transform_channel_id_to_rss_url(channel_id: str) -> str:
    return RSS_URL_PREFIX.format(channel_id)


def transform_rss_entry_to_post(entry: Dict) -> YoutubePost:
    return YoutubePost(
        url=entry['link'],
        title=entry['title'],
        published=str_to_date(entry['published']),
    )


def transform_rss_to_channel(feed: Dict, last_check: datetime) -> YoutubeChannel:
    href = feed['feed']['authors'][0]['href']
    title = feed['feed']['title']
    entries = feed['entries']
    posts = []
    for entry in entries:
        post = transform_rss_entry_to_post(entry)
        if post.published > last_check:
            posts.append(post)

    return YoutubeChannel(
        channel_url=href,
        title=title,
        posts=posts,
    )


def get_rss_feed(url: str) -> dict:
    from feedparser import parse
    return parse(url)


def get_channels(ids: List[str], last_check: datetime) -> Iterable[YoutubeChannel]:
    for id in ids:
        url = transform_channel_id_to_rss_url(id)
        feed = get_rss_feed(url)
        channel = transform_rss_to_channel(feed, last_check)
        if channel.posts:
            yield channel
