#import urllib
import urllib.request
import urllib.parse

def read_text():
	with open("C:\prank\movie_quotes.txt") as quotes:
		data = quotes.read()
	check_profanity(data)


def check_profanity(text_to_check):
	url="http://www.wdylike.appspot.com/?q=" + text_to_check
	resp = urllib.request.urlopen(url)
	respData = resp.read().decode("utf-8")
	print(respData)
	connection.close

read_text()



