# scratching of Finite Status Machine.


class FSM:
    _event_to_status = {}
    _end_status = []
    _start_status = None
    _current_status = None
    
    def add_status(self, status, event, end_status=False):
        self._event_to_status[event] = status
        if end_status:
            self._end_status.append(status)
    
    def set_status(self, status):
        self._current_status = status
    
    def set_start(self, status):
        self._start_status = status
    
    def run(self):
        while True:
            if not self._start_status:
                print("No start status set!")
                break
            else:
                event = input('input event: ')
                if self._event_to_status.get(event, False):
                    self.set_status(self._event_to_status[event])
                else:
                    print('event not defined, ignored.')
            self.status()
            if self._current_status in self._end_status:
                print('reached end status, exit.')
                break
    
    def status(self):
        print(f'current status is {self._current_status}')


f = FSM()
f.add_status('Turned On', 'lit')
f.add_status('Turned Off', 'shut')
f.add_status('Broken', 'shoot', end_status=True)

f.set_start('Turned Off')
f.run()
