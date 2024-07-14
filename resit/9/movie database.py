import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
movies = collection.getElementsByTagName('Movie')
collection2 = movies.documentElement
titles = collection2.getElementsByTagName('Title')
for movie in movies: 
    print(movie.getElementsByTagName('Title')[0].firstChild.nodeValue, movie.getElementsByTagName('Year')[0].firstChild.nodeValue, movie.getElementsByTagName('Genre')[0].firstChild.nodeValue)
for title in titles:
    print(title.getElementsByTagName('runtime')[0].firstChild.nodeValue)