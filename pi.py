#!/usr/bin/python

import time

import web

import RPi.GPIO as GPIO

pins = [
    (24, 25),
    (8, 7),
    (4, 17),
]

urls = (
    '/', 'index',
    '/motor1', 'motor1',
    '/motor2', 'motor2',
    '/motor3', 'motor3',
)

render = web.template.render('templates')

class StepperMotorsController:
    def __init__(self):
        pass

    def init(self):
        GPIO.setmode(GPIO.BCM)

        for step_pin, dir_pin in pins:
            GPIO.setup(step_pin, GPIO.OUT)
            GPIO.output(step_pin, GPIO.LOW)
            GPIO.setup(dir_pin, GPIO.OUT)
            GPIO.output(dir_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

    def do_cmd(self, motor, dir, delay, steps):
        step_pin, dir_pin = pins[int(motor)-1]
        if dir == 'HIGH':
            GPIO.output(dir_pin, GPIO.HIGH)
        else:
            GPIO.output(dir_pin, GPIO.LOW)

        for i in range(steps):
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(delay/1000.0)
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(delay/1000.0)

        return 'command: motor=%(motor)s dir=%(dir)s delay=%(delay)d steps=%(steps)d' % locals()

class index:
    def GET(self):
        return render.index()

class motor1:
    def GET(self):
        req = web.input(q='1')
        q = int(req.q)
        try:
            ret = []
            for i in range(q):
                ret.append(motors.do_cmd('1', 'LOW', 1, 600))
                ret.append(motors.do_cmd('1', 'HIGH', 1, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

class motor2:
    def GET(self):
        req = web.input(q='1')
        q = int(req.q)
        try:
            ret = []
            for i in range(q):
                ret.append(motors.do_cmd('2', 'LOW', 1, 600))
                ret.append(motors.do_cmd('2', 'HIGH', 1, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

class motor3:
    def GET(self):
        try:
            ret = []
            ret.append(motors.do_cmd('3', 'LOW', 5, 600))
            return '<br>'.join(ret)
        except Exception, why:
            return str(why).replace('<', '&lt;').replace('>', '&gt;')

motors = StepperMotorsController()
motors.init()

if __name__ == "__main__":
    app = web.application(urls, globals())
    try:
        app.run()
    finally:
        motors.cleanup()
