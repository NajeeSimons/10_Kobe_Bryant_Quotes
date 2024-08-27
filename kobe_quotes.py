import random
#QUotes
quotes = [
"Failure doesn't exist.",
"Love what you do & the hard work will pay off.",
"It's the destination, not the journey.",
"Enjoy life.",
"Get over yourself because it's not about you.",
"In order to get to a certain level, you have to have a certain amount of selfishness.",
"People will love you or hate you.",
"Don't do shit you're not passionate about.",
"I see the beauty of getting up in the morning & being in pain.",
]

def get_random_quote():
    return random.choice(quotes)

print(get_random_quote())