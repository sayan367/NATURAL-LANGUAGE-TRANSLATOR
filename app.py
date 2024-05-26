from tkinter import *
from tkinter import ttk 
from tracestack import *
from googletrans import Translator, LANGUAGES
import speech_recognition
import gtts
import playsound

def change(text="type",src="English",dest="Hindi"):
	text1=text 
	src1=src
	dest1=dest
	trans=Translator()
	trans1=trans.translate(text,src=src1,dest=dest1)
	return trans1.text

def data():
	s = comb_sor.get()
	d = comb_dest.get()
	masg = Sor_txt.get(1.0,END)
	textget = change(text=masg, src=s, dest=d)
	dest_txt.delete(1.0,END)
	dest_txt.insert(END,textget)

	audio1 = dest_txt.get(1.0,END)
	
	converted_audio = gtts.gTTS(audio1, lang="hi")
	converted_audio.save("hello.mp3")
	playsound.playsound("hello.mp3")




recognizer = speech_recognition.Recognizer()
# print(googletrans.LANGUAGES)

def mike():
	with speech_recognition.Microphone() as source:
		# print("speak now")
		S1="Speak..."
		Sor_txt.insert(END,S1)
		Sor_txt.delete(1.0,END)
		voice = recognizer.listen(source)
		text_s = recognizer.recognize_google(voice,language="en")
		# print(text)
		Sor_txt.insert(END,text_s)
	# converted_audio = gtts.gTTS(Sor_txt, lang="en")
	# converted_audio.save("hello.mp3")
	# playsound.playsound("hello.mp3")

def mike2():
	# audio1 = dest_txt.get(1.0,END)
	
	# converted_audio = gtts.gTTS(audio1, lang="hi")
	# converted_audio.save("hello.mp3")
	playsound.playsound("hello.mp3")





root = Tk()
root.title("NL_Translator")
root.geometry("500x700")
root.config(bg='#00b3b3')

lab_txt=Label(root,text="Translator",font=("Time New Roman", 40,"bold"),bg='#ff9900')
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

# input box
lab_txt=Label(root,text="Source Text",font=("Time New Roman", 20,"bold"),fg='Black',bg='#00b3b3')
lab_txt.place(x=100,y=90,height=30,width=300)

Sor_txt = Text(frame,font=("Time New Roman", 20,"bold"), wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_txt =list(LANGUAGES.values())

# voice button
photo=PhotoImage(file="mic_1.png")
button_change = Button(frame,image=photo,relief=RAISED, command=mike)
button_change.place(x=440,y=250,height=40,width=40)

comb_sor = ttk.Combobox(frame,value=list_txt)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED, command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_txt)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("Hindi")


# output box
lab_txt=Label(root,text="Translated Text",font=("Time New Roman", 20,"bold"),fg='Black',bg='#00b3b3')
lab_txt.place(x=100,y=360,height=30,width=300)

dest_txt = Text(frame,font=("Time New Roman", 20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

#Speaker button
photo2=PhotoImage(file="speaker1.png")
button_change = Button(frame,image=photo2,relief=RAISED, command=mike2)
button_change.place(x=440,y=520,height=40,width=40)

root.mainloop()