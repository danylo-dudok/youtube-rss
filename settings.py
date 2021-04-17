from datetime import datetime, timedelta
from typing import final

from tools import localize_time

RSS_URL_PREFIX: final = 'https://www.youtube.com/feeds/videos.xml?channel_id={0}'
LOCATION_ARGUMENT_PREFIX: final = '--location='
CHANNEL_ARGUMENT_PREFIX: final = '--channels='
LAST_CHECK_ARGUMENT_PREFIX: final = '--last-check='
TWO_WEEKS_IN_DAYS: final = 14
DEFAULT_LAST_CHECK: final = localize_time(datetime.now() - timedelta(days=TWO_WEEKS_IN_DAYS))
EMPTY: final = ''
CHANNEL_POSTS_LIMIT: final = 20
