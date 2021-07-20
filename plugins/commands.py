# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

#CH force Sbs
update_channel = "-1001152587608"

async def chack(client, message):
    user_id = message.from_user["id"]



    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, user_id)

            if user.status in ["member", "creator", "administrator"]:
                await message.reply_text(" ⚡ ️اهلا بك  في بوت الفوتوشوب  ⚡  \n\n فقط قم بإرسال صورة 🖼 للتعديل عليها ")
                return
        except UserNotParticipant:
            link = link = "t.me/qad3im"
            # await update.reply_text(f"Join @{update_channel} To Use Me")
            await message.reply_text(
                text="**لطفا انضم في القناة حتى تستخدمني  😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="انضمام الان ✅ ", url=link)]
                ])
            )
            return
        except Exception:
            await message.reply_text("حدث خطا ما راسل الدعم  @qad3im ")
            return


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await chack(client, message)
    except Exception:
        pass
