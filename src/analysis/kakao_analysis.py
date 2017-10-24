import csv
import json
import pandas as pd

from konlpy.tag import Kkma

# temporary path for file
PATH = '/Users/gyukebox/depromeet/depromeet_mining/src/analysis'


class KakaoAnalysis:
    def __init__(self):
        self.file = open('{}/data.csv'.format(PATH), 'r', encoding='utf8')
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
        indices = [datum[0] for datum in data[:15]]
        values = [datum[1] for datum in data[:15]]
        return pd.DataFrame(index=indices, data=values, columns=['words'])

    def find_most_mentioned(self):
        """
        Returns how many times that people has been mentioned in conversation
        :return: DataFrame object containing person's name and number of mentions
        """
        # 모든 대화를 담는다
        all_conversations = list()
        self._rewind()
        for row in self.reader:
            all_conversations.append(row[2])
        for conv in all_conversations:
            print(conv)
            # 자연어 처리 한다
            # 이름 집합이랑 비교 한다
            # 카운터로 세서 값 리턴해본다
        return None


if __name__ == '__main__':
    sample = KakaoAnalysis()
    sample.find_most_mentioned()
