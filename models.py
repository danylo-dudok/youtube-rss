from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class YoutubePost:
    url: str
    title: str
    published: datetime


@dataclass
class YoutubeChannel:
    channel_url: str
    title: str
    posts: List[YoutubePost]
