import requests as req


def get(num):
    url = f'http://numbersapi.com/{num}/math?json=true'
    if req.get(url).json()['found']:
        return 'Interesting'
    else:
        return 'Boring'

if __name__ == '__main__':
    with open('./num.txt') as f:
        for num in f:
            print(get(int(num)))

