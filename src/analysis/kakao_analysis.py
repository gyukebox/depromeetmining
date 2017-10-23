import csv
import pandas as pd


class KakaoAnalysis:
    def __init__(self):
        self.file = open('data.csv', 'r', encoding='utf8')
        self.reader = csv.reader(self.file)
        self.frame = pd.read_csv(self.file)

    def __str__(self):
        return '디프만 카톡방 데이터 분석하는 클래스'

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
        result = {row[1] for row in self.reader}
        self._rewind()
        return result

    def get_people_number(self):
        return len(self.get_all_names())

    def find_most_loquacious(self):
        """
        가장 말이 많은 사람을 찾아주는 함수
        :return: 가장 말 많은 사람의 이름
        """
        pass

    def find_most_mentioned(self):
        """
        가장 많이 언급된 사람을 찾아주는 함수
        :return:
        """
