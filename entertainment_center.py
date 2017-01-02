import media


toy_story =media.Movie("Toy Story",
 						"A Story about a boy and his toys that come alive",
 						"http://upload.wikipedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 						"https://www.youtube.com/watch?v=4KPTXpQehio")


#print(toy_story.storyline)


avatar =media.Movie("Avatar",
 						"A marine on an alien planet",
 						"https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg#/media/File:Avatar-Teaser-Poster.jpg",
 						"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

passangers= media.Movie("Passangers",
						"A story about two people who wake up 90 years too soon from an induced hibernation on board a spaceship bound for a new planet.",
						"https://en.wikipedia.org/wiki/Passengers_(2016_film)#/media/File:Passengers_2016_film_poster.jpg",
						"https://www.youtube.com/watch?v=7BWWWQzTpNU")

passangers.show_trailer()



