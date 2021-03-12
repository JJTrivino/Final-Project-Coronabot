from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# Advanced natural language processing
import spacy
# 
import os

# Murphy  will be the name of our bot
chatbot = ChatBot("Murphy",
#To disable the bot to keep storing each question in memory
    read_only= True, 
# Storage adapters provide an interface that allows ChatterBot to connect to different storage technologies.
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
# Selects a response to a given input statement.  
    logic_adapters=['chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            # Each confidence value represents the probability of a response being the correct response to the input.
            'maximum_similarity_threshold': 0.99
        }
    ],
# It will check if tables are present, if they are not, it will attempt to create the required tables.
    database_uri='sqlite:///database.sqlite3')

# For training
trainer = ListTrainer(chatbot)

"""
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

#Train the chatbot based on the english corpus only is necessary one time.
trainer.train("chatterbot.corpus.english")
"""
# Select the language (download previously)(sm = small)
nlp = spacy.load("en_core_web_sm")

"""
# We can export the data to a file json
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.export_for_training("./bot_mongo.json")
"""

def speak ():
    response = chatbot.get_response(user)
    print("BOT: "+str(response))
    return response


# With this function we can search in the memory of the bot for check for example the fever of the user.
"""
def reg (txto):
    patron = "\d{2}[\.\d]*"
    b = [re.findall(patron, i) for i in txto]
    new_list = []
    for i in b:
        try:
            #condición rango numeros
            new_list.append(i[0])
        except:
            pass
    return new_list """
# We filter the results obtained by RegEx and we can add conditions to them.
"""
def filtrado_top(listd):
    numb = [float(i) for i in listd]
    filt = list(filter(lambda n: (n > 35.0) and (n < 45), numb))
    return filt
"""

# The following loop will execute each time the user enters input
while True: 
    try:
        user = input(">>> ")
        speak()
    except(KeyboardInterrupt, EOFError, SystemExit): # For Interrupt the Bot (ctrl + C)
        break