import xml.etree.ElementTree as ET

class Movie:
    def __init__(self, title, runtime, year, genre):
        self.title = title
        self.runtime = runtime
        self.year = year
        self.genre = genre

    def print_details(self):
        print(f"Title: {self.title}, Runtime: {self.runtime} minutes, Year: {self.year}, Genre: {self.genre}")

def parse_movies_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    movies = []
    for movie_elem in root.findall('Movie'):
        title_elem = movie_elem.find('Title')
        genre_elem = movie_elem.find('Genre')
        year_elem = movie_elem.find('Year')
        runtime = int(title_elem.get('runtime', 0))
        title = title_elem.text
        genre = genre_elem.text
        year = int(year_elem.text)
        movie = Movie(title, runtime, year, genre)
        movies.append(movie)

    return movies

xml_file_path = './movies.xml'
movies_list = parse_movies_from_xml(xml_file_path)

for movie in movies_list:
    movie.print_details()
