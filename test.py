import requests


while (True):
  print("please write URL")
  URLs = list(map(str, input().split(',')))
  print(URLs)
  for URL in URLs:
    if ('https://' not in URL):
        URL = 'https://' + URL
        if ('com' not in URL):
            URL = URL + 'com'
    response = requests.get(URL)
    if (response.status_code == 200):
        print(f'{URL} is UP!')
    else:
        print(f'{URL} is Down!')

  