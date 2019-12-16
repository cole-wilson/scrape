import requests

# Definitions
def g(url):
  try:
    r = requests.get(url)
    r = str(r.content).replace('\\n','\n')  .replace('\\t','\t')
    return(r)
  except:
    return('')
def main(url):
  global depth
  visited.append(url)
  base = url
  r = g(base)
  r = r.split('<a href="')
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
    if (x not in a) and (x != '#') and (x != '#start-of-content') and (x != ''):
      a.append(x)
  f = open('results.txt','w+')
  for x in a:
    f.write(x+'\n')

# Files
f = open('results.txt','w+')
f.write('')
f.close()

#Variables
a = []
d = 0#int(input('Depth: '))
visited = []
depth = 0



main(input('Start URL: '))
input('Continue? ')
ol = len(a)
for x in range(ol):
  #print(str(x)+'/'+str(ol))
  try:
    main(a[x])
  except:
    print('Error..')
print('\n\n\n\n\n\n')
print(visited)



lf = open('res_list.txt','w+')
lf.write(str(a))
lf.close()