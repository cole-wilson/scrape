def main():
  ml = int(input('Minimum required length of words.'))
  f = open('results','r+')

  a = f.read().split('\n')

  c = []

  import requests, re

  div = 1


  import re
  def special_match(strg, search=re.compile(r'[^a-z0-9.]')  .search):
    return not bool(search(strg))

  print('Total: ' + str(round(len(a)/div)))

  for x in range(round(len(a)/div)):
    print(x)
    #print(a[x])
    if a[x] != '':
      b = str(requests.get(a[x]).content).replace('b\'','') .replace('\\n','\n')
    else:
      b= ''
    nonos = ['px','~','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','{','}','|','\\','\'','"',';',':','/','?','.','>',',']
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

  print(maxlen)