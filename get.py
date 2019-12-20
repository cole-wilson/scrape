import config

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
  r = g(base)
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

def l():
  ml = int(input('Minimum required length of words.'))
  f = open('results','r+')

  a = f.read().split('\n')

  c = []

  import requests, re

  #print('Total: ' + str(round(len(a)/div)))

  for x in range(len(a)):
    print(str(x) + '/' + str(len(a)))
    #print(a[x])
    if a[x] != '':
      b = str(requests.get(a[x]).content).replace('b\'','') .replace('\\n','\n')
    else:
      b= ''
    nonos = ['0','1','2','3','4','5','6','7','8','9','px','~','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','{','}','|','\\','\'','"',';',':','/','?','.','>',',']
    for x in re.findall('>(.*?)<',b):
      if x != '':
        cs = x.split(' ')
        for z in cs:
          br = True
          if (not z.lower().isnumeric())and(len(z)>=ml):
            for d in nonos:
              if d in z:
                br = False
            if br:
              c.append(z.lower())
      #else:
        #print('Space..')


  final = []

  for x in c:
    if x != '':
      final.append(x)
  #print(len(final))

  d = {}

  for x in final:
    d[x] = 0

  for x in final:
    d[x] = d[x] + 1

  #print(d)

  te = 0

  h = []
  for x in d.keys():
    h.insert(0, x)
    te = te + 1
    #print(te)


  maxlen = 0

  nh = []
  for x in range(len(h)):
    if len(str(d[h[x]])) > maxlen:
      maxlen = len(str(d[h[x]]))

  for x in range(len(h)):
    st = ''
    for y in range(maxlen-len(str(d[h[x]]))):
      st = st + '0'
    nh.append(st + str(d[h[x]]) + '   :   ' + h[x])
  print('\n\n\n\n\n\n\n\n\n\n\n')



  h = sorted(nh,reverse=True)
  l = open('words','w+')
  for x in range(len(h)):
    l.write(h[x] + '\n')
  l.close()

  #print(maxlen)

import requests

def g(url):
  try:
    r = requests.get(url)
    r = str(r.content).replace('\\n','\n')  .replace('\\t','\t')
    return(r)
  except:
    return('')

def rank():
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

import os
def post():
  try:
    os.system('cp words '  + config.dir_base_path + '/words.txt')
    os.system('echo "' + config.html_start + str(open('words','r+').read()).split('   :   ')[1].split('\n')[0] + config.html_start + '" > ' + config.dir_base_path + '/index.html')
  except:
    print('There was an error, so I didn\'t continue;')