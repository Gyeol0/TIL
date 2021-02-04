import json


def max_revenue(movies):
    # 최댓값 초기값
    max_rev = -9999999999999
    # 영화 리스트를 순회
    for movie in movies: # 20개의 영화
        movie_id = movie.get('id')
        # 각 영화 id에 따라 상세 정보 불러오기
        info_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        info_dict = json.load(info_json)
        # 최댓값 비교
        if max_rev < info_dict.get('revenue'):
            max_rev = info_dict.get('revenue')
            max_movie = info_dict.get('title')

    return max_movie

        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    print(max_revenue(movies_list))
    