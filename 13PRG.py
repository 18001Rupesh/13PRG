from tkinter import *
from unittest import skip
import random
window = Tk()
window.title("Year 9 English Language Feature Quiz")
window.config(bg = "#74a3ab")
window.geometry("1000x700")
titleLabel = Label(window, bg = "#74a3ab", text="Year 9 English Language Feature Quiz", font=("Helvetica",18))
titleLabel.place(x=150, y=30)

Question_List = [["The sky wept across the grey land.","onomatopoeia","personification","alliteration"],["He has a heart of gold.","metaphor","simile","metaphor"],["The snake slid across the sandy shore","alliteration","hyperbole","simile"], [" I love you to the moon and back.","hyperbole","metaphor","simile"],["The waves smashed and crashed and bashed the rocks.", "alliteration","metaphor","onomatopoeia"],["Twinkle, twinkle little star, how I wonder what you are.","rhyme", "metaphor","simile"],["The stars were diamonds in the black night.","metaphor","simile","rhyme"],["The trees were waving goodbye in the wind", "personification","hyperbole","simile"],["My love is like a red, red rose","alliteration","personification","rhyme"],["My teacher gave me a tonne of homework","hyperbole","metaphor","alliteration"],["First fog froze the sky in a grainy grey","alliteration","personification","rhyme"],["Water, water everywhere nut not a drop to drink","repetition","personification","metaphor"],["He entered the class like a hungry tiger","simile","sibilance"
,"metaphor"],["Don't you want to win?","rhetorical question","personification","rhyme"],["The moonlight smiled on the traveller","personification","rhyme.","metaphor"]]


Question_List = random.sample(Question_List, len(Question_List))

def skip():
    window2.destroy()



def playButton():
    window.destroy()



    for loop in range(15):


        global window2
        window2 = Tk()
        window2.configure(bg = "#74a3ab")
        window2.geometry("700x700")

        Question1 = Label(window2, font=("Helvetica",12),bg = "white", text = Question_List[loop][0])
        Question1.place(x=190,y=20)

        endquizButton  = Button(window2, text="End Quiz", command=exit)
        endquizButton.place (x=600, y=20)

        

        nextButton  = Button(window2, text="Next", command=skip)
        nextButton.place (x=50, y=20)
    

        QuestionA  = Button(window2, text= Question_List[loop][1], command=exit)
        QuestionA.place (x=200, y=90)

        QuestionB  = Button(window2, text=Question_List[loop][2], command=exit)
        QuestionB.place (x=200, y=150)
        
        QuestionC  = Button(window2, text=Question_List[loop][3], command=exit)
        QuestionC.place (x=450, y=90)

        #QuestionD  = Button(window2, text=Question_List[loop][4], command=exit)
        #QuestionD.place(x=350, y=150)




        window2.mainloop()
    









play = Button(window, text="Play", command=playButton,padx=50,pady=10)
play.place(x=150, y=300)


endquizButton  = Button(window, text="End Quiz", command=exit,padx=40,pady=10)
endquizButton.place (x=440, y=300)









    


window.mainloop()