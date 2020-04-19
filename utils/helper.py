import csv
with open('/home/abhinavjava/Projects/Website_Project/Recommendation_Engine/Dataset/book_data.csv') as inp, open('books_data.csv', 'w') as outp:
    csvwriter = csv.writer(outp)
    reader = csv.reader(inp)
    counter = 1
    for row in reader:
        if row[0] != "Title":
            row1 = [counter]
            row1.extend(row)
            row = row1
            counter += 1
        else:
            row1 = ["id"]
            row1.extend(row)
            row = row1

        csvwriter.writerow(row)

with open('/home/abhinavjava/Projects/Website_Project/Recommendation_Engine/Dataset/movie_data.csv') as inp, open('movies_data.csv', 'w') as outp:
    csvwriter = csv.writer(outp)
    reader = csv.reader(inp)
    counter = 1
    for row in reader:
        if row[0] != "Title":
            row1 = [counter]
            row1.extend(row)
            row = row1
            counter += 1
        else:
            row1 = ["id"]
            row1.extend(row)
            row = row1

        csvwriter.writerow(row)

with open('/home/abhinavjava/Projects/Website_Project/Recommendation_Engine/Dataset/tv_data.csv') as inp, open('tvs_data.csv', 'w') as outp:
    csvwriter = csv.writer(outp)
    reader = csv.reader(inp)
    counter = 1
    for row in reader:
        if row[0] != "Title":
            row1 = [counter]
            row1.extend(row)
            row = row1
            counter += 1
        else:
            row1 = ["id"]
            row1.extend(row)
            row = row1

        csvwriter.writerow(row)

