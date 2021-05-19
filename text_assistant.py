#------------------------Modules & Libraries------------------
from tkinter import*
import os
import pyttsx3
import wikipedia

#--------------------text-to-speech-------------------
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate', 125)

class text_assistant:
    def __init__(self,root):
        self.root=root
        self.root.title("Eva")
        self.root.geometry("900x600+300+100")
       
        chitchat_frame=Frame(self.root,bg="deepskyblue3")
        chitchat_frame.place(x=0,y=0,height=600,width=900)
        
        def lets():
            query=chitchat_var.get().lower()
            txtarea.delete(1.0,END)

            if "wikipedia" in query:
                query = query.replace("wikipedia","")
                result=wikipedia.summary(query, sentences=2)
                txtarea.insert(1.0,result)
                return result 
                        
            elif "google" in query:
                webbrowser.open("www.google.com")

            elif "youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open code" in query:
                result=r"C:\Users\Nikhat Parween\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(result)

            elif "open c++ library" in query:
                result=r"C:\Users\Nikhat Parween\Desktop\library"
                os.startfile(result)

            elif "play song online" in query:
                webbrowser.open("www.gaana.com")
            elif "play music online" in query:
                webbrowser.open("www.gaana.com")
                        
            elif "play song" in query:
                result=f"C:\\Users\\Nikhat Parween\\Music\\tune1.mp3"
                os.startfile(result)
            elif "play music" in query:
                result=f"C:\\Users\\Nikhat Parween\\Music\\tune1.mp3"
                os.startfile(result)

                #-----------------pictures------------------
            elif "open pic"in query:
                result=r"C:\Users\Nikhat Parween\Pictures"
                os.startfile(result)
            elif "open photo"in query:
                result=r"C:\Users\Nikhat Parween\Pictures"
                os.startfile(result)

            #---------------------whatsapp-------------------
            elif "open whatsapp" in query:
                result=r"C:\ProgramData\Nikhat Parween\WhatsApp\WhatsApp.exe"
                os.startfile(result)
            elif "send whatsapp msg to me" in query:
                result=r"C:\ProgramData\Nikhat Parween\WhatsApp\WhatsApp.exe"
                os.startfile(result)
                os.system('python automate.py')

            #------------------------------eva-------------------
            elif "your intro" in query:
                result="Hi, I am Eva. How are you?"
                txtarea.insert(1.0,result)
                return result 
            elif "who are you" in query:
                result="Hi, I am Eva. How are you?"
                txtarea.insert(1.0,result)
                return result 

            elif "how are you" in query:
                result="I am fine. Thankyou \nHow may I help you?"
                txtarea.insert(1.0,result)
                return result 

            else:
                result="Sorry!, I can't understand your command. \nPlease try again!"
                txtarea.delete(1.0,END) 
                txtarea.insert(1.0,result)
                return result

        def speak():
            audio=lets()
            engine.say(audio)
            engine.runAndWait()
                               

        chitchat_var=StringVar()
        lbl1=Label(chitchat_frame,text="Ask Me Anything!",font="mistral 30 bold",bg="deepskyblue3")
        lbl1.grid(row=1,column=0,padx=370)
        Entry(chitchat_frame,textvariable=chitchat_var,font="mistral 20 bold",bg="deepskyblue3").grid(row=2,column=0,ipady=8,pady=5,ipadx=150)
        Button(chitchat_frame,text="Let's Go!",font="mistral 25 bold",bg="deepskyblue3",command=lets).grid(row=3,column=0,pady=5,ipadx=50)
        Button(chitchat_frame,text="speak",command=speak,font="mistral 25 bold",bg="deepskyblue3").grid(row=4,column=0,pady=5,ipadx=50)
        txtarea=Text(chitchat_frame,font="mistral 20 bold",width=50,height=5,bg="deepskyblue3")
        txtarea.grid(row=5,column=0,pady=5,columnspan=2)


root=Tk()
obj=text_assistant(root)
root.mainloop()
