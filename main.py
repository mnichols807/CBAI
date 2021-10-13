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
from flask import *
#importing all the methods, classes, functions from flask


app = Flask(__name__)


#This is the first page that comes when you type localhost:5000... it will have a a tag that redirects to a page
@app.route("/")
def  HomePage():
    return "<a href='/runscript'>EXECUTE SCRIPT </a>"

#Once it redirects here (to localhost:5000/runscript) it will run the code before the return statement
@app.route("/runscript")
def ScriptPage():
    #Type what you want to do when the user clicks on the link
    # once it is done with doing that code... it will redirect back to the homepage
    return redirect(url_for("HomePage"))

#Running it only if we are running it directly from the file... not by importing
if __name__ == "__main__":
    app.run(debug=True)
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
print("<html><body>TestingTesting</body></html>")