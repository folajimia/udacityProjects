import urllib
#import urllib.request
#import urllib.parse


def read_text():
	quotes = open("C:\prank\movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()


	check_profanity(contents_of_file)


def check_profanity(text_to_check):

	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert")
	elif "false" in output:
		print("This document has no curse words")

read_text()


#Try adding a contents_of_file.encode("utf-8") after quotes.close()