# scratching of Finite Status Machine.


# class FSM:
#     _event_to_status = {}
#     _end_status = []
#     _start_status = None
#     _current_status = None
    
#     def add_status(self, status, event, end_status=False):
#         self._event_to_status[event] = status
#         if end_status:
#             self._end_status.append(status)
    
#     def set_status(self, status):
#         self._current_status = status
    
#     def set_start(self, status):
#         self._start_status = status
    
#     def run(self):
#         while True:
#             if not self._start_status:
#                 print("No start status set!")
#                 break
#             else:
#                 event = input('input event: ')
#                 if self._event_to_status.get(event, False):
#                     self.set_status(self._event_to_status[event])
#                 else:
#                     print('event not defined, ignored.')
#             self.status()
#             if self._current_status in self._end_status:
#                 print('reached end status, exit.')
#                 break
    
#     def status(self):
#         print(f'current status is {self._current_status}')


# f = FSM()
# f.add_status('Turned On', 'lit')
# f.add_status('Turned Off', 'shut')
# f.add_status('Broken', 'shoot', end_status=True)

# f.set_start('Turned Off')
# f.run()


from types import MethodType


class Status:
    def __init__(self, name, behavior) -> None:
        self._name = name
        self.behavior = MethodType(behavior, self)
    
    def enter(self, FSM, event):
        print('because of event:', event)
        print(FSM.name, "entered status", self._name)
    
    def exit(self, FSM, event):
        print('because of event:', event)
        print(FSM.name, 'exited status', self._name)


class FSM:
    _event_status = {}
    
    def __init__(self, name, init_status) -> None:
        self.name = name
        self._status = init_status
        self._current_event = None

    def add_status(self, event, status: Status):
        self._event_status[event] = status
    
    def update(self, event):
        if event in self._event_status:
            self._status.exit(self, event)
            
            self._current_event = event
            self._status = self._event_status[event]
            self._status.enter(self, event)
        else:
            print('undefined event, ignored.')
    
    # this behave is actually using staticmethod, self is passed explicitly.
    # there could be a way that you bound method by using MethodType.
    def behave(self):
        self._status.behavior(self, self._current_event)
            

def sleep(self, FSM, event):
    print(FSM.name, 'is dreaming caused by', event)


def work(self, FSM, event):
    print(FSM.name, 'is working because of', event)


class Awake(Status):
    pass


class Sleeping(Status):
    pass


f = FSM('宫哥', Awake('清醒', work))

f.add_status('老板电话', Awake('清醒', work))
f.add_status('老板走了', Sleeping('睡眠', sleep))

print('====== 开始 ======')
f.behave()
print('====== 事件 ======')
f.update('老板走了')
f.behave()
print('====== 事件 ======')
f.update('老板电话')
f.behave()

