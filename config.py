from dotenv import load_dotenv
import os

# Find .env file with os variables
load_dotenv()

# retrieve config variables
try:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    BOT_OWNERS = os.getenv('BOT_OWNERS')
    
except (TypeError, ValueError) as ex:
    print("Error while reading config:", ex)
