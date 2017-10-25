import csv
from konlpy.tag import Mecab
from collections import Counter


class FacebookAnalysis:
    def __init__(self):
        self._PATH = '/Users/gyukebox/depromeet/depromeet_mining/data'

    def __str__(self):
        return 'Code for analyzing Depromeet facebook group'

    def _open_file(self, filename):
        """
        Opens file from given file name
        :param filename: name of file to open
        :return: file object
        """
        try:
            return open('{}/{}'.format(self._PATH, filename), 'r', encoding='utf8')
        except FileNotFoundError:
            return None

    @staticmethod
    def find_common(filename):
        """
        Finds common keyword in given file(name)
        :param filename: name of file to analyze
        :return: Common keyword of file(returned as list of tuples)
                 Returned result is sorted
        """
        file = sample._open_file(filename)
        keywords = list()

        while True:
            line = file.readline().split(',')
            keywords += line[:-1]
            if line == ['']:
                break

        mecab = Mecab()
        category = ['NNP', 'NNG', 'SL', 'VV', 'VA', 'XR', 'VA+ETM', 'NP+VCP+EC']
        keywords = [classification[0] for classification in mecab.pos(str(keywords)) if classification[1] in category]

        cnt = sorted(Counter(keywords).items(), key=lambda x: x[1], reverse=True)
        return cnt


if __name__ == '__main__':
    sample = FacebookAnalysis()
    file_names = ['interests.txt', 'likes.txt', 'dislikes.txt']
    for file_name in file_names:
        common_category = sample.find_common(file_name)
        with open('../../web/{}'.format(file_name), 'w', encoding='utf8') as csvfile:
            csvfile.write('word,freq\n')
            writer = csv.writer(csvfile)
            writer.writerows(common_category)
