from tkinter import *
from unittest import skip
import random
window = Tk()
window.title("Year 9 English Language Feature Quiz")
window.config(bg = "#cfe2f3")
window.geometry("1000x700")
titleLabel = Label(window, bg = "#cfe2f3", text="Year 9 English Language Feature Quiz", font=("Cooper Black",24))
titleLabel.place(x=250, y=30)
global score
score = 0
Question_List = [["The sky wept across the grey land.","onomatopoeia","personification","alliteration"],["He has a heart of gold.","metaphor","simile","metaphor"],["The snake slid across the sandy shore","alliteration","hyperbole","simile"], [" I love you to the moon and back.","hyperbole","metaphor","simile"],["The waves smashed and crashed and bashed the rocks.", "alliteration","metaphor","onomatopoeia"],["Twinkle, twinkle little star, how I wonder what you are.","rhyme", "metaphor","simile"],["The stars were diamonds in the black night.","metaphor","simile","rhyme"],["The trees were waving goodbye in the wind", "personification","hyperbole","simile"],["My love is like a red, red rose","alliteration","personification","rhyme"],["My teacher gave me a tonne of homework","hyperbole","metaphor","alliteration"],["First fog froze the sky in a grainy grey","alliteration","personification","rhyme"],["Water, water everywhere but not a drop to drink","repetition","personification","metaphor"],["He entered the class like a hungry tiger","simile","sibilance" ,"metaphor"],["Don't you want to win?","rhetorical question","personification","rhyme"],["The moonlight smiled on the traveller","personification","rhyme","metaphor"]]


Question_List = random.sample(Question_List, len(Question_List))


imagefile = PhotoImage(file="bookimage.png")
imageLabel = Label(window,image=imagefile,bg="#cfe2f3")
imageLabel.place(x=450,y=200)


def skip():
    window2.destroy()



def playButton():
    
    window.destroy()



    for loop in range(15):


        global window2
        window2 = Tk()
        window2.configure(bg = "#cfe2f3")
        window2.geometry("980x800")

        imagefile = PhotoImage(file="keepgoing.png")
        imageLabel = Label(window2,image=imagefile,bg="#cfe2f3")
        imageLabel.place(x=350,y=150)

        Question1 = Label(window2, font=("Cooper Black",16),bg = "#cfe2f3", text = Question_List[loop][0], padx= 20, pady=20,borderwidth=1,relief="solid")
        Question1.place(x=480,y=50, anchor="center")

        endquizButton  = Button(window2,borderwidth=1, font=("Cooper Black",16), relief="solid",bg = "#cfe2f3", text="End Quiz", command=exit)
        endquizButton.place (x=850, y=20)

        SkipButton  = Button(window2,borderwidth=1, font=("Cooper Black",16), relief="solid", bg = "#cfe2f3",text="Skip", command=skip)
        SkipButton.place (x=50, y=20)
    
        global temp
        temp = []
        temp.append(Question_List[loop][1])
        temp.append(Question_List[loop][2])
        temp.append(Question_List[loop][3])

        answerA = Button(window2,padx= 10, pady=10,borderwidth=1, relief="solid", font=("Cooper Black",16),bg = "#cfe2f3",text= temp[0],command=lambda:answerPress(0))
        answerA.place (x=300, y=400,anchor="center")

        answerB = Button(window2,padx= 10, pady=10, borderwidth=1, relief="solid",font=("Cooper Black",16),bg = "#cfe2f3", text=temp[1],command=lambda:answerPress(1))
        answerB.place (x=300, y=550,anchor="center")
        
        answerC = Button(window2,padx= 10, pady=10,borderwidth=1, relief="solid", font=("Cooper Black",16),bg = "#cfe2f3",text=temp[2],command=lambda:answerPress(2))
        answerC.place (x=650, y=400,anchor="center")


        

        def answerPress(AnswerNum):
            if temp[AnswerNum] == Question_List[loop][1]:
                answerMessage = Label(window2, bg = "#cfe2f3",font=("Cooper Black",20),borderwidth=1.5, relief="solid", text="Correct")
                answerMessage.place (x=300, y=400)
                global score
                score += 1
            else:
                answerMessage = Label(window2, bg = "#cfe2f3",font=("Cooper Black",20),borderwidth=1.5, relief="solid", text="Incorrect")
                answerMessage.place (x=300, y=400)
            
            nextQuestion  = Button(window2, borderwidth=1,bg = "#cfe2f3", relief="solid", font=("Cooper Black",16),text="Next", command=next)
            nextQuestion.place (x=600, y=400)

            answerA.destroy()
            answerB.destroy()
            answerC.destroy()




        def next():
            window2.destroy()


        window2.mainloop()




    global window3
    window3 = Tk()
    window3.configure(bg = "#cfe2f3")
    window3.geometry("700x700")
        
    if score <= 9:
        grade = "Not Achived"
    elif score < 12:
        grade = "Achieved"
    elif score  < 13:
        grade = "Merit"
    else:
        grade = "Excellence",
    
    print = Label(window3,font=("Cooper Black",25), bg = "#cfe2f3", text="Score:",padx=100,pady=100,borderwidth=1,relief="solid")
    print.place(x=190,y=350)

    print = Label(window3,font=("Cooper Black",25), bg = "#cfe2f3", text="Grade:")
    print.place(x=190,y=500)
    
    printScore = Label(window3, font=("Cooper Black",25),bg = "#cfe2f3", text=score)
    printScore.place(x=600,y=350)
    print = Label(window3,font=("Cooper Black",25),bg = "#cfe2f3",text=grade)
    print.place(x=450,y=500)
    print = Label(window3,font=("Cooper Black",25),bg = "#cfe2f3", text="Thank You For Playing :)",padx=30,pady=40,borderwidth=2,relief="solid")
    print.place(x=190,y=20)



    imagefile = PhotoImage(file="bookout.png")
    imageLabel = Label(window3,image=imagefile,bg="#cfe2f3")
    imageLabel.place(x=300,y=150)


    play = Button(window3,borderwidth=1, relief="solid",bg = "#cfe2f3", text="Play Again",font=("Cooper Black",16),command=playButton,padx=50,pady=10)
    play.place(x=100, y=600)

    endquizButton  = Button(window3,borderwidth=1, relief="solid",bg = "#cfe2f3", text="End Quiz",font=("Cooper Black",16), command=exit,padx=40,pady=10)
    endquizButton.place (x=450, y=600)

    window3.mainloop()



        
    

play = Button(window,borderwidth=1, relief="solid",bg = "#cfe2f3", text="Play",font=("Cooper Black",16),command=playButton,padx=50,pady=10)
play.place(x=250, y=500)


endquizButton  = Button(window,borderwidth=1, relief="solid",bg = "#cfe2f3", text="End Quiz",font=("Cooper Black",16), command=exit,padx=40,pady=10)
endquizButton.place (x=650, y=500)

    


window.mainloop()