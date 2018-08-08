import  os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("baymax")
bot.set_trainer(ListTrainer)
for each in os.listdir("C:/Users/white/Downloads/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english"):
	data = open("C:/Users/white/Downloads/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english/"+each,"r").readlines()
	bot.train(data)
while True:
	message = input("you:")
	if message.strip() != "bye":
		reply = bot.get_response(message)
		print("bay:",reply)
	else:
		exit()
