import requests, re

class Page:
  def __init__(self, url):
    try:
      tmp = str(requests.get(url).content)
      tmp = tmp.replace('b\'','').replace('\\n','\n')
    except:
      print('error.')
      tmp = ''
    self.content = tmp
    self.url = url
    del tmp
    
bob = Page('https://google.com')
print(bob.content)

#TODO: Add the main loop.