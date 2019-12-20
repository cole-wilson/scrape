import config, rank, get, l, git

if config.moz:
  rank.main()
c = 0
for x in open('top','r+').read().split('\n'):
  c = c + 1
  print('Getting ' + x + ' (' + str(c) + '/' + str(len(open('top','r+').read().split('\n'))-1) + ')')
  get.main(x)
  m = open('all','w+')
  m.write(m.read()+'\n\n===\n\n'+open('results','r').read())



l.main()

git.main()