import requests
from tmdb import URLMaker


def popular_count():
    # 인스턴스 생성
    maker = URLMaker('pass')
    # 영화 리스트 조회 URL 생성
    url = maker.get_url('movie', 'popular')

    # requests 패키지를 이용하여 URL에 요청
    res = requests.get(url)
    # json 변환
    movie_dict = res.json()
    # 영화 리스트의 개수 계산
    result = len(movie_dict.get('results'))
    return result

if __name__ == '__main__':
    print(popular_count())