import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,Application,ApplicationBuilder,ContextTypes,ConversationHandler
from groq import Groq
import os
import gradientai
from gradientai import Gradient
from gradientai.openapi.client.configuration import Configuration

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
    completion = new_model_adapter.complete(query=query, max_generated_token_count=100).generated_output
    print(f"Response:{completion}")
    reply=str(completion)
    return reply

async def start(update: Update,context:CallbackContext):
    await update.message.reply_text(" Hey I'm Faith , Your Virtual Friend !\nIf you have any issue or doubts send \help \n Else Lets chat !")
async def help(update: Update,context:CallbackContext):
    await update.message.reply_text("Is there any Issue ?")

async def message_handle(update: Update,context:CallbackContext):
    user_mssg=str(update.message.text)
    print(type(user_mssg))
    bot_mssg=grad(user_mssg)

    await update.message.reply_text(text=bot_mssg)

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
    samples=[
    {
        "inputs": "<s>### Instruction:\n: I'm going through some things with my feelings and myself. I barely sleep and I do nothing but think about how I'm worthless and how I shouldn't be here. I've never tried or contemplated suicide. I've always wanted to fix my issues, but I never get around to it. How can I change my feeling of being worthless to everyone?\n\n### Response:\nI first want to let you know that you are not alone in your feelings and there is always someone there to help. You can always change your feelings and change your way of thinking by being open to trying to change. You can always make yourself available to learning new things or volunteering so that you can make a purpose for yourself.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: Lately, I've been feeling very anxious and overwhelmed by my responsibilities. I can't seem to relax and it's affecting my sleep and overall well-being. What can I do to manage my anxiety better?\n\n### Response:\nIt's understandable to feel overwhelmed with responsibilities. One effective method to manage anxiety is to establish a routine that includes self-care activities such as exercise, meditation, and adequate rest. Breaking tasks into smaller, manageable steps can also help reduce the feeling of being overwhelmed. Additionally, talking to a trusted friend or therapist about your feelings can provide emotional support and guidance.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I've been having trouble with my self-esteem. I constantly compare myself to others and feel like I'm not good enough. How can I improve my self-esteem?\n\n### Response:\nImproving self-esteem is a gradual process. Start by recognizing your own strengths and accomplishments, no matter how small they may seem. Practice self-compassion and challenge negative self-talk by replacing it with positive affirmations. Engaging in activities that you enjoy and that make you feel good about yourself can also boost your self-esteem. Remember, everyone has their own unique journey, and comparing yourself to others is not a fair measure of your worth.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: Well, I cheated on my boyfriend and he found out about it. He was damn amazing person. He's becoming an IAS soon. I'm feeling very sad for what I have done.\n\n### Response:\nTough spot to be in. Let's skip the judgment and dig into why this happened. Do you regret your actions, or just the consequences?</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I've been feeling really lonely lately. Even when I'm with friends, I still feel like I'm alone. What can I do to feel more connected?\n\n### Response:\nFeeling lonely even when surrounded by others can be very tough. It's important to seek meaningful connections. Try to open up to close friends or family about how you're feeling. Engaging in activities or groups that interest you can help you meet like-minded people. Sometimes, seeking professional support can provide deeper insights and coping strategies for these feelings.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I'm struggling with balancing work and personal life. I feel like I'm always behind at work, but I'm also missing out on time with my family. How can I find a better balance?\n\n### Response:\nBalancing work and personal life can be challenging. It might help to set clear boundaries between work and personal time. Prioritize your tasks and delegate when possible. Make sure to schedule regular quality time with your family and stick to it. Sometimes, discussing your workload with your employer can lead to adjustments that improve your work-life balance.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I've been feeling very depressed lately and I don't know why. I can't seem to find joy in anything. What should I do?\n\n### Response:\nIt's very brave of you to share this. When dealing with depression, it's important to reach out for support from loved ones or a mental health professional. Sometimes, small steps like engaging in physical activity, maintaining a routine, and setting small goals can make a difference. Therapy or counseling can also help you explore underlying causes and develop coping strategies.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I'm having issues with my body image. I constantly feel like I'm not good enough because of the way I look. How can I develop a healthier body image?\n\n### Response:\nDeveloping a healthier body image takes time and patience. Start by focusing on what your body can do rather than how it looks. Engage in activities that make you feel good physically and mentally. Surround yourself with supportive people who appreciate you for who you are. Limiting exposure to unrealistic media portrayals and practicing self-compassion can also be helpful. Sometimes, speaking with a therapist who specializes in body image issues can provide additional support.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I recently lost a loved one and I'm finding it really hard to cope. I feel overwhelmed with grief. What can I do to start healing?\n\n### Response:\nI'm very sorry for your loss. Grieving is a deeply personal process and there's no right or wrong way to do it. Allow yourself to feel your emotions without judgment. Talking about your loved one and sharing memories can be comforting. Seeking support from friends, family, or a grief counselor can provide you with a safe space to express your feelings. Engaging in self-care and giving yourself time to heal is crucial.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I'm struggling with anger issues. I often find myself getting angry over small things and I don't know how to control it. What should I do?\n: It's good that you're seeking help for your anger issues. Recognizing your triggers and understanding why they provoke such a strong reaction is a good first step. Practice relaxation techniques like deep breathing or meditation to calm yourself in the moment. Developing healthy ways to express your anger, such as through physical activity or creative outlets, can also help. Sometimes, working with a therapist can provide strategies and support for managing anger more effectively.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I'm feeling very insecure in my relationship. I'm always worried that my partner will leave me. How can I overcome these insecurities?\n: Relationship insecurities can be challenging. It's important to communicate your feelings with your partner in an open and honest way. Building trust and understanding through communication can help alleviate some of your fears. Working on your self-esteem and recognizing your worth outside of the relationship can also strengthen your confidence. If these insecurities persist, seeking support from a therapist can provide tools and strategies to work through these feelings.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I feel like I'm stuck in my career and not progressing. It's really frustrating. What can I do to feel more fulfilled professionally?\n: Feeling stuck in your career can be very frustrating. It might help to reassess your career goals and identify what aspects of your job you find most fulfilling. Consider seeking additional training or education to open up new opportunities. Networking with professionals in your field can also provide new perspectives and opportunities. Sometimes, speaking with a career counselor can help you explore different paths and make a plan for moving forward.</s>"
    },
    {
        "inputs": "<s>### Instruction:\n: I recently went through a breakup and I'm having a hard time moving on. I feel like I'll never find happiness again. What should I do?\n: Breakups can be incredibly difficult, and it's normal to feel sad and lost afterward. Allow yourself to grieve the relationship and take the time you need to heal. Focus on self-care and doing things that bring you joy and comfort. Surround yourself with supportive friends and family. Sometimes, reflecting on what you've learned from the relationship can help you grow. If you're finding it particularly hard to move on, talking to a therapist can provide additional support and guidance.</s>"
    }
]
    base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
    new_model_adapter=base_model.create_model_adapter(name="therapist")
    print(f"created model adapter with id {new_model_adapter.id}")
    new_model_adapter.fine_tune(samples=samples)
    print("model fine tuned with dataset")
    application=ApplicationBuilder().token(os.environ.get("TELE_API")).build()
    start_handler = CommandHandler('start', start)
    help_handler=CommandHandler("help",help)
    mssg_handler=MessageHandler(filters.TEXT & (~filters.COMMAND),message_handle)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(mssg_handler)
    application.run_polling()