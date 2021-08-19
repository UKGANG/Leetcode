'''
Convert Production Schedule
'''


class Task:
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        self.sub_task = []


def convert_schedule(compressed):
    # Write your code here
    # compressed = unicode(compressed, 'utf-8')
    curr = root = Task(1, None)
    n = []
    for c in compressed:
        if c.isnumeric():
            n.append(c)
        elif '[' == c:
            curr.sub_task.append(Task(int(''.join(n)), curr))
            curr = curr.sub_task[-1]
            n.clear()
        elif ']' == c:
            task = ''.join(curr.sub_task)
            task = task * curr.n
            curr.parent.sub_task[-1] = task
            curr = curr.parent
            n.clear()
        else:
            curr.sub_task.append(c)
    return ''.join(root.sub_task)