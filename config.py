import os
from os import environ

TG_BOT_TOKEN = ""
APP_ID = 29245477
API_HASH = "0abc83883262245c90ca337b7a0375c4"
OWNER_ID = 8226767954
PORT = 8080
DB_URL = ""
DB_NAME = "power"
BOT_USERNAME = "PowerXRobot"
FSUB_PIC = os.environ.get("FSUB_PIC", "https://files.catbox.moe/mattfj.jpg")
START_PIC =os.environ.get("START_PIC", "https://files.catbox.moe/mattfj.jpg")
START_MSG = os.environ.get("START_MSG", "<b><blockquote>Bᴀᴋᴀᴀᴀ...!!!{mention} Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs. I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ʏᴏᴜʀ ғɪʟᴇs ᴇᴀsɪʟʏ ɪɴ ᴀ sᴇᴄᴏɴᴅ...!!</b></blockquote>")
ABOUT_TXT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote>◈ᴀɴɪᴍᴇ : <a href='https://t.me/KafkaX_Bot?start=LTEwMDE0NTczMTMwMjg='>ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ɴᴇᴡs :<a href='https://t.me/Anime_News_Arena'>ᴀɴɪᴍᴇ ɴᴇᴡs</a>\n◈ᴇᴄᴄʜɪ : <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a>\n◈ ᴄʀᴇᴀᴛᴏʀ :<a href=https://t.me/EternalsHelplineBot>ᴏᴡɴᴇʀ</a>\n◈ᴅᴀᴛᴀʙᴀsᴇ :<a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a></blockquote></b>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "⁉️ Hᴇʟʟᴏ {mention} \n<blockquote expandable><b>➪ Iᴀᴍ ᴀ ᴘᴜʙʟɪᴄ ғɪʟᴇ(s) sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇ ғɪʟᴇs ᴀɴᴅ ᴀʟsᴏ I ᴄᴀɴ sᴇɴᴅ ᴛʜᴀᴛ ғɪʟᴇs ɪɴ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ.</blockquote>ʜᴇʟᴘʟɪɴᴇ @EternalsHelplineBot</b>")
TG_BOT_WORKERS = 10000
FSUB_LINK_EXPIRY = 300
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003089960436"))
LOG_FILE_NAME = "links-sharingbot.txt"
SEASON_PATTERN = r'[Ss](\d{1,2})'
EPISODE_PATTERN = r'[Ee][Pp]?(\d{1,3})'
QUALITY_PATTERN = r'(480p|720p|1080p|HDRip|2k|4k)'

TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

SORTING_MODES = {
  'Quality': lambda x: (x['quality_order']),
  'All': lambda x: (x['season'], x['episode'], x['quality_order']),
  'Episode': lambda x: (x['episode']),
  'Season': lambda x: (x['season'])
}
QUALITY_ORDER = {
  '480p': 1,
  '720p': 2,
  '1080p': 3,
  'HDRip': 4,
  '2k': 5,
  '4k': 6,
  'unknown': 7
}
