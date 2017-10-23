import csv
import json
import pandas as pd


class KakaoAnalysis:
    def __init__(self):
        self.file = open('data.csv', 'r', encoding='utf8')
        self.reader = csv.reader(self.file)
        self.frame = pd.read_csv(self.file)

    def __str__(self):
        return '디프만 카톡방 데이터 분석하는 클래스'

    @staticmethod
    def store_to_json(data, filename):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def _rewind(self):
        """
        Rewinds file cursor to front
        :return: void
        """
        self.file.seek(0)

    def get_all_names(self):
        """
        Returns all people's names
        :return: Set of names
        """
        self._rewind()
        result = {row[1] for row in self.reader}
        return result

    def get_people_number(self):
        return len(self.get_all_names())

    def find_most_loquacious(self):
        """
        가장 말이 많은 사람을 찾아주는 함수
        :return: 가장 말 많은 사람의 이름
        """
        data = dict()
        for row in self.frame.itertuples():
            if row[2] in data.keys():
                data[row[2]] += len(row[3])
            else:
                data[row[2]] = len(row[3])
        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        print(data)  # test
        return data[:15]  # most 10

    def find_most_mentioned(self):
        """
        가장 많이 언급된 사람을 찾아주는 함수
        :return:
        """


if __name__ == '__main__':
    sample = KakaoAnalysis()
    print(sample.get_all_names())
    print(sample.get_people_number())
    result = sample.find_most_loquacious()
    print(result)
