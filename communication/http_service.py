import requests

def get_kpop_from_jpop(jpop_artist):
    return requests.get(f'http://localhost:5001/recommend_kpop',
                        params={'jpop_artist': jpop_artist}).json()

def get_jpop_from_kpop(kpop_artist):
    return requests.get(f'http://localhost:5002/recommend_jpop',
                        params={'kpop_artist': kpop_artist}).json()

def get_comparison(artist1, artist2):
    return requests.get(f'http://localhost:5003/compare',
                        params={'artist1': artist1, 'artist2': artist2}).json()