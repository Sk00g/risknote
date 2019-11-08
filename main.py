import json
import requests


# s98jl0c90jtnpogqbrvshjsf32
# s98jl0c90jtnpogqbrvshjsf32


if __name__ == '__main__':
    print('... running risknote v1.01')

    with open('config.json', 'r') as file:
        config = json.load(file)
    print('... loaded config from file')

    session = requests.Session()

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cache-control': 'no-cache',
        'connection': 'keep-alive',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'origin': 'https://www.conquerclub.com',
        'referer': 'https://www.conquerclub.com/public.php?mode=home',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

    }

    login_data = {
        'username': config['username'],
        'password': config['password'],
        'connect': "",
        'direct': '35###www.conquerclub.com###',
        'submit': 'Login',
        'redirect': "",
        'protocol': 'HTTPS'
    }

    cookies = {
        'PHPSESSID': 's98jl0c90jtnpogqbrvshjsf32',
        'cc_username': 'Sk00g',
        'login_return': '%2Fpublic.php%3Fmode%3Dhome',
        '__utmv': '155244841.|1=Member%20Type=Free=1',
        '__gads': 'Test',
        'browser': '70a6ca917b267c5f8c2b96c5d3aa9afb',
        'referer': '%5Bdirect%5D',
        'referer60': '%5Bdirect%5D',
        'style_cookie': 'null'
    }

    print('... sending post request\n\n')
    response = session.post(config['loginUrl'],
                            data=login_data,
                            headers=headers,
                            cookies=cookies)
    # response = session.post('http://httpbin.org/post',
    #                          data=login_data,
    #                          headers=headers)

    # print(response)
    # print()
    # print(response.text)

    for header in response.request.headers:
        print('%s: %s' % (header, response.request.headers[header]))

    print('\n%s\n' % response)

    if response.status_code == 400:
        print(response.text)

    print('\n')

    for header in response.headers:
        print('%s: %s' % (header, response.headers[header]))

    print('\n\n')

    # response = session.get(config['statusUrl'])

    # print('\n%s\n' % response)

    # print(response.text[:256])

    print('... exiting')