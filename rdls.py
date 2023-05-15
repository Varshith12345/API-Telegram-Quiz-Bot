import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

# Define your Telegram bot token and Rasa endpoint URL as environment variables
TELEGRAM_TOKEN = os.environ.get('TYPE OR PASTE YOUR TELEGRAM BOT API TOKEN HERE')

# Define the questions and answers
QUESTIONS = {
    "What five letter word becomes shorter when you add two letters to it?": "Short",
    "I shoot but never kill.Who am I?": "Camera",
    "What is the next letter in the  given progression? [W,I,T,N,L,I,T,G,?]": "P",
    "I am a delicious way of representing data.What am I?":"Pie chart",
    "I get smaller everytime I take a bath.What am I?":"Soap",
    "What word in the dictionary is spelled Incorrectly?":"Incorrectly",
    "What can you hold in your right hand, but never in your left hand?":"Right hand glove",
    "Two fathers and two sons are in a car, yet there are only three people in the car.How?":"grandfather,father and son",
    "No matter how little or how much you use me,you change me every month.What am I?":"Calender",
    "What is the value of half of two plus two?":"Three",
    "I have branches ,but no fruits, trunk or leaves .Who am I?":"Bank",
    "What can travel all around the world without leaving its corner?":"Stamp",
    "What type of dress can never be worn?":"Address",
    "The only book which has leaves":"Cheque Book",
    "I have lakes with no water ,mountains with no stone and cities with no buildings .Guess me":"Map",  
    "I have one eye but unable to see.Who am I?":"Needle" ,
    "What kind of room has no doors or windows?":"Mushroom",
}

# Define the current question index
current_question_index=0
count=0
l=list(QUESTIONS.items())
random.shuffle(l)
b=dict(l)
# Create an Updater object to receive Telegram updates
updater = Updater('6073146259:AAGrHCkuoQYF0ZtUuwUJ7aYMI27HYAI65vw')

# Define a command handler for the /start command
def start(update, context):
    global current_question_index
    global count
    global b
    current_question_index = 0
    count=0
    context.bot.send_message(chat_id=update.message.chat_id, text="""HELLO!!👋\nWELCOME TO THE MYSTERIOUS ESCAPE ROOM\nYOUR TARGET IS SIMPLE🎯\nSOLVE THE LEVELS, GET THE CLUES AND CATCH THE REAL KILLER\nSO,LET'S GET STARTED...\nNOTE:\n1)Answer atleast any two questions correctly to proceed to the next level.\n2)⚠️Answers can be in single word or in sentence form.\n3)Ignore the passage if you have answered only one question correctly.""")
    l=list(b.items())
    random.shuffle(l)
    b=dict(l)
    # Get the current question and answer
    current_question = list(b.keys())[current_question_index]
    context.bot.send_message(chat_id=update.message.chat_id, text=current_question)

# Define a message handler to receive text messages from users
def message(update, context):
    global current_question_index
    global count
    current_answer = list(b.values())[current_question_index]
    message=update.message.text
     # Check if the user's message is the correct answer
    if message.lower() == current_answer.lower():
          global count
          count=+2
           # Send a message to congratulate the user on answering correctly
          context.bot.send_message(chat_id=update.message.chat_id, text="Correct!")
        
           # Move to the next question
          current_question_index += 1
      
        
          # Check if we have reached the end of the questions
          if current_question_index == 3:
            if count==2 or count==3:
                context.bot.send_message(chat_id=update.message.chat_id, text="YOU HAVE ANSWERED QUESTIONS CORRECTLY.WELL DONE!!. Mr.Samuel a reputed bussinessman has been murdered and the police have narrowed down the suspects to three people RANI the victim's  wife JOSE the victim's friend and bussiness partner and finally the gardener ARUN.The police have investigated them seperately and their statements have been recorded.These statements will play over the speakers as you solve the puzzles.Listen very carefully because one of them is lying.FIND OUT WHO IS THAT and ESCAPE the Room..GOOD LUCK!!!")
            elif count==1 or count==0:
                context.bot.send_message(chat_id=update.message.chat_id, text="YOU HAVE ANSWERED TWO QUESTIONS INCORRECTLY.BETTER LUCK NEXT TIME...")
          else:
             # Ask the next question
             next_question = list(b.keys())[current_question_index]
             context.bot.send_message(chat_id=update.message.chat_id, text=next_question)
    else:
           # Send a message to inform the user that their answer is incorrect
            context.bot.send_message(chat_id=update.message.chat_id, text="Incorrect!!")
            current_question_index += 1

            if current_question_index == 3:
              if count==2 or count==3:
                context.bot.send_message(chat_id=update.message.chat_id, text="YOU HAVE ANSWERED QUESTIONS CORRECTLY.WELL DONE!!. Mr.Samuel a reputed bussinessman has been murdered and the police have narrowed down the suspects to three people RANI the victim's  wife JOSE the victim's friend and bussiness partner and finally the gardener ARUN.The police have investigated them seperately and their statements have been recorded.These statements will play over the speakers as you solve the puzzles.Listen very carefully because one of them is lying.FIND OUT WHO IS THAT and ESCAPE the Room..GOOD LUCK!!!")
              elif count==1 or count==0:
                context.bot.send_message(chat_id=update.message.chat_id, text="YOU HAVE ANSWERED TWO QUESTIONS INCORRECTLY.BETTER LUCK NEXT TIME...")
            else: 
               next_question = list(b.keys())[current_question_index]
               context.bot.send_message(chat_id=update.message.chat_id, text=next_question)

# Create a command handler and a message handler and add them to the Updater object
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & (~Filters.command), message)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
