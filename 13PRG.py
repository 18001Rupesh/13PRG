from tkinter import *

window = Tk()
window.title("Year 9 English Language Feature Quiz")
window.config(bg = "#74a3ab")
titleLabel = Label(window, bg = "#74a3ab", text="Year 9 English Language Feature Quiz", font=("Helvetica",13))
titleLabel.grid(row=5, column=7,sticky="W",padx=50)

Question_List = [["The sky wept across the grey land.","onomatopoeia","personification","alliteration"],["He has a heart of gold.","metaphor","simile","metaphor"],["The snake slid across the sandy shore","alliteration","hyperbole","simile"], [" I love you to the moon and back.","hyperbole","metaphor","simile"],["The waves smashed and crashed and bashed the rocks.", "alliteration","metaphor","onomatopoeia"],["Twinkle, twinkle little star, how I wonder what you are.","rhyme", "metaphor","simile"],["The stars were diamonds in the black night.","metaphor","simile","rhyme"],["The trees were waving goodbye in the wind", "personification","hyperbole","simile"],["My love is like a red, red rose","alliteration","personification","rhyme"],["My teacher gave me a tonne of homework","hyperbole","metaphor","alliteration"],["First fog froze the sky in a grainy grey","alliteration","personification","rhyme"],["Water, water everywhere nut not a drop to drink","repetition","personification","metaphor"],["He entered the class like a hungry tiger","simile","sibilance"
,"metaphor"],["Don't you want to win?","rhetorical question","personification","rhyme"],["The moonlight smiled on the traveller","personification","rhyme.","metaphor"]]



def playButton():
    window2 = Toplevel(window)
    window2.configure(bg = "#74a3ab")
    window2.geometry("700x700")

    Question1 = Label(window2, bg = "white", text = "The sky wept across the grey land.")
    Question1.grid(row=1,column=0, columnspan=2)


play = Button(window, text="Play", command=playButton)
play.grid(row=15, column=3)






def endquizButton():
    window.quit()
    return

endquizButton  = Button(window, text="End Quiz", command=endquizButton)
endquizButton.grid (row=15, column=10)









    


window.mainloop()