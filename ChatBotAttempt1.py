"""run this in console
import os
import importlib
import sys
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#the blanks are intentional. if it fails just paste it again.
def runtest():
    os.system('python ChatBotAttempt1.py')

cls()
#after this run runtest() to use the program
runtest()
"""
import time
import threading
import importlib
import string
#Importing premade elements for initial conversation.
import ChatBotData as CBD
#Preparing a clear console command.
import os
import sys
#Reload ChatBotData
importlib.reload(CBD)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()
#making it easier to create inputs
def ci(addwrd : str = ''):
    ci.tempinput = None
    addwrd = str(addwrd)
    try:
        ci.tempinput = input(addwrd +': ')
        ci.tempinput = ci.tempinput.lower()
        #print(ci.tempinput)
    except ValueError:
        print('Wasn\'t understood, perhaps I heard incorrectly.')
def f():
    ci.tempinput = None
    f.i = ''
    clear()
    #testing stopping a thread
    while (f.i != '100'):
        if (ci.tempinput == None):
            clear()
            print('This is a test.')
            ci('Input 100 to complete')
            f.i = ci.tempinput
        else:
            ci.tempinput = None
        #if keyboard.read_key() == '1':
            #time.sleep(1)
        time.sleep(0.15)
ci(CBD.Greetings[CBD.greetingsi])
#testing a way to save words
if (ci.tempinput.split(' ')[0] == str(CBD.initialresponses[0])):
    print('Ready to be taught.')
    ci("Input a new word")

ci("Input")
#testing threading
if(ci.tempinput == 'testingtime'):
    thread = threading.Thread(target=f)
    thread.start()
#remove everything, but the commas from a list
templist = str(str(str(str(str(CBD.Responses[0]).replace(']','')).replace('[','')).replace("'",'')).replace(' ','')).replace(',',' ')
print(templist)
print(str(len(CBD.Responses)))
#add a str to another python files list
with open('ChatBotData.py', 'r') as _CBD:
    CBDread = _CBD.read()
with open('ChatBotData.py', 'w') as _CBD:
    #print(CBDread)
    _CBD.write(CBDread)
    #len(CBDread.split('\n'))
    for x in range(1,len(CBDread.split('\n'))+1):
        if CBDread.split('\n')[x-1].split(' ')[0] == 'LearnedGreetings':
            print(CBDread.split('\n')[x-1])
            #print(CBDread.split('\n')[x-1].split(' ')[0])
        #print(CBDread.split('\n')[x-1])
    pass