#!/usr/bin/python

import urllib2

import web

controller_url = 'http://192.168.254.77'

urls = (
    '/', 'index',
    '/motor1', 'motor1',
    '/motor2', 'motor2',
    '/motor3', 'motor3',
)

render = web.template.render('templates')

def do_cmd(motor, dir, delay, steps):
    fi = urllib2.urlopen('%s/cmd?motor=%s&dir=%s&delay=%d&steps=%d' % (controller_url, motor, dir, delay, steps))
    ret = fi.read()
    return ret

class index:
    def GET(self):
        return render.index()

class motor1:
    def GET(self):
        try:
            ret = []
            ret.append(do_cmd('1', 'LOW', 1, 600))
            ret.append(do_cmd('1', 'HIGH', 1, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

class motor2:
    def GET(self):
        try:
            ret = []
            ret.append(do_cmd('2', 'LOW', 1, 600))
            ret.append(do_cmd('2', 'HIGH', 1, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

class motor3:
    def GET(self):
        try:
            ret = []
            ret.append(do_cmd('3', 'LOW', 5, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
