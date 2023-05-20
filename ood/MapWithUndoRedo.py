"""
Map with Undo Redo
"""


class UndoRedoMap:
    def __init__(self):
        self._map = {}
        self._undo_stack = []
        self._redo_stack = []

        self.set = self.log(self.set)
        self.delete = self.log(self.delete)

    def get(self, key):
        return self._map.get(key, None)

    def set(self, key, val):
        self._map[key] = val

    def delete(self, key):
        del self._map[key]

    def log(self, func):
        def wrapper(*args, **kwargs):
            key = args[0]
            prev_val, prev_exists = None, False
            if key in self._map:
                prev_val, prev_exists = self._map[key], True

            self._undo_stack.append((prev_val, prev_exists, key))
            self._redo_stack.clear()
            return func(*args, **kwargs)

        return wrapper

    def _replay(self, src_stack, target_stack):
        if not src_stack:
            return
        src_val, src_exists, key = src_stack.pop()
        target_val, target_exists = None, False
        if key in self._map:
            target_val, target_exists = self._map[key], True
        target_stack.append((target_val, target_exists, key))
        if not src_exists:
            del self._map[key]
        else:
            self._map[key] = src_val

    def undo(self):
        self._replay(self._undo_stack, self._redo_stack)

    def redo(self):
        self._replay(self._redo_stack, self._undo_stack)


customized_map = UndoRedoMap()
customized_map.set(1, 3)
customized_map.set(2, 3)
customized_map.undo()
print(customized_map.get(2))
customized_map.delete(1)
customized_map.redo()
print(customized_map.get(2))
