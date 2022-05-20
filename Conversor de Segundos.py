from tkinter import *


class Converter:
    def __init__(self):
        self.window = Tk()

        self.defaultFont = ('Arial', '10')

        self.container1 = Frame(self.window, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.window, pady=10)
        self.container2.pack()

        self.container3 = Frame(self.window, pady=10)
        self.container3.pack()

        self.title = Label(self.container1, text='Seconds converter', font=('Arial', '10', 'bold'))
        self.title.pack()

        self.seconds = Label(self.container2, text='Enter the number of seconds:', font=self.defaultFont)
        self.seconds.pack(side=LEFT)

        self.boxSeconds = Entry(self.container2, width=15, font=self.defaultFont)
        self.boxSeconds.pack(side=LEFT)

        self.toConvert = Button(self.container3, text='To Convert', width=12, command=self.convert, font=('Calibri', '8'))
        self.toConvert.pack()

        self.result = Label(self.container3, text='', font=self.defaultFont)
        self.result.pack()

        mainloop()


    def convert(self):
        seconds = int(self.boxSeconds.get())
        if seconds >= 3600:
            hours = seconds // 3600
            minutes = (seconds - (hours * 3600)) // 60
            seconds = seconds - (hours * 3600) - (minutes * 60)
            self.result['text'] = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        elif seconds < 3600 and seconds >= 60:
            minutes = seconds // 60
            seconds = seconds - (minutes * 60)
            self.result['text'] = f'00:{minutes:02d}:{seconds:02d}'
        else:
            self.result['text'] = f'00:00:{seconds:02d}'


myConverter = Converter()
