import random
import time

responses = ["It is certain", "It is decidedly so", "Without a doubt",
"Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
"Outlook good", "Yes", "Signs point to yes","Don't count on it", "My reply is no",
"My sources say no", "Outlook not so good", "Very doubtful",
"Reply hazy try again", "Ask again later", "Better not tell you now",
"Cannot predict now", "Concentrate and ask again"]
question = input("Please ask me a Yes/No style question \n")
time.sleep(2)
print(random.choice(responses))
