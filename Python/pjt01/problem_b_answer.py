import json
from pprint import pprint


def movie_info(movie, genres):
    # 새로운 영화 정보를 담을 딕셔너리
    new_movie_dict = {}
    info = ['id', 'overview',  'poster_path', 'title', 'vote_average']
    # 변환된 영화 장르를 넣을 리스트
    genre_name = []
    # 장르 id
    for i in movie.get('genre_ids'):
        for genre_dict in genres: 
            if i == genre_dict.get('id'):
                genre_name.append(genre_dict.get('name'))
                break

    new_movie_dict['genre_names'] = genre_name
    for i in info:
        new_movie_dict[i] = movie.get(i)
    return new_movie_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))