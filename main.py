"""run this in console
import os
import importlib
import sys
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#the blanks are intentional. if it fails just paste it again.
def runtest():
    os.system('python main.py')

cls()
#after this run runtest() to use the program
runtest()
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
if __name__ == '__main__':
    pass
import os
import importlib
import sys
import ChatBotData as CBD
importlib.reload(CBD)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()
#X is the word added to LearnedGreetings
X = "helloworld"
with open('ChatBotData.py', 'r') as _CBD:
    CBDread = _CBD.read()
    #print(CBDread.split("\n")[1])
for x in range(1,len(CBDread.split('\n'))+1):
        if CBDread.split('\n')[x-1].split(' ')[0] == 'LearnedGreetings':
            CorrectLine = CBDread.split('\n')[x-1]
            Learned = CBD.LearnedGreetings
            Learned.append(X)
            NewLine = CBDread.split('\n')[x-1].split(' ')[0] + ' = ' + str(Learned)
            print(NewLine)
TestStr = "LearnedGreetings"
Test = CBDread.replace(CorrectLine, NewLine)
print(Test)
#To update the Storage File, unhash the following.
#with open('ChatBotData.py', 'w') as _CBD:
    #_CBD.write(Test)