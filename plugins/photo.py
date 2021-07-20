# By @TroJanzHEX
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
#CH force Sbs
update_channel = "-1001152587608"

async def photo(client: Client, message: Message):

    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="حدد الوضع المطلوب من الأسفل!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="تنوير 🌅 ", callback_data="bright"),
                        InlineKeyboardButton(text=" 🎨 MIX الالوان", callback_data="mix"),
                        InlineKeyboardButton(text="تباين 🏞 ", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text=" تحويل الصورة دائرية ⭕️ ", callback_data="circle"),
                        InlineKeyboardButton(text="تحويل الى ملصق 🦁 ", callback_data="stick"),

                    ],
                    [
                        InlineKeyboardButton(text="فلتر ضبابي 🌫  ", callback_data="blur"),
                        InlineKeyboardButton(text="تدوير 🔄 ", callback_data="rotate"),
                        InlineKeyboardButton(text="ابيض & اسود 📽 ", callback_data=" b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="فلتر عتيق 📺 ", callback_data="sepia"),
                        InlineKeyboardButton(text="رسم ✍🏻 ", callback_data="pencil"),
                        InlineKeyboardButton(text="كارتون 🎭 ", callback_data="cartoon"),
                    ],
                    [

                        InlineKeyboardButton(text=" ⚡ GLITCH (گلتش)", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="إزالة الخلفية من الصورة 🔮 ", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="أدوات تنسيق 🎚🎛 ", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="إغلاق ❌ ", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("حدث خطا ما راسل الدعم   @qad3im!", quote=True)
            except Exception:
                return

@Client.on_message(filters.photo & filters.private)
async def start(client: Client, message: Message):

    user_id = message.from_user["id"]


    try:
        user = await client.get_chat_member(update_channel,user_id= user_id)
        print(user.status)

        if user.status in ["member","creator","administrator"]:
           await photo(client, message)
           return
    except UserNotParticipant:
        link = "t.me/qad3im"
            # await update.reply_text(f"Join @{update_channel} To Use Me")
        await message.reply_text(
                text="**لطفا انضم في القناة حتى تستخدمني  😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="انضمام الان 🔥 ", url=link)]
                ])
            )
        return
    except Exception:
        await message.reply_text("حدث خطا ما راسل الدعم  @qad3im ")
        return







