import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    # 인스턴스 생성
    maker = URLMaker('pass')
    # 영화 리스트 조회 URL 생성
    url = maker.get_url('movie', 'popular')
    # requests 패키지를 이용하여 URL에 요청
    res = requests.get(url)
    # json 변환
    movie_dict = res.json()
    # 영화 리스트
    movie_list = movie_dict.get('results')

    # vote_average을 기준으로 내림차순 정렬
    result = sorted(movie_list, key = lambda x: x.get('vote_average'), reverse = True)
    # 상위 5개 출력
    return result[:5]

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())