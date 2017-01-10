import gevent
from gevent import getcurrent
from gevent.pool import Group

group = Group()

def hello_from(n):
	print('Size of group {0}'.format(len(group)))
	print('Hello from greenlet id: {0}'.format(id(getcurrent())))
	print('task'+ str(n) )

def intensive(n):
	gevent.sleep(3 - n)
	return 'task', n

def main():
	
	group.map(hello_from, range(3))
	
	print('Ordered')
	ogroup = Group()
	for i in ogroup.imap(intensive, range(3)):
		print(i)
	
	print('Unordered')
	igroup = Group()
	for i in igroup.imap_unordered(intensive, range(3)):
		print(i)
	

if __name__ == '__main__': main()
