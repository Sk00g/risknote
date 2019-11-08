

class Skraper:
    def __init__(self, dev_mode=True):
        self._data = ""
        self._dev_mode = dev_mode

    def set_data(self, data):
        self._data = data

        if self._dev_mode:
            print('*SKRAPER* - Added new data: %d lines, %d characters' % (len(data.split('\n')), len(data)))

    def get_indices_within(self, pre, after, snippet=None):
        data = snippet if snippet else self._data

        indices = []

        scan = data.find(pre)

        while scan != -1:
            rlimit = data.find(after, scan)
            if rlimit == -1:
                break
            indices.append((scan + len(pre), rlimit))
            scan = data.find(pre, rlimit + len(after))

        print('*SKRAPER* - Found %d values between %s and %s' % (len(indices), pre, after))

        return indices

    def get_values_within(self, pre, after, start_index=0, end_index=-1, snippet=None):
        data = snippet if snippet else self._data

        end_index = len(data) if end_index == -1 else end_index

        values = []

        scan = data.find(pre, start_index)

        while scan != -1 and scan < end_index:
            rlimit = data.find(after, scan)
            values.append(data[scan + len(pre):rlimit])
            scan = data.find(pre, rlimit + len(after))

        print('*SKRAPER* - Found %d values between %s and %s' % (len(values), pre, after))

        return values

