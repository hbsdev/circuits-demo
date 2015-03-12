"""
Simple Demo Service

1) Runs a webserver, so the monitoring service 
   can try TCP Port 80 to check if it is alive.

2) Writes its pid as soon as it starts, so
   it can be restarted from the monitoring service.

3) Includes timer demos that write to the console.

4) There is a simulated exception to show that all 
   other timer events continue.
"""


import helpers
import myhttp


from circuits import Event, Component, Timer

class App(Component):

    def hello(self):
        print("Hello World")

    def simulate_exception(self):
        print("simulate exception before")
        1/0
        print("simulate exception after")

    def foo(self):
        print("this is foo")

    def bar(self):
        print("this is bar")

    def started(self, component):
        # Timer(seconds, event, persist=False)
        Timer(4, Event.create("simulate_exception")).register(self)
        Timer(5, Event.create("hello")).register(self)
        Timer(1, Event.create("foo"), persist=True).register(self)
        Timer(3, Event.create("bar"), persist=True).register(self)

if __name__ == "__main__":
    helpers.write_pid_file()
    import conf
    Webserver = myhttp.register_webserver(conf.sync.INTERFACE, conf.sync.PORT)
    (App() + Webserver).run()
