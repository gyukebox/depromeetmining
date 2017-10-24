from src.analysis.kakao_analysis import KakaoAnalysis
from src.analysis.visualization import Visualizer


class KakaoAnalysisTest:
    def __init__(self):
        self.testcase = KakaoAnalysis()
        self.visulizer = Visualizer()

    def __str__(self):
        return 'Test code for KakaoAnalysis and Visualizer'

    def test_loquacity(self):
        self.visulizer.plot_bar_pandas(self.testcase.find_loquacity())


if __name__ == '__main__':
    test = KakaoAnalysisTest()
    test.test_loquacity()
