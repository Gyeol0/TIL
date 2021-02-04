import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    # 인스턴스 생성
    maker = URLMaker('pass')
    # 영화 제목에 대한 id 변환
    movie_id = maker.movie_id(title)
    # movie_id가 있으면
    if movie_id:
        # 영화 추천 URL 생성
        re_url = maker.get_url('movie', f'{movie_id}/recommendations', region='KR', language='ko')
        res = requests.get(re_url)
        re_dict = res.json()
        # 추천 영화 제목 리스트 생성
        result = list(map(lambda x: x.get('title'), re_dict.get('results')))
        return result
    # movie_id가 None이면 None 반환
    return None
    


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
