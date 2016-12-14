import time
import webbrowser
import pafy

url="https://www.youtube.com/watch?v=lKVs9PHvV2U"
video = pafy.new(url)
videoLength=video.length


print("Enter no of breaks")
numberOfBreaks =input()
i=0

#numberOfBreaks=3
breakCount=0

print("This program started on "+time.ctime())
while breakCount < int(numberOfBreaks):
	#todo -add code to close video when it ends
	print("going on a break")
	print("Your "+ str(breakCount) +"started at "+time.ctime())
	time.sleep(10)
	webbrowser.open(url,new=0)
	breakCount+=1

