from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
import spacy
from chatterbot.storage import StorageAdapter

# Murphy  will be the name of our bot
chatbot = ChatBot("Murphy",
# Storage adapters provide an interface that allows ChatterBot to connect to different storage technologies.
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
# Selects a response to a given input statement.  
    logic_adapters=['chatterbot.logic.BestMatch'],
# It will check if tables are present, if they are not, it will attempt to create the required tables.
    database_uri='sqlite:///database.sqlite3')

"""
This is one example of how to train one phrase
"""
# 
trainer = ChatterBotCorpusTrainer(chatbot)
example = [
    "Good Morning",
    "Good Morning",
]
trainer = ListTrainer(chatbot)
trainer.train(example)