#use this code if the bot has already been trained else use baytrainer
import  os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#name the chatbox as baymax
bot = ChatBot("baymax")
#set up a trainer for baymax
bot.set_trainer(ListTrainer)
#once the bot got trained input the chat and get reply from the bot "bay"
while True:
#if "bye" is typed exit the program else continue getting reply from the chat 
	message = input("you:")
	if message.strip() != "bye":
		reply = bot.get_response(message)
		print("bay:",reply)
	else:
		exit()
