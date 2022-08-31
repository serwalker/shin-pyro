# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# shin-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from ProjectMan import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from ProjectMan.helpers.misc import git, heroku

MSG_ON = """
☑️ **shin_pyro Berhasil Di Aktifkan.**
━━
-≽ **🤖 Userbot Version -** `{}`
-≽ **Ketik** `.alive` **Untuk Mengecheck Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("kennartt")
            await bot.join_chat("oh_sinnn")
            await bot.join_chat("CilikSupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("shin").info("Memulai shinpyro")
    LOGGER("shin").info(f"Total Clients = {len(bots)} Pengguna")
    install()
    git()
    heroku()
    LOGGER("shin").info(f"shin-pyro v{BOT_VER} ⚙️[⚡ Diaktifkan ⚡]")
    LOOP.run_until_complete(main())
