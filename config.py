import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "MissBroken_Bot")

# Don't Add style font 
BOT_USERNAME2 = getenv("BOT_USERNAME2" , "miss Broken")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

    # Don't edit variables below this line #
SUDO_USERS = [6566179661, 6415940074]

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MXNIHACKER/BrokenMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Team_Hunter_X")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Devils_Hell_0")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))


# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


   
# ██████╗░██████╗░░█████╗░██╗░░██╗███████╗███╗░░██╗
# ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║
# ██████╦╝██████╔╝██║░░██║█████═╝░█████╗░░██╔██╗██║
# ██╔══██╗██╔══██╗██║░░██║██╔═██╗░██╔══╝░░██║╚████║
# ██████╦╝██║░░██║╚█████╔╝██║░╚██╗███████╗██║░╚███║
# ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝
# 
#      ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
#      ████╗░████║██║░░░██║██╔════╝██║██╔══██╗
#      ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
#      ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
#      ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
#      ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░




BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/a199c1adfa09d02786ca7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/0661f62601d0decde581f.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/f1e2fce89f46e84e46207.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
