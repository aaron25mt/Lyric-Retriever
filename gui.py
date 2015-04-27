import rapgenius
import Tkinter

class GUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		songField = Tkinter.Entry(self)
		songField.grid(column=1, row=0, sticky="EW")
		artistField = Tkinter.Entry(self)
		artistField.grid(column=1, row=1, sticky="EW")

		lyricsButton = Tkinter.Button(self, text="Get Lyrics", command=self.onButtonClick)
		lyricsButton.grid(column=0, row=2, columnspan=2)

		songLabel = Tkinter.Label(self, text="Song Name:", anchor="w", fg="black")
		songLabel.grid(column=0, row=0, columnspan=1, sticky="EW")
		artistLabel = Tkinter.Label(self, text="Artist Name:", anchor="w", fg="black")
		artistLabel.grid(column=0, row=1, columnspan=1, sticky="EW")

		self.grid_columnconfigure(0, weight=1)
		self.resizable(False, False)
		self.update()
		self.geometry(self.geometry())

	def onButtonClick(self):
		print(songField.get())
		print(rapgenius.getLyrics(getPotentialLinks(songField.get(), artistField.get())[0]))

if __name__ == "__main__":
	gui = GUI(None)
	gui.title("robottom's Lyric Retriever")
	gui.mainloop()