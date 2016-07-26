import gevent


class MyNoopGreenlet(gevent.Greenlet):

    def __init__(self, seconds):
        gevent.Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        gevent.sleep(self.seconds)

    def __str__(self):
        return 'MyNoopGreenlet(%s)' % self.seconds

g = MyNoopGreenlet(4)
g.start()
g.kill()
print(g.dead)

print(gevent.__version__)