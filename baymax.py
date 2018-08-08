import  os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot("baymax")
bot.set_trainer(ListTrainer)
while True:
	message = input("you:")
	if message.strip() != "bye":
		reply = bot.get_response(message)
		print("bay:",reply)
	else:
		exit()