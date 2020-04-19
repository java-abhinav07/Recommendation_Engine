import csv

with open('Dataset/book_data.csv') as inp, open('Dataset/books_data.csv', 'w') as outp:
    csvwriter = csv.writer(outp)
    reader = csv.reader(inp)
    for row in reader:
        print(row)
        if row[0] != 'Title':
            row[-1] = str(row[-1])
            img_src = row[-1]
            img_src = img_src[:-11] + ".jpg"
            print(img_src)
            row[-1] = img_src

        csvwriter.writerow(row)


