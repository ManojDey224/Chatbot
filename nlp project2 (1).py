from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3
import speech_recognition as s
import threading

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()

convo = open('dataset.txt','r').readlines()


bot = ChatBot("MY Bot")

trainer=ListTrainer(bot)

trainer.train(convo)
#convo=[
      # 'hello',
       #'hi there !',
       #'what is your name ?',
       #'My name is Bot , I am created by Shew , Anik ,manoj',
       #'how are you ?',
       #'I am doing great these days',
       #'thankyou',
       #'In which city you live ?',
       #'I live in Kolkata',
       #'In which language you talk',
       #' I mostly talk in English ',
    #   ]
    

# now training the bot with the help of trainer


#trainer.train(f)

#answer = bot.get_response("what is your name?")
#print(answer)

#print("Talk to bot ")
#while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)
     
main = Tk()

main.geometry("450x770")
main.borderwidth=('30')

main.title("TPI CHAT BOT")
img = PhotoImage(file="tpi.png")

photoL = Label(main, image=img,borderwidth=20,bg="#00ff66",relief='groove')
main["bg"]="#33cc33"

photoL.pack(pady=5)

#takey query : takes audio as input from user and converts it to string.

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query,)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)
    
frame=Frame(main)

sc = Scrollbar(frame)
msgs=Listbox(frame,width=80,height=15, bg='#ffcc99',yscrollcommand = sc.set,borderwidth=15,fg='#000000',relief='sunken')
sc.pack(side=RIGHT, fill = Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()
sc.config(command=msgs.yview,)

# creating text field

textF=Entry(main,font=("Time New Roman",20),bg='#333333',borderwidth=15,fg='#ffffff')
textF.pack(fill=X,pady=15)

btn=Button(main,text="Ask from bot", bg='#00ff99',fg='#000000',activebackground='#33ff99',font=("Time New Roman", 20),borderwidth=15,command=ask_from_bot,)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()
    
#going to binid main window with enter key....

main.bind('<Return>', enter_function)



def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)

t.start()

main.mainloop()
