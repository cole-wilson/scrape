









bu = 'https://google.com/'






















import requests, re, time
sleep = 0.1

au = []
errors = []
words = ''

tab = 0
maxdepth = int(input('What should the maximum length be?'))#1
amo = 0
class Page:
  def __init__(self, url):
    global amo
    amo = amo + 1
    try:
      tmp = str(requests.get(url).content)
      tmp = tmp.replace('b\'','').replace('\\n','\n')
    except:
      print('error.')
      tmp = ''
    self.content = tmp
    self.url = url
    del tmp
    try:
      self.domain = 'https://' + re.findall('(?<=://)(.*)(?=/)',url)[0]
    except IndexError:
      self.domain = url
      errors.append(url)
      
      
    
def tabify():
  global tab
  c = ''
  if True:
    for x in range(tab):
      c = c + '|  '
    
  return c
w = open('urls','w+')
f = open('words','w+')
def main(base):
  global tab
  global words
  global au
  global maxdepth
  global w
  global f
  global sleep
  if tab > maxdepth:
    return
  p = Page(base).content
  domain = Page(base).domain
  urls = []
  for x in p.split('href="'):
    c = ''
    for y in x:
      if y == '"':
        urls.append(c)
        break
      else:
        c = c + y
  fi  = []
  for x in re.findall('>.*?<',p):
    words = words + ' ' + x.replace('>','').replace('<','')
  for y in urls:
    try:
      x = re.findall('(?<=)(.*)(?=\?)',y)[0]
    except:
      x = y
    if x not in au:
      if x == '':
        continue
      elif x[0] == '.':
        continue
      elif x[0:2] == '//':
        fi.append('https:' + x)
      elif x[0] == '/':
        fi.append(domain + x)
      elif x[0:2] == 'ht':
        fi.append(x)
      elif x[0] == '<':
        continue
      else:
        fi.append(base + x)
  #print(fi)
  for x in fi:
    au.append(x)
  for x in range(len(fi)):
    if tab == 0:
      if x+1 == len(fi):
        print('└──' + str(x+1) + '/' + str(len(fi)))
        w.write('└──' + fi[x] + '\n')
      else:
        print('├──' + str(x+1) + '/' + str(len(fi)))
        w.write('├──' + fi[x] + '\n')
    elif x+1 != len(fi):
      print(tabify() + '├──' + str(x+1) + '/' + str(len(fi)))
      w.write(tabify() + '├──' + fi[x] + '\n')
    else:
      print(tabify() + '└──' + str(x+1) + '/' + str(len(fi)))
      w.write(tabify() + '└──' + fi[x] + '\n')
      
    time.sleep(sleep)
    w.write(tabify() + fi[x] + '\n')
    tab = tab + 1
    try:
      main(fi[x])
    except KeyboardInterrupt:
      print('user abort')
    tab = tab - 1
    
goodwords = []
totals = {}
fl = []




print(bu)
w.write(bu + '\n')
main(bu)



for x in words.split():
  if not re.search('[/,_,;,\\,\',\=,\[\],0-9,!@#$%^&*(),.?":{}|<>,\-]',x):
    goodwords.append(x.lower())

for x in goodwords:
  totals[x] = 0
for x in goodwords:
  totals[x] = totals[x] + 1
#print(totals)
ml = 0
for x in totals.keys():
  if (len(str(int(totals[x])))) > ml:
    ml = len(str(int(totals[x])))
#print(ml)





for x in totals.keys():
  tb = ''
  for y in range(ml-len(str(totals[x]))):
    tb = tb + '0'
  tb = tb + str(totals[str(x)]) + '     ' + str(x)
  fl.append(tb)
fl.sort(reverse=True)
#print(fl)
for x in fl:
  f.write(x + '\n')

print('\n\n\n\n\n\n\n\n\nCollected about ' + str(amo) + ' pages, at depth ' + str(maxdepth) + '. The base url was ' + bu + '.')
if len(errors) != 0:
  print('\nSome errors occured: ' + str(errors))
else:
  print('\nNo errors occured.')

f.close()
w.close()