import csv
import pandas as pd
from collections import Counter
from konlpy.tag import Kkma, Mecab

# temporary path for file
PATH = '/Users/gyukebox/depromeet/depromeet_mining/data'


class KakaoAnalysis:
    def __init__(self):
        self.file = open('{}/data.csv'.format(PATH), 'r', encoding='utf8')
        self.reader = csv.reader(self.file)
        self.frame = pd.read_csv(self.file)

    def __str__(self):
        return '디프만 카톡방 데이터 분석하는 클래스'

    # TODO implemention of function
    def _preprocess(self, conversation):
        """
        Preprocesses data(카카오톡 대화 중 필요없는 내용 삭제)
        :return: preprocessed data
        """
        # 이모티콘 삭제
        while True:
            try:
                conversation.remove('(이모티콘)')
            except ValueError:
                break
        # 사진들 삭제
        while True:
            try:
                conversation.remove('사진')
            except ValueError:
                break
        # 불필요한 줄바꿈 삭제
        while True:
            try:
                conversation.remove('\n')
            except ValueError:
                break
        return conversation

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
        return {row[1] for row in self.reader}

    def get_all_conversations(self):
        self._rewind()
        result = list()
        for row in self.reader:
            single_conversation = row[2].split(' ')
            for word in single_conversation:
                result.append(word)
        return result
        # return [row[2] for row in self.reader]

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
        self._rewind()

        # get all conversations
        all_conversations = self.get_all_conversations()

        # word parser objects
        mecab = Mecab()
        kkma = Kkma()

        # parse all conversation words, and get only nouns
        all_nouns = list()
        for conversation in all_conversations:
            all_nouns += mecab.nouns(conversation)

        # exclude family name(성) from name
        names_list = list()
        for name in self.get_all_names():
            preprocessed_name = kkma.nouns(name)
            for data in preprocessed_name:
                if len(data) != 1:
                    names_list.append(data)

        # compare two list
        mentioned_people = [person for person in all_nouns if person in names_list]

        # count using Counter and return
        cnt = Counter(mentioned_people)
        return cnt.most_common(len(cnt))

    def find_common_topic(self):
        """
        Finds common topic of overall conversation, and stores into csv file.
        :return: void. csv file will be generated
        """
        # Get conversation
        self._rewind()
        all_conversations = self._preprocess(self.get_all_conversations())

        # perform nlp on all words of conversation
        mecab = Mecab()
        category = ['NNP', 'NNG']
        keywords = [classification[0] for classification in mecab.pos(str(all_conversations)) if classification[1] in category]

        freq = Counter(keywords).most_common(300)
        return freq


if __name__ == '__main__':
    sample = KakaoAnalysis()
    print(sample.find_loquacity())
    # print(sample.find_most_mentioned())
    topic = sample.find_common_topic()
    with open('../../web/words.csv', 'w', encoding='utf8') as csvfile:
        csvfile.write('word,freq\n')
        writer = csv.writer(csvfile)
        writer.writerows(topic)
