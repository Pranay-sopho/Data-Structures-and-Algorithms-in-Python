class Range:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._start = start
        self._step = step