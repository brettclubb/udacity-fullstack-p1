import media as m
import fresh_tomatoes as ft

# Create list of movie objects
movies = []
movies.append(m.Movie(
	"Toy Story",
	"http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc"))

movies.append(m.Movie(
	"Avatar",
	"http://ecx.images-amazon.com/images/I/91N1lG%2BLBIS._SY679_.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"))

movies.append(m.Movie(
	"Ocean's Eleven",
	"http://ecx.images-amazon.com/images/I/51wvCeHnHmL.jpg",
	"https://www.youtube.com/watch?v=imm6OR605UI"))

movies.append(m.Movie(
	"Finding Nemo",
	"http://ecx.images-amazon.com/images/I/51qeAio4V-L.jpg",
	"https://www.youtube.com/watch?v=SPHfeNgogVs"))

movies.append(m.Movie(
	"Fight Club",
	"http://ecx.images-amazon.com/images/I/51ORyncmJAL.jpg",
	"https://www.youtube.com/watch?v=SUXWAEX2jlg"))

movies.append(m.Movie(
	"Italian Job",
	"http://ecx.images-amazon.com/images/I/91BI%2BAGPCmL._SY679_.jpg",
	"https://www.youtube.com/watch?v=5Eyw-Qiwpj0"))

# Use movie objects to create and open the movies webpage
ft.open_movies_page(movies)
