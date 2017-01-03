import media
import fresh_tomatoes


ghost_in_the_shell =media.Movie("Ghost in the shell",
 						"Cyborg counter-cyberterrorist field commander The Major (Scarlett Johansson), and her task force Section 9 thwart cyber criminals and hackers. Now, they must face a new enemy who will stop at nothing to sabotage Hanka Robotic's artificial intelligence technology",
 						"https://upload.wikimedia.org/wikipedia/en/1/11/Ghost_in_the_Shell_%282017_film%29.png",
 						"https://www.youtube.com/watch?v=G4VmJcZR0Yg")


#print(toy_story.storyline)


alien_covenant  =media.Movie("Alien: Covenant ",
 						"Bound for a remote planet on the far side of the galaxy, the crew of the colony ship Covenant find what they believe to be an uncharted paradise. What the crew discover is a dark, dangerous world, inhabited by the 'synthetic' David (Michael Fassbender), the sole survivor of the doomed Prometheus expedition, and monstrous creatures that are hunting them",
 						"https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
 						"https://www.youtube.com/watch?v=H0VW6sg50Pk")

#print(avatar.storyline)
#avatar.show_trailer()

passangers= media.Movie("Passangers",
						"A story about two people who wake up 90 years too soon from an induced hibernation on board a spaceship bound for a new planet.",
						"https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
						"https://www.youtube.com/watch?v=7BWWWQzTpNU")

#passangers.show_trailer()

valerian= media.Movie("Valerian and the City of a Thousand Planets",
						"Time-traveling agent Valerian is sent to investigate a galactic empire, along with his partner Laureline.",
						"https://upload.wikimedia.org/wikipedia/en/0/07/Valerian_and_the_City_of_a_Thousand_Planets.jpg",
						"https://www.youtube.com/watch?v=BszXhUjJz00")

logan= media.Movie("logan",
						"Logan emerges as a mentor to a mutant girl, who has two claws instead of his three.",
						"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
						"https://www.youtube.com/watch?v=gbug3zTm3Ws")

life= media.Movie("Life",
						"The six-member crew of the International Space Station is tasked with studying a sample from Mars that may be the first proof of extra-terrestrial life, but which proves to be more intelligent than expected",
						"https://upload.wikimedia.org/wikipedia/en/c/c4/Life_%282017_film%29.png",
						"https://www.youtube.com/watch?v=LeLsJfGmY_Y")

movies=[ghost_in_the_shell,alien_covenant,passangers,valerian,logan,life]

fresh_tomatoes.open_movies_page(movies)