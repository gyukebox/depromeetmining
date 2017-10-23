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
        """
        Returns how many people exists in Kakaotalk chatroom
        :return: number of people
        """
        return len(self.get_all_names())

    def find_loquacity(self):
        """
        Finds loquacity(measure of frequency of talking) of people
        :return: DataFrame object containing person's name and number of words
        """
        data = dict()
        # itertuples 말고 더 좋은 성능 향상법이 있을까?
        for row in self.frame.itertuples():
            if row[2] in data.keys():
                data[row[2]] += len(row[3])
            else:
                data[row[2]] = len(row[3])
        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return pd.DataFrame(data, columns=['Name', 'words'])  # most 10

    def find_most_mentioned(self):
        """
        가장 많이 언급된 사람을 찾아주는 함수
        :return:
        """


if __name__ == '__main__':
    sample = KakaoAnalysis()
    print(sample.get_all_names())
    print(sample.get_people_number())
    result = sample.find_loquacity()
    print(result)
