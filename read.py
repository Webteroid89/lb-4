import csv
import sys
filename1 = "first_group.txt"
filename2 = "second_group.txt"
fd = open(filename1, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader:
    print(row)  
fd.close()