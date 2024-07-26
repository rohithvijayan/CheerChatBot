import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,Application,ApplicationBuilder,ContextTypes,ConversationHandler
from groq import Groq
import os
import gradientai
from gradientai import Gradient
from gradientai.openapi.client.configuration import Configuration
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()
GRADIENT_WORKSPACE_ID=os.environ["GRADIENT_WORKSPACE_ID"]
GRADIENT_ACCESS_TOKEN=os.environ["GRADIENT_ACCESS_TOKEN"]
gradient=Gradient()
configuration =Configuration(
    access_token = os.environ["GRADIENT_ACCESS_TOKEN"]
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def grad(user_mssg):
    query=user_mssg
    completion = new_model_adapter.complete(query=query, max_generated_token_count=300).generated_output
    print(f"Response:{completion}")
    reply=str(completion)
    audio(reply)
    return reply
def audio(reply):
    tts=gTTS(reply,tld='co.in')
    tts.save("reply.mp3")
async def start(update: Update,context:CallbackContext):
    await update.message.reply_text(" Hey I'm Faith , Your Virtual Friend !\nIf you have any issue or doubts send \help \n Else Lets chat !")
async def help(update: Update,context:CallbackContext):
    await update.message.reply_text("Is there any Issue ?")
async def message_handle(update: Update,context:CallbackContext):
    user_mssg=str(update.message.text)
    print(type(user_mssg))
    bot_mssg=grad(user_mssg)
    
    #await update.message.reply_text(text=bot_mssg)
    with open("reply.mp3","rb+") as reply:
        await update.message.reply_audio(audio=reply,performer="Faith",title="Faith's Reply:")

#def generate_mssg(user_mssg):
    #reply=client.chat.completions.create(messages=[{'role':'user','content':user_mssg}],model="llama3-8b-8192")
    #chat_completion=(reply.choices[0].message.content)
    #return chat_completion

    #query=user_mssg
    #completion=new_model_adapter.complete(query=query,max_generated_token_count=200).generated_output()
    #print(type(completion))
    #print(f"Response:{completion}")
    #return completion


if __name__ == '__main__':
    #base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
    new_model_adapter=gradient.get_model_adapter(model_adapter_id="c0c0b3c8-3c14-487b-852c-52689c8c2e3a_model_adapter")
    print(f"loaded model adapter with id {new_model_adapter.id}")
    application=ApplicationBuilder().token(os.environ.get("TELE_API")).build()
    start_handler = CommandHandler('start', start)
    help_handler=CommandHandler("help",help)
    mssg_handler=MessageHandler(filters.TEXT & (~filters.COMMAND),message_handle)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(mssg_handler)
    application.run_polling()