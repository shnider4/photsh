# By @TroJanzHEX
import os
import shutil

from PIL import Image, ImageOps


async def black_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-black-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "جاري التحميل....", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("جاري معالجة الصورة...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="black")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("لماذا قمت بحذف ذلك؟؟")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("black_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "حدث خطا ما راسل الدعم   @qad3im!", quote=True
                )
            except Exception:
                return


async def green_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-green-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "جاري التحميل....", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("جاري معالجة الصورة...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="green")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("لماذا قمت بحذف ذلك؟؟")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("green_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "حدث خطا ما راسل الدعم   @qad3im!", quote=True
                )
            except Exception:
                return


async def blue_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-blue-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "جاري التحميل....", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("جاري معالجة الصورة...")
            img = Image.open(a)
            height =int (img.height)
            width = int(img.width)
            if height > width :
                y = 0
                x = height - width
                x = x / 2
                x = int(x)
                img_with_border = ImageOps.expand(img, border=(x, y, x, y), fill="white")
                img_with_border.save(edit_img_loc)
                await message.reply_chat_action("upload_photo")
                await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
                await msg.delete()
            elif width > height:
                x = 0
                y=  width - height
                y = y / 2
                y= int(y)
                print(x)
                print(y)
                img_with_border = ImageOps.expand(img, border=(x, y, x, y), fill="white")
                img_with_border.save(edit_img_loc)
                await message.reply_chat_action("upload_photo")
                await message.reply_photo(photo=edit_img_loc, quote=True)
                await msg.delete()
            else:
                await message.reply_text("قياس الصورة مضبوط ✅✅ ")
                await msg.delete()


        else:
            await message.reply_text("لماذا قمت بحذف ذلك؟؟")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("blue_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "حدث خطا ما راسل الدعم   @qad3im!", quote=True
                )
            except Exception:
                return


async def red_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-red-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "جاري التحميل....", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("جاري معالجة الصورة...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="white")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("لماذا قمت بحذف ذلك؟؟")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("red_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "حدث خطا ما راسل الدعم   @qad3im!", quote=True
                )
            except Exception:
                return
