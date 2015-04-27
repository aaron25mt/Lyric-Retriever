from bs4 import BeautifulSoup
import requests

def prompt():
	song = raw_input("Song Name: ")
	artist = raw_input("Artist Name: ")
	potentialLinks = getPotentialLinks(song, artist)
	for pLink in potentialLinks:
		print("\n" + pLink)
		response = raw_input("Does this link seem right? (Y/N) ")
		if(response == 'Y' or response == 'y'):
			link = pLink
			break
	print("\n\n-----Lyrics-----")
	lyrics = getLyrics(link)
	print(lyrics)
	print("------End------\n\n")
	response = raw_input("Would you like to save these lyrics to a text document? (Y/N) ")
	if(response == 'Y' or response == 'y'):
		saveLyrics(lyrics)
	end()

def getPotentialLinks(song, artist):
	potentialLinks = []
	url = "http://genius.com/search?q=" + song.replace(" ", "+") + "+" + artist.replace(" ", "+")
	soup = BeautifulSoup(requests.get(url).text)
	for link in soup.find_all("a"):
		if("lyrics" in str(link.get("href"))):
			potentialLinks.append(link.get("href"))
	return potentialLinks

def getLyrics(link):
	soup = BeautifulSoup(requests.get(link).text)
	return soup.find("div", {"class": "lyrics"}).getText()

def saveLyrics(text):
	lyricsDocName = raw_input("\nName of Doc: ")
	if(not lyricsDocName.endswith(".txt")):
		lyricsDocName += ".txt"
	lyricsDoc = open(lyricsDocName, "w+")
	lyricsDoc.write(text)
	lyricsDoc.close()
	print("")

def main():
	print("Welcome to robottom's RapGenius Lyric Retriever!\n")
	prompt()

def end():
	response = raw_input("Would you like to get lyrics for another song? (Y/N) ")
	if(response == 'Y' or response == 'y'):
		prompt()

if __name__ == '__main__':
	main()