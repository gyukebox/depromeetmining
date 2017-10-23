import csv
import pandas as pd


class DataSet:
    def __init__(self):
        self.file = open('data.csv', 'r', encoding='utf8')
        self.reader = csv.reader(self.file)
        self.frame = pd.read_csv(self.file)

    def __str__(self):
        return '디프만 데이터분석에 필요한 데이터가 있는 클래스'

    def _rewind(self):
        self.file.seek(0)

    def print_all_data(self):
        for row in self.reader:
            print(row)
        self._rewind()


if __name__ == '__main__':
    sample = DataSet()
    sample.print_all_data()
