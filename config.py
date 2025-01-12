# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28188032")

API_HASH = os.environ.get("API_HASH", "f522bb2880eea35d37e205ab46795362")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7891697894:AAEsgZ8BG5oiG3ILdpw3cJg9wUnDkR1qs7o") 

FORCE_SUB = os.environ.get("FORCE_SUB", "renambot01") 

             

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://gameghor4444:fX5nVkbXS3dKwSf9@cluster0.goisu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6867480825, 7613604632').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
