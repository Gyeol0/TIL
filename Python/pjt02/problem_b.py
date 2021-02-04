import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    # 인스턴스 생성
    maker = URLMaker('pass')
    # 영화 리스트 조회 URL 생성
    url = maker.get_url('movie', 'popular')
    # requests 패키지를 이용하여 URL에 요청
    res = requests.get(url)
    # json 변환
    movie_dict = res.json()

    result = []
    # 영화 리스트
    movie_list = movie_dict.get('results')
    # 평점 8 이상인 영화 목록
    for movie in movie_list:
        if movie.get('vote_average') >= 8:
            result.append(movie)
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())    
