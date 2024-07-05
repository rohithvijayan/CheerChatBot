import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,Application,ApplicationBuilder,ContextTypes,ConversationHandler
from groq import Groq
import os
client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update,context:CallbackContext):
    await update.message.reply_text(" Hey I'm Faith , Your Virtual Friend !\nIf you have any issue or doubts send \help \n Else Lets chat !")
async def help(update: Update,context:CallbackContext):
    await update.message.reply_text("Is there any Issue ?")

async def message_handle(update: Update,context:CallbackContext):
    user_mssg=update.message.text
    print(type(user_mssg))
    response=generate_mssg(user_mssg)
    await update.message.reply_text(response)

def generate_mssg(user_mssg):
    reply=client.chat.completions.create(messages=[{'role':'user','content':user_mssg}],model="llama3-8b-8192")

    chat_completion=(reply.choices[0].message.content)
    return chat_completion

if __name__ == '__main__':
    application=ApplicationBuilder().token(os.environ.get("TELE_API")).build()
    start_handler = CommandHandler('start', start)
    help_handler=CommandHandler("help",help)
    mssg_handler=MessageHandler(filters.TEXT & (~filters.COMMAND),message_handle)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(mssg_handler)
    application.run_polling()