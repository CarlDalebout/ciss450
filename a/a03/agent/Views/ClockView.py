from ObjectView import ObjectView

class ClockView(ObjectView):
    def __init__(self, clock):
        ObjectView.__init__(self, clock)

class ClockTextView(ClockView):
    def __init__(self, clock):
        ClockView.__init__(self, clock)
    def run(self):
        # Newline added to string
        return "\nclock      : %s" % self.object.time

class ClockGUIView(ClockView):
    def __init__(self, clock):
        ClockView.__init__(self, clock)
    def run(self):
        # Need access to pygame surface
        # Need to specify drawing position, font size, color, etc.
        # Maybe have a GUIText subclass for drawing text
        pass
        
    
