from mockfirestore.collection import CollectionReference
from mockfirestore.batch import BatchReference

class MockFirestore:

    def __init__(self) -> None:
        self._data = {}

    def collection(self, name: str) -> CollectionReference:
        if name not in self._data:
            self._data[name] = {}
        return CollectionReference(self._data, [name])

    def reset(self):
        self._data = {}

    def batch(self) -> BatchReference:
        return BatchReference()


