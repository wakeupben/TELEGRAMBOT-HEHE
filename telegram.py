
TOKEN='XXXXXX'
BOT_USERNAME='XXXX'

#I KNOW I LEFT MY API KEYS XD
import requests
import telebot
import google.generativeai as genai

bot= telebot.TeleBot(TOKEN)

GOOGLE_API_KEY=('XXXX')
genai.configure(api_key=GOOGLE_API_KEY)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "balls balls faiz balls")

    
@bot.message_handler(commands=['verse_of_the_day'])
def verse(message):

    url = "https://beta.ourmanna.com/api/v1/get"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers).text

    bot.reply_to(message, response)
    
model = genai.GenerativeModel('gemini-1.0-pro-latest')
chat = model.start_chat(history=[])

@bot.message_handler(commands=['chat'])
def prompt(message):

        response="hi im faiz's wife do ask me anything.(exit)"
        bot.send_message(message.chat.id,response,parse_mode="Markdown")
        bot.register_next_step_handler(message,res)  
def res(message):

    print(message.text)
    if message.text == "exit":
        bot.reply_to(message,"byebye")
    else:
        response=chat.send_message(message.text, stream=True)
        for chunk in response:
                if chunk.text:
                    bot.send_message(message.chat.id,chunk.text,parse_mode="Markdown")
                    print(chunk.text)
        bot.register_next_step_handler(message,res)
        

        
        
        
        


    



# @bot.message_handler(commands=['goon_sesh'])
# def goon(message):






# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
 


bot.infinity_polling()
