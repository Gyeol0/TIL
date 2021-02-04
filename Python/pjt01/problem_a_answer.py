import json
from pprint import pprint


def movie_info(movie):
    new_movie_dict = {}
    # 서비스에 필요한 정보 리스트 할당
    info = ['genre_ids', 'id', 'overview',  'poster_path', 'title', 'vote_average']
    # info 리스트를 순회하면서 정보 dict 저장
    for i in info:
        new_movie_dict[i] = movie.get(i)

    return new_movie_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))
