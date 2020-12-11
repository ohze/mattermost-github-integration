import os

USERNAME = "Github"
ICON_URL = os.environ.get("MG_ICON_URL")

# Repository settings
MATTERMOST_WEBHOOK_URLS = {
    'default' : (os.environ.get("MM_DOMAIN"), os.environ.get("CHANNEL")),
}

# Ignore specified event actions
GITHUB_IGNORE_ACTIONS = ""

# Ignore events from specified users
IGNORE_USERS = ""

# Redirect events to different channels
REDIRECT_EVENTS = ""
SECRET = ""
SHOW_AVATARS = True
SERVER = {
    'hook': "/",
    'address': "0.0.0.0",
    'port': 5000,
}
