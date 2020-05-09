import csv

file = open("notes.csv", mode="w", newline='')
writer = csv.writer(file)
writer .writerow(["title", "price", "img_src"])