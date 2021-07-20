# By @TroJanzHEX
from image.edit_1 import (  #pylint:disable=import-error
    bright,
    mix,
    black_white,
    g_blur,
    normal_blur,
    box_blur,
)
from image.edit_2 import ( #pylint:disable=import-error
    circle_with_bg,
    circle_without_bg,
    sticker,
    edge_curved,
    contrast,
    sepia_mode,
    pencil,
    cartoon,
)
from image.edit_3 import (  # pylint:disable=import-error
    green_border,
    blue_border,
    black_border,
    red_border,
)
from image.edit_4 import (  # pylint:disable=import-error
    rotate_90,
    rotate_180,
    rotate_270,
    inverted,
    round_sticker,
    removebg_white,
    removebg_plain,
    removebg_sticker,
)
from image.edit_5 import (  # pylint:disable=import-error
    normalglitch_1,
    normalglitch_2,
    normalglitch_3,
    normalglitch_4,
    normalglitch_5,
    scanlineglitch_1,
    scanlineglitch_2,
    scanlineglitch_3,
    scanlineglitch_4,
    scanlineglitch_5,
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "removebg":
        await query.message.edit_text(
            "**اختار نوع الازلة الخلفية 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="مع لون ابيض", callback_data="rmbgwhite"
                        ),
                        InlineKeyboardButton(
                            text="بدون لون ", callback_data="rmbgplain"
                        ),
                    ],
                    [InlineKeyboardButton(text="ملصق", callback_data="rmbgsticker")],
                ]
            ),
        )
    elif query.data == "stick":
        await query.message.edit(
            "**اختر النوع 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="طبيعي ", callback_data="stkr"),
                        InlineKeyboardButton(
                            text="ملصق حواف دائرية 🅰️ ", callback_data="cur_ved"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ملصق دائري ⭕️ ", callback_data="circle_sticker"
                        )
                    ],
                ]
            ),
        )
    elif query.data == "rotate":
        await query.message.edit_text(
            "**اختار درجة الدوران **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="180", callback_data="180"),
                        InlineKeyboardButton(text="90", callback_data="90"),
                    ],
                    [InlineKeyboardButton(text="270", callback_data="270")],
                ]
            ),
        )

    elif query.data == "glitch":
        await query.message.edit_text(
            "**حدد الوضع المطلوب**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="طبيعي", callback_data="normalglitch"
                        ),
                        InlineKeyboardButton(
                            text="خطوط المسح 〰️ ", callback_data="scanlineglitch"
                        ),
                    ]
                ]
            ),
        )
    elif query.data == "normalglitch":
        await query.message.edit_text(
            "**حدد مستوى مقدار تأثير الخلل 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="normalglitch1"),
                        InlineKeyboardButton(text="2", callback_data="normalglitch2"),
                        InlineKeyboardButton(text="3", callback_data="normalglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="normalglitch4"),
                        InlineKeyboardButton(text="5", callback_data="normalglitch5"),
                    ],
                ]
            ),
        )
    elif query.data == "scanlineglitch":
        await query.message.edit_text(
            "**حدد مستوى مقدار تأثير الخلل 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
                        InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
                        InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
                        InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
                    ],
                ]
            ),
        )
    elif query.data == "blur":
        await query.message.edit(
            "**حدد الوضع المطلوب 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="مربع", callback_data="box"),
                        InlineKeyboardButton(text="طبيعي", callback_data="normal"),
                    ],
                    [InlineKeyboardButton(text="ضبابية عالية", callback_data="gas")],
                ]
            ),
        )
    elif query.data == "circle":
        await query.message.edit_text(
            "**حدد الوضع المطلوب 🔰 \n \n  ملاحظة : يفضل ان تكون الصورة مربعة **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="مع خلفية بيضاء⬜️", callback_data="circlewithbg"
                        ),
                        InlineKeyboardButton(
                            text="بدون خلفية", callback_data="circlewithoutbg"
                        ),
                    ]
                ]
            ),
        )
    elif query.data == "border":
        await query.message.edit(
            "**حدد الوضع المطلوب 🔰 **",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="⬜️ مربع ابيض ⬜️ ", callback_data="red"),
                        InlineKeyboardButton(text="🟩 مربع اخضر 🟩", callback_data="green"),
                    ],
                    [
                        InlineKeyboardButton(text="⬛️ مربع اسود ⬛️", callback_data="black"),
                        InlineKeyboardButton(text="♻️ منشور انستا ♻️", callback_data="blue"),
                    ],
                ]
            ),
        )
    if query.data not in [
        "removebg",
        "stick",
        "rotate",
        "start_data",
        "help_data",
        "about_data",
        "glitch",
        "normalglitch",
        "scanlineglitch",
        "blur",
        "circle",
        "border",
    ]:
        await query.message.delete()
        if query.data == "bright":
            await bright(client, query.message)

        elif query.data == "mix":
            await mix(client, query.message)

        elif query.data == "b|w":
            await black_white(client, query.message)

        elif query.data == "circlewithbg":
            await circle_with_bg(client, query.message)

        elif query.data == "circlewithoutbg":
            await circle_without_bg(client, query.message)

        elif query.data == "green":
            await green_border(client, query.message)

        elif query.data == "blue":
            await blue_border(client, query.message)

        elif query.data == "red":
            await red_border(client, query.message)

        elif query.data == "black":
            await black_border(client, query.message)


        elif query.data == "circle_sticker":
            await round_sticker(client, query.message)

        elif query.data == "inverted":
            await inverted(client, query.message)

        elif query.data == "stkr":
            await sticker(client, query.message)

        elif query.data == "cur_ved":
            await edge_curved(client, query.message)

        elif query.data == "90":
            await rotate_90(client, query.message)

        elif query.data == "180":
            await rotate_180(client, query.message)

        elif query.data == "270":
            await rotate_270(client, query.message)

        elif query.data == "contrast":
            await contrast(client, query.message)

        elif query.data == "box":
            await box_blur(client, query.message)

        elif query.data == "gas":
            await g_blur(client, query.message)

        elif query.data == "normal":
            await normal_blur(client, query.message)

        elif query.data == "sepia":
            await sepia_mode(client, query.message)

        elif query.data == "pencil":
            await pencil(client, query.message)

        elif query.data == "cartoon":
            await cartoon(client, query.message)

        elif query.data == "normalglitch1":
            await normalglitch_1(client, query.message)

        elif query.data == "normalglitch2":
            await normalglitch_2(client, query.message)

        elif query.data == "normalglitch3":
            await normalglitch_3(client, query.message)

        elif query.data == "normalglitch4":
            await normalglitch_4(client, query.message)

        elif query.data == "normalglitch5":
            await normalglitch_5(client, query.message)

        elif query.data == "scanlineglitch1":
            await scanlineglitch_1(client, query.message)

        elif query.data == "scanlineglitch2":
            await scanlineglitch_2(client, query.message)

        elif query.data == "scanlineglitch3":
            await scanlineglitch_3(client, query.message)

        elif query.data == "scanlineglitch4":
            await scanlineglitch_4(client, query.message)

        elif query.data == "scanlineglitch5":
            await scanlineglitch_5(client, query.message)

        elif query.data == "rmbgwhite":
            await removebg_white(client, query.message)

        elif query.data == "rmbgplain":
            await removebg_plain(client, query.message)

        elif query.data == "rmbgsticker":
            await removebg_sticker(client, query.message)
