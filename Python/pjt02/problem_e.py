import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    # 인스턴스 생성
    maker = URLMaker('pass')
    # 영화 제목에 대한 id 변환
    movie_id = maker.movie_id(title)
    # movie_id가 있으면
    if movie_id:
        # credits URL 생성
        credits_url = maker.get_url('movie', f'{movie_id}/credits', region='KR', language='ko')
        res = requests.get(credits_url)
        credits_dict = res.json()

        # 배우 리스트 생성
        cast_list = [cast.get('name') for cast in credits_dict.get('cast') if cast.get('cast_id') < 10]
        # 감독 리스트 생성
        crew_list = [crew.get('name') for crew in credits_dict.get('crew') if crew.get('department') == 'Directing']
       
        result = {
            'cast': cast_list,
            'crew': crew_list
        }

        return result
    # movie_id가 None이면 None 반환
    return None


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None