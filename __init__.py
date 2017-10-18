import csv


if __name__ == '__main__':
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)