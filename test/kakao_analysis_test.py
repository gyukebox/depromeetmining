from src.analysis.kakao_analysis import KakaoAnalysis

# 객체 생성
sample = KakaoAnalysis()


def test_names():
    """
    사람의 이름과 관련된 함수들 테스트
    :return: void
    """
    sample_name = sample.get_all_names()
    for name in sample_name:
        print(name)
    print('Total {} people'.format(sample.get_people_number()))


def test_loquacious():
    """
    "가장 말 많은 사람" - find_most_loquacious 함수 테스트
    :return: 
    """
    pass


def test_mentioned():
    """
    "가장 많이 언급된 사람 - find_most_mentioned 함수 테스트
    :return:
    """
    pass
