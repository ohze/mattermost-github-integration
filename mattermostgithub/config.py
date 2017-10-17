import os

USERNAME = "Github"
ICON_URL = os.environ.get("MG_ICON_URL")


# compute MATTERMOST_WEBHOOK_URLS dict from `MM_HOOKS` & MM_DOMAIN env variables
# ex, MM_HOOKS = default:1324/off-topic,hook2:4444/channel2
# return {'default': ('chat.ohze.net/hooks/1324', 'off-topic'), 'hook2': ('chat.ohze.net/hooks/4444', 'channel2')}
def get_hooks():
    domain = os.environ.get("MM_DOMAIN")  # ex yourdomain.org

    def slash(s: str):
        kv = s.split("/")
        return domain + "/hooks/" + kv[0], kv[1]

    def colon(s: str):
        kv = s.split(":")
        return kv[0], slash(kv[1])

    hooks = os.environ.get("MM_HOOKS")
    hooks = [kv.strip() for kv in hooks.split(",")]
    return dict(map(colon, hooks))


MATTERMOST_WEBHOOK_URLS = get_hooks()


# compute GITHUB_IGNORE_ACTIONS dict from MM_IGNORE_ACTIONS env variable
# ex, MM_IGNORE_ACTIONS = issues:labeld:assigned,
# return {"issues": ["labeled", "assigned"]}
def get_ignore_actions():
    def colon(s: str):
        l = s.split(":")
        return l[0], l[0:]

    ignore_actions = os.environ.get("MM_IGNORE_ACTIONS")
    ignore_actions = [kv.strip() for kv in ignore_actions.split(",")]
    return dict(map(colon, ignore_actions))


GITHUB_IGNORE_ACTIONS = get_ignore_actions()
SECRET = os.environ.get("MM_SECRET")
SHOW_AVATARS = True
SERVER = {
    'hook': "/",
    'address': "0.0.0.0",
    'port': 5000,
}
