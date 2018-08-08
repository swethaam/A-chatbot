#import the chatterbot  
import  os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#name the chatterbot as "baymax"
bot = ChatBot("baymax")
#set the trainer to "baymax"
bot.set_trainer(ListTrainer)
#loop through all the files which are needed to train the bot
for each in os.listdir("C:/Users/white/Downloads/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english"):
	data = open("C:/Users/white/Downloads/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english/"+each,"r").readlines()
	#train the bot
	bot.train(data)
	#once bot got trained completely enter input and get reply from the bot
while True:
	message = input("you:")
	#if user input is "bye" exit the chat else continue the chat
	if message.strip() != "bye":
		reply = bot.get_response(message)
		print("bay:",reply)
	else:
		exit()
