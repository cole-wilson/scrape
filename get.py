import rank, config

startsplit = config.startsplit
endsplit = config.endsplit


a = []
d = 0#int(input('Depth: '))
visited = []
depth = 0

def main(url):
  global depth
  visited = []
  visited.append(url)
  base = url
  r = rank.g(base)
  r = r.split(startsplit)
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
      if x[y] != endsplit:
        c = c + x[y]
      else:
        urls.append(c)
        break
  
  for x in urls:
    if (x not in a) and (x != '#') and (x != '#start-of-content') and (x != '') and ('mailto:' not in x) and ('tel:' not in x):
      a.append(x)
  f = open('results','w+')
  for x in a:
    f.write(x+'\n')
