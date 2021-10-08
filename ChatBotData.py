import random as r
Greetings = ['Good morning, what would you like to do today', 'Welcome back, been a little bit of time, get to work =)', 'Well this is your next big thing right, so get started', 'Good afternoon, this won\x27t be your last time here']
Responses = ['teach', 'test']
LearnedGreetings = ['']
LearnedDefinitions = ['']
initialresponses = Responses[0]
greetingsi = r.randint(0,len(Greetings)-1)