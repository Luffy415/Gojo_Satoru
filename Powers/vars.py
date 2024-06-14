from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID",default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default="-1001978176529"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="mongodb+srv://Zen:Zen@groupnavigator.tmv4lcx.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="Zen")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="QuirkySquad")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="ZenBotX")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "GroupNavigatorBot"
    BOT_ID = ""
    BOT_NAME = "𝘎𝘳𝘰𝘶𝘱 𝘕𝘢𝘷𝘪𝘨𝘢𝘵𝘰𝘳"
    owner_username = "SyncZen"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6513948062:AAGjiuULDk9djlFlC0SuG2-lMgSKWfq2bJc"
    API_ID = 27169529  # Your APP_ID from Telegram
    AuDD_API = None
    API_HASH = "5d67602a4e0bbfabe669c0febeaf63b6"  # Your APP_HASH from Telegram
    OWNER_ID = 6542673293  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001978176529  # Your Private Group ID for logs
    DEV_USERS = [6758178852]
    SUDO_USERS = [6758178852]
    WHITELIST_USERS = [6758178852]
    DB_URI = "mongodb+srv://madharchod:Hijda@madharchod.bkufl86.mongodb.net/?retryWrites=true&w=majority&appName=Madharchod"  # Your mongo DB URI
    DB_NAME = "GojoSatoru"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "TheGenChat"
    SUPPORT_CHANNEL = "TheGenNetwork"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
