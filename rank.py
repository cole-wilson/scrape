import requests

def g(url):
  try:
    r = requests.get(url)
    r = str(r.content).replace('\\n','\n')  .replace('\\t','\t')
    return(r)
  except:
    return('')

def main():
  a = []
  base = 'https://moz.com/top500'
  r = g(base)
  r = r.split('</td><td><a href="')
  r = r[1:len(r)]
  urls = []
  for x in r:
    if x[0:2] == '//':
      x = 'https:' + x[0:len(x)]
    elif x[0:2] =='./':
      x = base + x[0:len(x)]
    elif x[0:3] =='../':
      x = ''
    elif x[0] =='#':
      x = ''
    elif x[0] == '/':
      x = base + x[0:len(x)]
    c = ''
    for y in range(len(x)):
      if x[y] != '"':
        c = c + x[y]
      else:
        urls.append(c)
        break

  for x in urls:
    if (x not in a) and (x != '#') and (x !=  '#start-of-content') and (x != ''):
      a.append(x)
  f = open('top','w+')
  for x in a:
    f.write(x+'\n')

  f.close()
