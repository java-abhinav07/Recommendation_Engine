from bs4 import BeautifulSoup as bs
import regex as re 
import csv
from urllib.request import urlretrieve
from urllib.parse import quote
import requests
from tqdm import tqdm




"""https://www.youtube.com/embed/scraped_code"""

with open('/home/abhinavjava/Projects/Website_Project/Recommendation_Engine/Dataset/main_movie.csv', 'r') as inpt, open('/home/abhinavjava/Projects/Website_Project/Recommendation_Engine/Dataset/main_movie_new.csv', 'w') as outpt:
    csvwriter = csv.writer(outpt)
    reader = csv.reader(inpt)
    counter = 0
    for row in tqdm(reader):
        #print(row)
        if row[0] == "id":
            row.append("YT_link")
        else:
            if len(row)!=11:
                url = "https://www.youtube.com/results?search_query=" + quote(str(row[1]) + "movie trailer")
                page = requests.get(url)

                soup = bs(page.content, 'html.parser')
                if soup:
                    table = soup.find('div', attrs={'id':'content'})
                    if table:
                        table2 = table.find_all('', class_="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix")
                        if table2:
                            result = str(table2[0])

                            x = result.index("data-context-item-id=")
                            y = result.index('" data-visibility-tracking')

                            result = result[x+len("data-context-item-id")+2:y]
                            #results.find_all('', class_=)
                            #print(result)
                            row.append(result)


        csvwriter.writerow(row)
        counter += 1
        #print(counter)





#"https://www.youtube.com/results?search_query=" + title