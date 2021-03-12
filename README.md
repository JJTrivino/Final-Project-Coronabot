# Final Project Coronabot
![test](https://cdn.pixabay.com/photo/2017/05/10/19/29/robot-2301646_960_720.jpg)

# Coronabot

## Introduction

This is my final project done during the IronHack Data Analytics bootcamp.

The goal is create a chatbot that contains important information about the Coronavirus, to help prevent and teach the most basic things to beat this virus.

## Tecnology stack 🔨
[Python](https://www.python.org) (Programming language)

[Chatterbot](https://chatterbot.readthedocs.io/en/stable/#) (Machine learning, conversation dialog engine)

[Spacy](https://spacy.io) (Natural Language Processing)

[NLTK](https://www.nltk.org) (Natural Language Toolkit)

[RegEx](https://regexr.com) (Edit the Expression & Text to see matches)

[Pandas](https://pandas.pydata.org) (data analysis and manipulation tool)

## Performance

- For fast data processing, we convert the database to pandas DataFrame.

- I have added some alarm functions so that if the user types the keywords of the worst symptoms of Covid-19, an audible message immediately appears to alert the user to call for help immediately.

- With a RegEx function we can search the database for matches to obtain the desired results. For example we perform a search of the fever degrees to make a small visualization.

- We apply a filter function to apply conditions to the data obtained. For example, for numbers that correspond to fever data, we filter by decimal numbers, which are in a range of more than 35 degrees and less than 45 degrees.

- The questions and answers to the bot are made through an interface, this API has been programmed with HTML and CSS language to have a better design and get a better user experience (similar to a WhatsApp conversation). 

- Different endpoints have been created to be able to connect directly with the Coronabot's brain and see how it stores all the information.

- To show the different endpoints, we connect to the SQLite database and perform different queries

## Endpoints Structure
- *"/" GET method. Is the home page of Coronabot.

- *"/brain"*  displays the entire memory of the Coronabot database.

- *"/Q&A"* shows the questions and answers of the Coronabot.

- *"/text"* shows the Coronabot's answers

- *"/fev"* allows us to see the analysis of the user input, which shows us in days the development of the fever that the user is having.

## Next Steps

- Train a lot, this will allow the Bot to become smarter and smarter and to answer questions that have not been trained.

- Have the API online for example in Heroku, so that several users can be informed and enjoy using a Chatbot in a simple way.

- Create more endpoints that offer more possibilities with the bot, for example if we grant permissions to perform database cleanup from the API.

- Create an app and connect directly to the cell phone.