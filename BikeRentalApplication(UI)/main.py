from tkinter import *



#window

display = Tk()



#window title and dimenson

display.title("Goodwin Bike's - Main Menu")

#geometry(widthxheight)

display.geometry('700x700')
display.config(padx=50, pady=50)
display.configure(bg = '#269fe0')

#font style

font_style = "Cavolini"

#widgets

#canvas

canvas = Canvas(height=92, width=436, highlightthickness=0)
logo_img = PhotoImage(file="logo4.png")
canvas.config(bg= '#269fe0')
canvas.grid(row=0, column=1)
img_label2 = Label(image=logo_img)
img_label2.grid(row=0, column=6) 

#Labels

greeting_label = Label(text = "Welcome to Mike Goodwin's Bike Service")
greeting_label.config(bg="#269fe0", fg ="#FFFFFF", font=(font_style, 15 , "bold"), height = 2) 
greeting_label.grid(row = 1, column = 6)



#entries




#pages

def hireabike():
    display.destroy()
    import hirebike

def returnbike():
    display.destroy()
    import bikereturn

def log():
    display.destroy()
    import bikelog



Button(
    display, 
    text="Hire a Bike", 
    font= font_style,
    height = 5,
    width = 30, 
    command= hireabike
    ).grid(row = 3, column = 6)

Button(
    display, 
    text="Return Bike", 
    font= font_style,
    height = 5,
    width = 30,
    command= returnbike
    ).grid(row = 5, column = 6)

Button(
    display, 
    text="Track My Progress", 
    font= font_style,
    height = 5,
    width = 30, 
    command= log
    ).grid(row = 7, column = 6)

btn = Button(display, text = ' Exit ', bd = '5',width = 20, height = 3, command = display.destroy)
btn.grid(row = 5, column = 5) 





#Tkinter execution

display.mainloop()
