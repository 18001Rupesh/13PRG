from dis import Instruction
from distutils.log import info
from tkinter import *
from unittest import skip
import random

def startup():
    global Question_Amount
    Question_Amount = 15
    global window
    window = Tk()
    window.title("Year 9 English Language Feature Quiz")
    window.config(bg = "#cfe2f3")
    #Adds size for the first screen
    window.geometry("1000x700")
    titleLabel = Label(window, bg = "#cfe2f3", text="Year 9 English Language Feature Quiz", font=("Cooper Black",24))
    titleLabel.place(x=250, y=30)
    global score
    #sets score to 0
    score = 0
    global Question_List
    Question_List = [["Is 'The sky wept across the grey land' personificaton.","True","False"],["Is 'He has a heart of gold' a metaphor.","True","False"],["The snake slid across the sandy shore","alliteration","hyperbole","simile"], [" I love you to the moon and back.","hyperbole","metaphor","simile"],["The waves smashed and crashed and bashed the rocks.", "alliteration","metaphor","onomatopoeia"],["Twinkle, twinkle little star, how I wonder what you are.","rhyme", "metaphor","simile"],["The stars were diamonds in the black night.","metaphor","simile","rhyme"],["The trees were waving goodbye in the wind", "personification","hyperbole","simile"],["My love is like a red, red rose","alliteration","personification","rhyme"],["My teacher gave me a tonne of homework","hyperbole","metaphor","alliteration"],["First fog froze the sky in a grainy grey","alliteration","personification","rhyme"],["Water, water everywhere but not a drop to drink","repetition","personification","metaphor"],["He entered the class like a hungry tiger","simile","sibilance" ,"metaphor"],["Don't you want to win?","rhetorical question","personification","rhyme"],["The moonlight smiled on the traveller","personification","rhyme","metaphor"]]
    global colours
    #colour codes for the differnt interface pages
    colours = ["#91bfbb","#739599", "#93a3e6","#b7c1e8","#aa9bbd","#cedbbd","#8c7fa3","#89b097","#84a19e","#91a3a1"]

    info = Label(window, bg = "#cfe2f3", text="Read & Select the Correct Language Feature", padx=20, pady=20, font=("Cooper Black",16))
    info.place(x=290, y=390)


    Question_List = random.sample(Question_List, len(Question_List))

    #importing the image file
    imagefile = PhotoImage(file="bookimage.png")
    imageLabel = Label(window,image=imagefile,bg="#cfe2f3")
    imageLabel.place(x=450,y=200)

    play = Button(window,borderwidth=1, relief="solid",bg = "#cfe2f3", text="Play",font=("Cooper Black",16),command=playButton,padx=50,pady=10)
    play.place(x=250, y=500)

    #end the quiz button to close the interface
    endquizButton  = Button(window,borderwidth=1, relief="solid",bg = "#cfe2f3", text="End Quiz",font=("Cooper Black",16), command=exit,padx=40,pady=10)
    endquizButton.place (x=650, y=500)
    window.mainloop()



 #Defines the skip button on what to do next after skip is clicked
def skip():
    window2.destroy()


 #Defines the Play Button to close the window once 'play' is pressed
def playButton():
    
    window.destroy()


    #Sets up a loop count 
    for loop in range(Question_Amount):

        #window 2 dimessions
        global window2
        window2 = Tk()
        global colours
        colours = random.sample(colours, len(colours))
        window2.configure(bg = colours[0])
        window2.geometry("980x800")

        imagefile = PhotoImage(file="keepgoing.png")
        imageLabel = Label(window2,image=imagefile,bg=colours[0])
        imageLabel.place(x=350,y=150)

        #QUestion label 
        Question1 = Label(window2, font=("Cooper Black",16),bg = colours[0], text = Question_List[loop][0], padx= 20, pady=20,borderwidth=1,relief="solid")
        Question1.place(x=480,y=50, anchor="center")
        #End the Quiz
        endquizButton  = Button(window2,borderwidth=1, font=("Cooper Black",16), relief="solid",bg = colours[0], text="End Quiz", command=exit)
        endquizButton.place (x=850, y=20)
        #Skip Button for the user
        SkipButton  = Button(window2,borderwidth=1, font=("Cooper Black",16), relief="solid", bg = colours[0],text="Skip", command=skip)
        SkipButton.place (x=50, y=20)
        #randomises the answer positions
        global temp
        temp = []
        temp.append(Question_List[loop][1])
        temp.append(Question_List[loop][2])
        if len(Question_List[loop]) > 3:
            temp.append(Question_List[loop][3])
        temp = random.sample(temp,len(temp))
        #Asnwer A button
        answerA = Button(window2,padx= 10, pady=10,borderwidth=1, relief="solid", font=("Cooper Black",16),bg = colours[0],text= temp[0],command=lambda:answerPress(0))
        answerA.place (x=300, y=400,anchor="center")
        #Asnwer B button
        answerB = Button(window2,padx= 10, pady=10, borderwidth=1, relief="solid",font=("Cooper Black",16),bg = colours[0], text=temp[1],command=lambda:answerPress(1))
        answerB.place (x=300, y=550,anchor="center")
        
        #For the T and F questions determines if 2 buttons need to pop up or 3 
        if len(Question_List[loop]) > 3:
            answerC = Button(window2,padx= 10, pady=10,borderwidth=1, relief="solid", font=("Cooper Black",16),bg = colours[0],text=temp[2],command=lambda:answerPress(2))
            answerC.place (x=650, y=400,anchor="center")


        
        #adds a point to the score is the answer is correct
        #prints the asnwer correct and adds a point if the answer is right
        def answerPress(AnswerNum):
            if temp[AnswerNum] == Question_List[loop][1]:
                answerMessage = Label(window2, bg = "#98FB98",font=("Cooper Black",20),borderwidth=1.5, relief="solid", text="Correct")
                answerMessage.place (x=300, y=400)
                global score
                score += 1
            else:
                #prints incorrect message for the user and does not add a extra point
                answerMessage = Label(window2, bg = "#CD5C5C",font=("Cooper Black",20),borderwidth=1.5, relief="solid", text="Incorrect")
                answerMessage.place (x=300, y=400)
             #Next Qurestion Button For the USer
            nextQuestion  = Button(window2, borderwidth=1,bg = colours[0], relief="solid", font=("Cooper Black",16),text="Next", command=next)
            nextQuestion.place (x=600, y=400)
           #Destroys the window after the answer is selected 
            answerA.destroy()
            answerB.destroy()
            if len(Question_List[loop]) > 3:
                answerC.destroy()




        def next():
            window2.destroy()


        window2.mainloop()




    global window3
    window3 = Tk()
    window3.configure(bg = "#cfe2f3")
    window3.geometry("700x700")
    #Determines the end score based on the amount of questions right and wrong  
    if score <= 9:
        grade = "Not Achived"
    elif score < 12:
        grade = "Achieved"
    elif score  < 13:
        grade = "Merit"
    else:
        grade = "Excellence"
    

    
    print1 = Label(window3,font=("Cooper Black",25), bg = "#cfe2f3", text="Score:")
    print1.place(x=190,y=350)

    print2 = Label(window3,font=("Cooper Black",25), bg = "#cfe2f3", text="Grade:")
    print2.place(x=190,y=500)
    
     #Prints the end results such as score, grade and message
    printScore = Label(window3, font=("Cooper Black",25),bg = "#cfe2f3", text=score)
    printScore.place(x=600,y=350)
    print3 = Label(window3,font=("Cooper Black",25),bg = "#cfe2f3",text=grade)
    print3.place(x=450,y=500)

    if grade == "Excellence":
        message = "Congrats!"
    else:
        message = "Thank You For Playing :)"
    print4 = Label(window3,font=("Cooper Black",25),bg = "#cfe2f3", text=message,padx=30,pady=40,borderwidth=2,relief="solid")
    print4.place(x=190,y=20)



    imagefile = PhotoImage(file="bookout.png")
    imageLabel = Label(window3,image=imagefile,bg="#cfe2f3")
    imageLabel.place(x=340,y=150)


    play = Button(window3,borderwidth=1, relief="solid",bg = "#cfe2f3", text="Play Again",font=("Cooper Black",16),command=restart,padx=50,pady=10)
    play.place(x=100, y=600)


    endquizButton  = Button(window3,borderwidth=1, relief="solid",bg = "#cfe2f3", text="End Quiz",font=("Cooper Black",16), command=exit,padx=40,pady=10)
    endquizButton.place (x=450, y=600)

    window3.mainloop()

#Restarts to the first window once the restart button is clicked
def restart():
    #Destorys the third window
    window3.destroy()
    startup()

startup()

