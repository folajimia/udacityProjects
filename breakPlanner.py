import time
import webbrowser


print("Enter no of breaks")
numberOfBreaks =input()
i=0

#numberOfBreaks=3
breakCount=0

print("This program started on "+time.ctime())
while breakCount < numberOfBreaks:
	print("going on a break")
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=lKVs9PHvV2U",new=0)
	breakCount+=1

