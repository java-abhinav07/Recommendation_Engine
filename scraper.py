import requests
from bs4 import BeautifulSoup as bs
import regex as re
import csv

<<<<<<< HEAD
def imdb(url):
=======
def imdb():
    url = 'https://www.imdb.com/list/ls060918726/'
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
    page = requests.get(url)

    soup = bs(page.content, 'html.parser')
    results = soup.find(id='main')
    elements = results.find_all('', class_='lister-item-header')
    #print(elements)
    genre_tag = results.find_all('', class_='text-muted text-small')
    rating_tag = results.find_all('', class_="ipl-rating-widget")
    people_element = results.find_all('', class_="text-muted text-small")
<<<<<<< HEAD
    duration_element = results.find_all('', class_="text-muted text-small")

=======
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b

    title_list = []
    genre_list = []
    year_list = []
    rating_list = []
<<<<<<< HEAD
    director_list = []
    star_list = []
    duration_list = []
    oscar_list = []

    for element in duration_element:
        duration = (element.find('', class_="runtime"))
        if duration:
            duration = str(duration)
            duration_list.append(int(re.findall(r"\d+", duration)[0]))
    
=======
    #director_list = []
    star_list = []
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b

    for element in elements:
        title = (str(element.find('a')).split('<'))[-2]
        #print(title)
        x = title.index(">")
        title = title[x+1:]
        year_elem = str(element.find('', class_="lister-item-year text-muted unbold"))
        year = re.findall(r'\d+', year_elem)
        #print(title, year[0])
        title_list.append(title)
        year_list.append(year[0])

    for element in genre_tag:
<<<<<<< HEAD
=======
        
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
        genre = str(element.find('', class_="genre")).split("<")
        if genre[0] != 'None':
            genre_list.append(genre[1][19:].strip())

    for element in rating_tag:
        rating = str(element.find('', class_="ipl-rating-star__rating"))
<<<<<<< HEAD
        rating = re.findall(r"\d+\.\d+", rating) 
        if rating != []: 
            rating_list.append(float(rating[0]))
            oscar_list.append(False)
=======
        rating = re.findall(r'\d+', rating) 
        rating_list.append(rating[0])
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b

    for element in people_element:
        people = element.find_all('a')
        if people:
<<<<<<< HEAD
            #x = str(people).index(">")
=======
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
            #director_list.append(str(people[0])[x:-4])
            #print("director:", str(people[0])[x:-4])
            #print(people)
            temp_list = []
            for stars in people[1:]:
                y = str(stars).index(">")
                temp_list.append(str(stars)[y+1:-4])
                #print("stars:", str(stars)[y:-4])

            star_list.append(temp_list)

<<<<<<< HEAD
    #rint(genre_list)
=======
    #print(genre_list)
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
    #print(title_list)
    #print(year_list)
    #print(director_list)
    #print(star_list)
<<<<<<< HEAD
    #print(duration_list)



    data_list = list(zip(title_list, year_list, genre_list, star_list, rating_list, duration_list))
=======

    data_list = list(zip(title_list, year_list, genre_list, star_list))
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
    print(data_list)
    return data_list






<<<<<<< HEAD
def write(data, filename="tv_data.csv"):
    fields = ['Title', 'Year', 'Genre', 'Stars', 'Rating', 'Duration']
=======


def write(data, filename="tv_data.csv"):
    fields = ['Title', 'Year', 'Genre', 'Stars']
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
    rows = []
    for d in data:
        rows.append(list(d))

    with open(filename, 'a') as f:
        csvwriter = csv.writer(f)
        #csvwriter.writerow(fields)
        csvwriter.writerows(rows)


        
        
    




<<<<<<< HEAD
data = imdb('https://www.imdb.com/list/ls008957859/?sort=list_order,asc&st_dt=&mode=detail&page=3')
=======




data = imdb()
>>>>>>> 7ab1e431c9199882b499b5f7156ecba8c2ecd20b
write(data)