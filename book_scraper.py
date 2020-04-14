import regex as re 
from bs4 import BeautifulSoup as bs
import csv
import requests


def good_reads(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    results = soup.find(id="all_votes")


    titles = results.find_all('', class_='bookTitle')
    authors = results.find_all('', class_='authorName__container')
    ratings = results.find_all('', class_='greyText smallText uitext')
    img = results.find_all('', class_="bookCover")

    title_list = []
    rating_list = []
    author_list = []
    img_src = [] # needs to be changed

    for tit in titles:
        for titl in tit:
            for title in titl:
                title = title.strip()
                if title != '':
                    title_list.append(title)


    for aut in authors:
        for auth in aut:
            for author in auth:
                for item in author:
                    if len(item)>1:
                        author_list.append(item)


    for rate in ratings:
        for rating in rate:
            #print(rating)
            x = re.findall(r"\d+\.\d+", str(rating))
            if x != []:
                rating_list.append(float(x[0]))


    for item in img:
        img_src.append((str(item)[str(item).index('http'):-3]))




    #print(title_list)
    #print(author_list)
    #print(rating_list)
    #print(img_src)

    data = zip(title_list, author_list, rating_list, img_src)
    #print(list(data))
    return data





def write(data, filename="book_data.csv"):
    fields = ['Title', 'Author', 'Rating', 'Image Source']
    rows = []
    for d in data:
        rows.append(list(d))

    with open(filename, 'a') as f:
        csvwriter = csv.writer(f)
        #csvwriter.writerow(fields)
        csvwriter.writerows(rows)

for i in range(11, 21):
    data = good_reads('https://www.goodreads.com/list/show/1.Best_Books_Ever?page=' + str(i))
    write(data)