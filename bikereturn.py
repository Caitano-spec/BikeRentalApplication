from tkinter import *



#window

display = Tk()

#window title and dimenson

display.title("Mike Goodwin's - Bike Return ")

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

#labels

greeting_label = Label(text = "Thank You for Returning your Bike")
greeting_label.config(bg="#269fe0", fg ="#FFFFFF", font=(font_style, 15 , "bold"), height = 2) 
greeting_label.grid(row = 1, column = 6)



def main_menu ():
    display.destroy()
    import tkinker22

#buttons

btn = Button(display, text = ' Exit ', bd = '5',width = 20, height = 3, command = display.destroy)

btn.grid(row = 2, column = 6)

btn = Button(display, text = ' Back ', bd = '5',width = 20, height = 3, command =  main_menu)

btn.grid(row = 3, column = 6) 





