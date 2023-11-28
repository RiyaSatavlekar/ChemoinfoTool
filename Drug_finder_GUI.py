from tkinter import Button, Canvas, Entry, Tk, PhotoImage, StringVar
from DrugBank_scraper_Modified import WebScarper
# Main Window
mainWindow = Tk()
mainWindow.title('DrugFinder')

# Canvas
canvas = Canvas(mainWindow)
canvas.pack(fill='both',expand=True)

# Title Image
titleImg = PhotoImage(file='Drugfinder.png')
canvas.create_image(0, 0, image=titleImg, anchor='nw')

# Search Bar
canvas.create_text(30, 30, text='Enter Query', fill='#000000', anchor='nw')
usr_query = StringVar()
searchBar = Entry(mainWindow, textvariable=usr_query, width=30)
tool = WebScarper()
searchButton = Button(mainWindow, text='Search', command=lambda : tool.Scraper(usr_query.get()))
canvas.create_window(120, 30, window=searchBar, anchor='nw')
canvas.create_window(400, 30, window=searchButton, anchor='n')

# Window initiation
mainWindow.geometry('500x500')
mainWindow.mainloop()