import csv

'''
Reading csv files
'''

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print (row)
        #a, b, c, d = row #error as in second row it doesn't have any value.
        # print (a,b,c,d)


'''
Writing to the files
'''

# Needs list of list to work properly.
hosts = [[1,2,3,4],[5,6,7]]
with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    #This unfortunately prints out a new line everytime.
    writer.writerows(hosts)

# Can use simple list to help and resolve this.
hosts = [1]
with open('test1.csv', 'w') as file:
    writer = csv.writer(file)
    #This unfortunately prints out a new line everytime.
    writer.writerow(hosts)
