"""
SimulatorView:
    Base class of container of all views. This is a runnable class.
"""

class SimulatorView:
    def __init__(self):
        self.views = []
    def add(self, obj):
        self.views.append(obj)
    def run(self):
        pass

class SimulatorTextView:
    def __init__(self):
        SimulatorView(self)
        self.buffer = ""
    def run(self):
        self.buffer = ""
        for obj in self.views:
            self.buffer += "%s\n" % obj.run()
        print(self.buffer)
