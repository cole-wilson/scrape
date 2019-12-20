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
  q = input('Amount of websites: ')
  if (q == 'a')or(q == 'all')or(q == 'al'):
    amo = 500
  else:
    amo = q
  for x in range(int(amo)):
    if r[x][0:2] == '//':
      r[x] = 'https:' + r[x][0:len(r[x])]
    elif r[x][0:2] =='./':
      r[x] = base + r[x][0:len(r[x])]
    elif r[x][0:3] =='../':
      r[x] = ''
    elif (r[x][0] =='#')or(r[x][0] == 't'):
      r[x] = ''
    elif r[x][0] == '/':
      r[x] = base + r[x][0:len(r[x])]
    elif r[x][0:3] == 'htt':
      r[x] = r[x]
    else:
      r[x] = base + r[x]
    c = ''
    for y in range(len(r[x])):
      if r[x][y] != '"':
        c = c + r[x][y]
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