class EventList:
    __EventList = []

    @classmethod
    def add(cls, event):
        cls.__EventList.append(event)

    @classmethod
    def remove(cls, event):
        cls.__EventList.remove(event)

    @classmethod
    def checkEvent(cls, event):
        for e in cls.__EventList:
            e.event(event)

