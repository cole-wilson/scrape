bi = input('URL:   https://')

import requests, re, time, sys, os, calendar
startime = calendar.timegm(time.gmtime())

if bi[len(bi)-1] != '/':
  print(' -  Apended Leading Slash to URL\n')
  bi = bi + '/'
bu = 'https://' + bi

sleep = 0
sizes = []
nnn = bi
upp = []
au = []
errors = []
words = ''
fc = open('fc','w+')
fc.write('```mermaid\ngraph LR\n')
subs = {}
tab = 0
maxdepth = int(input('What should the maximum depth be?'))-1#1
amo = 0
class Page:
  def __init__(self, url):
    global amo
    try:
      tmp = str(requests.get(url).content)
      tmp = tmp.replace('b\'','').replace('\\n','\n')
    except requests.exceptions.SSLError:
      tmp = str(requests.get(url.replace('https','http')).content)
      tmp = tmp.replace('b\'','').replace('\\n','\n')
    except:
      #print('error.')
      print(sys.exc_info()[0])
      tmp = ''
    open('tempfile','w+').write(tmp)
    self.size = os.path.getsize('tempfile')
    #sizes.append(self.size)
    self.content = tmp
    self.url = url
    try:
      self.title = re.findall('(?<=<title>)(.*)(?=<\/title>)',self.content)[0]
    except:
      self.title = self.url[0:20]
    del tmp
    try:
      self.domain = 'https://' + re.findall('(?<=://)(.*)(?=/)',url)[0]
    except IndexError:
      self.domain = url
      #errors.append(url)    
def tabify():
  global tab
  c = ''
  if True:
    for x in range(tab):
      c = c + '|   '
    
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
  global fc
  global sleep
  global amo
  p = Page(base).content
  amo = amo + 1
  sizes.append(Page(base).size)
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
  upp.append(len(urls))
  for y in urls:
    try:
      x = re.findall('(?<=)(.*)(?=\?)',y)[0]
    except:
      x = y
    if x not in au:
      if x == '':
        continue
      elif ('<' in x) or ('>' in x):
        continue
      elif x[0] == '.':
        continue
      elif x[0:2] == '//':
        fi.append('https:' + x)
      elif x[0] == '/':
        fi.append(domain + '/' + x)
      elif x[0:2] == 'ht':
        fi.append(x)
      elif x[0] == '<':
        continue
      elif x[0] == ' ':
        continue
      else:
        fi.append(base + '/' + x)
  #print(fi)
  for x in range(len(fi)):
    try:
      if fi[x][0] != 'h':
        del fi[x]
      if ('{' in fi[x])or('}' in fi[x]):
        del fi[x]

    except:
      print(end='')
    au.append(x)
  if tab < maxdepth+1:
    for x in range(len(fi)):
      #print(amo)
      try:
        subs[tab].append('' + fi[x] + '' + '\n')
      except KeyError:
        subs[tab] = []
        subs[tab].append('' + fi[x] + '' + '\n')
      fc.write('' + Page(base).url + '-->' + fi[x] + '\n')
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

print('\n\n\n\n\n\n\n\n\Gathered about ' + str(amo) + ' pages, at depth ' + str(1) + '. The base url was ' + bu + '.')
if len(errors) != 0:
  print('\nSome errors occured: ' + str(errors))
else:
  print('\nNo errors occured.')

fc.write('subgraph Depth 0\n' + bu + '\nend\n')

for x in subs.keys():
  fc.write('subgraph Depth ' + str(x+1) + '\n')
  for z in subs[x]:
    fc.write(z + '')
  fc.write('end\n')

fc.write('```')
fc.close()
f.close()
w.close()
os.chdir('/home/runner/scrape-2/')

#print('Flowchart File Size: {} bytes'.format(os.path.getsize('fc')))
#print('Words Ranking Size: {} bytes'.format(os.path.getsize('words')))
#print('URLS List Size: {} bytes'.format(os.path.getsize('urls')))
#print(sizes)
s = 0
for x in sizes:
  s = s + x
print('Average webpage size in bytes: {}'.format(s/len(sizes)))
g = 0
for x in upp:
  g = g + x
print('Average URLS per page: {}'.format(g/len(upp)))

endtime = calendar.timegm(time.gmtime())

open('meta','w+').write('Base URL: ' + bi + '\nTime: ' + str(endtime-startime) + ' seconds\n' + str(len(errors)) + ' errors\nDepth: ' + str(maxdepth+2) + '\n# of Pages: ' + str(amo) + '\nAverage URLS per Page: ' + str(g/len(sizes)) + '\nAverage Page Size: ' + str(s/len(sizes)) + ' bytes\n' + 'Flowchart File Size: {} bytes\n'.format(os.path.getsize('fc')) + 'Word Ranking File Size: {} bytes\n'.format(os.path.getsize('words')) + 'URLS List File Size: {} bytes\n'.format(os.path.getsize('urls')))
os.system('tar cf ' + nnn.replace('.','_').replace('/','-') + '.scrap fc meta urls tempfile words')

input('Press enter to clear temporary files.')
os.system('rm fc meta urls words')