 
#    License can be found in <https://github.com/lkdevelopers8065/Telegraph-Uploader> 

import os
import telebot
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

bot = telebot.TeleBot("5457677394:AAGjtXl3roSTlENej8EA5Ycjro81XhZ_wyE")

Tgraph = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "https://t.me/lkdevelopers_org/51")

@Tgraph.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("🐋 ⋆ 🐤 `𝙏ʀʏɪɴɢ Ͳᴏ ɖᴏᴡɴʟᴏᴀᴅ` 🐤 ⋆ 🐋")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("✌🍬  `𝑻ʀʏɪɴɢ 𝑻ᴏ 𝑼𝒑𝒍𝒐𝒂𝒅`  ൠ☜")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("🐋 ⋆ 🐤 `𝙏ʀʏɪɴɢ Ͳᴏ ɖᴏᴡɴʟᴏᴀᴅ` 🐤 ⋆ 🐋")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("✌🍬  `𝑻ʀʏɪɴɢ 𝑻ᴏ 𝑼𝒑𝒍𝒐𝒂𝒅`  ൠ☜")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("🐋 ⋆ 🐤 `𝙏ʀʏɪɴɢ Ͳᴏ ɖᴏᴡɴʟᴏᴀᴅ` 🐤 ⋆ 🐋")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("✌🍬  `𝑻ʀʏɪɴɢ 𝑻ᴏ 𝑼𝒑𝒍𝒐𝒂𝒅`  ൠ☜")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@Tgraph.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/lkdevelopers_org'),
        InlineKeyboardButton('Source Code', url='https://github.com/lkdevelopers8065/Telegraph-Uploader')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Hey there,
        
im a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegra.ph
        
Made With Love By @joker_dev</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Tgraph.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/lkdevelopers_org')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""There Is Nothung To KnowMore,
        
Just Send Me A Video/gif/photo Upto 5mb.

i'll upload ut to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Tgraph.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

Tgraph.run()
