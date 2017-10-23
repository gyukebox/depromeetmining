import csv


if __name__ == '__main__':
    file = open('data.csv', 'r', encoding='utf8')
    reader = csv.reader(file)

    # test
    for row in reader:
        print(row)

    file.seek(0)

    # 사람들의 이름 집합 구해보기
    names = {row[1] for row in reader}
    print(names)
    print(len(names))  # 디프만 톡방에서 말을 "한번이라도" 한 사람 수

    # 가장 말을 많이 한 사람 구해보기

    file.close()

