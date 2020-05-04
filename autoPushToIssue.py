import os

i = 0
while i <= 10:
	os.system('echo 1 >> log.txt')
	os.system('git add -A')
	os.system('git commit -m "first commit %s"' % (i))
	os.system('git push origin master -f')
	i = i + 1
