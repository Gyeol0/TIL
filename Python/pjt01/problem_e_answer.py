import json


def dec_movies(movies):
    dec_list = []
    # 영화 리스트를 순회
    for movie in movies:
        movie_id = movie.get('id')
        # 각 영화 id에 따라 상세 정보 불러오기
        info_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        info_dict = json.load(info_json)
        
        if info_dict.get('release_date')[5:7] == '12':
            dec_list.append(info_dict.get('title'))
    
    return dec_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))