from src.analysis.kakao_analysis import KakaoAnalysis
from src.analysis.visualization import Visualizer


class KakaoAnalysisTest:
    def __init__(self):
        self.analysis = KakaoAnalysis()
        self.visualizer = Visualizer()

    def __str__(self):
        return 'Test code for KakaoAnalysis and Visualizer'

    def test_loquacity(self):
        """
        Test function of find_loquacity(). Result printed as console output.
        :return: True if test ends without any error. False if any error occurs.
        """
        description = 'Test result for find_loquacity()'
        print('=' * len(description))
        print(description)
        print('=' * len(description))

        try:
            loquacity = self.analysis.find_loquacity()
            print(loquacity)
            self.visualizer.plot_bar_pandas(loquacity)
            print()
            return True
        except Exception as e:
            print('Test failed. Error cause:')
            print(e)
            return False

    def test_mentioned(self):
        """
        Test function of find_most_mentioned(). Result printed as console output.
        :return: True if test ends without any error. False if any error occurs.
        """
        description = 'Test result for find_most_mentioned()'
        print('=' * len(description))
        print(description)
        print('=' * len(description))

        try:
            print(self.analysis.find_most_mentioned())
            print()
            return True
        except Exception as e:
            print('Test failed. Error cause:')
            print(e)
            return False

    def test_common_topic(self):
        """
        Test function for find_common_topic(). Result printed as console output.
        :return: True if test ends without any error. False if any error occurs.
        """
        description = 'Test result for find_common_topic()'
        print('=' * len(description))
        print(description)
        print('=' * len(description))

        try:
            print(self.analysis.find_common_topic())
            print()
            return True
        except Exception as e:
            print('Test failed. Error cause:')
            print(e)
            return False


if __name__ == '__main__':
    test_case = KakaoAnalysisTest()
    test_case.test_loquacity()
    test_case.test_mentioned()
    test_case.test_common_topic()
