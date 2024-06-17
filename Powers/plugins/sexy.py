import random

from telethon import Button, events

from .. import tbot as asst

BUTTON = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/ZenBotX")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"
BEAUTIFULL = "https://telegra.ph/file/37f85c796e49b0cc0e232.gif"
HANDCY = "https://telegra.ph/file/fbbc734152df5411efc7c.gif"
SIGMA = 'https://te.legra.ph/file/d62dc5ac7150f8d5a3d96.mp4'
LOYAL = 'https://te.legra.ph/file/e31be3e34c9a91a8c39b2.mp4'


@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNY = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ!**"
    await e.reply(HORNY, buttons=BUTTON, file=HOT)


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**🍷** {mention} **ɪꜱ** {mm}**% ɢᴀʏ!**"
    await e.reply(GAY, buttons=BUTTON, file=SMEXY)


@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    FEK = f"**💜** {mention} **ɪꜱ** {mm}**% ʟᴇᴢʙɪᴀɴ!**"
    await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)


@asst.on(events.NewMessage(pattern="/boob ?(.*)"))
async def boob(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"**🍒** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}**!**"
    await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"**🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ**"
    await e.reply(COCK, buttons=BUTTON, file=LANG)


@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍑** {mention} {mm}**% ᴄᴜᴛᴇ**"
    await e.reply(CUTE, buttons=BUTTON, file=CUTIE)


@asst.on(events.NewMessage(pattern="/beautiful ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BEAUTIFUL = f"**🤩** {mention} {mm}**% ʙᴇᴀᴜᴛɪғᴜʟ**"
    await e.reply(BEAUTIFUL, buttons=BUTTON, file=BEAUTIFULL)

@asst.on(events.NewMessage(pattern="/handsome ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HANDSOME = f"**ʜᴇʏ ʏᴏᴜ 💌** {mention} {mm}**% ʜᴀɴᴅsᴏᴍᴇ**"
    await e.reply(HANDSOME, buttons=BUTTON, file=HANDCY)

@asst.on(events.NewMessage(pattern="/sigma ?(.*)"))
async def sigma(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    FEK = f"**🗿** {mention} **ɪꜱ** {mm}**% sɪɢᴍᴀ!**"
    await e.reply(SIGMA, buttons=BUTTON, file=SIGMA)

@asst.on(events.NewMessage(pattern="/loyal ?(.*)"))
async def loyal(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**🍷** {mention} **ɪꜱ** {mm}**% ʟᴏʏᴀʟ!**"
    await e.reply(LOYAL, buttons=BUTTON, file=LOYAL)


__help__ = """
➻ /horny - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʜᴏʀɴʏᴇꜱꜱ.

➻ /gay - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢᴜʏɴᴇꜱꜱ.

➻ /lezbian - ᴄʜᴇᴄᴋ ᴜʀ ᴄᴜʀʀᴇɴᴛ ʟᴀᴢʙɪᴀɴ.

➻ /boob - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʙᴏᴏʙꜱ ꜱɪᴢᴇ.

➻ /cute - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴜᴛᴇɴᴇꜱꜱ.

➻ /sigma - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴜᴄʜ sɪɢᴍᴀ ʏᴏᴜ'ʀᴇ.

➻ /beautiful - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʙᴇᴀᴜᴛʏ.

➻ /handsome - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴜᴄʜ ʜᴀɴᴅsᴏᴍᴇ ʏᴏᴜ'ʀᴇ.

➻ /loyal - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʟᴏʏᴀʟɪᴛʏ.
"""

__mod_name__ = "Sᴇᴍxʏ"
