import json
from pprint import pprint


def movie_info(movies, genres):
    # 새로운 영화 정보들을 담을 리스트
    new_movies_list = []
    # 새로운 정보 리스트
    info = ['id', 'overview',  'poster_path', 'title', 'vote_average']
    # 상위 20개의 영화들을 차례로 순회한다.
    for movie in movies:
        genre_name = []
        new_movie_dict = {}
        # 각각의 영화의 genre_ids를 genre_names으로 변환한다.
        for genre_id in movie.get('genre_ids'):
            for genre_dict in genres:
                if genre_id == genre_dict.get('id'):
                    genre_name.append(genre_dict.get('name'))
                    break
        
        # 새로운 영화 정보 입력
        new_movie_dict['genre_names'] = genre_name
        for i in info:
            new_movie_dict[i] = movie.get(i)
        # 새로운 정보들이 입력된 딕셔너리를 리스트에 append
        new_movies_list.append(new_movie_dict)
    return new_movies_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)
    pprint(movie_info(movies_list, genres_list))