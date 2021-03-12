from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
import spacy
from chatterbot.storage import StorageAdapter
from chatterbot.conversation import Statement


chatbot = ChatBot('Murphy',
    read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 1
        }
    ],
    database_uri='sqlite:///database.sqlite3'
    )

trainer = ListTrainer(chatbot)

trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english")
#trainer.train("./covid.yml")

nlp = spacy.load("en_core_web_sm")

def speak():
    response = chatbot.get_response(user)
    print("BOT: "+str(response))
    return response

def emergency ():
    print("Call 112 or call ahead to your local emergency facility")
    os.system("say -v Samantha Call 112")
    return print(" Ask help")
"""
def guardar (user):
    # The bonus would be to use this function to tell it what I want it to save.
    frase = Statement(user)
    return frase.save()
"""
def warning():
    alert = ["trouble breathing", "persistent pain", "pressure in the chest", "confusion","inhability to wake",
            "pale", "gray", "blue-colored"]
    for x in alert:
        if x in user:
            #guardar(user)
            return emergency()

    return speak()


while True: 
    try:
        user = input(">>> ")
        warning()
    except(KeyboardInterrupt, EOFError, SystemExit): # For interrupt the Bot
        break

