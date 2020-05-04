import os, random

i = 10
while i <= 20:
	os.system('echo 1 >> '+str(random.randrange(2,1000,2))+'.txt')
	os.system('git add -A')
	os.system('git commit -m "first commit %s"' % (i))
	os.system('git push origin master -f')
	i = i + 1
