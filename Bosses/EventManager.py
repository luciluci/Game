#EventHook manages each type of event being used.
#It plays the role of an event Observer, it triggers specific events to theyr registered callbacks

class EventHook(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def clearObjectHandlers(self, inObject):
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler

#Broadcaster manages all EventHook needed, it has one member for each event type
class Broadcaster:
    def __init__(self):
        self.on_click = EventHook()
        self.on_screen_change = EventHook()
        self.on_key_press = EventHook()

def myFunction():
    print "test"

if __name__ == "__main__":
    theBroadcaster = Broadcaster()

    # add a listener to the event
    theBroadcaster.on_click += myFunction

    # fire event
    theBroadcaster.on_click.fire()

    # remove listener from the event
    theBroadcaster.on_click -= myFunction
