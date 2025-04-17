from abc import abstractmethod
class BaseRepository:
    def filter(self, defaults):
        return self.dao.get_by_attributes(defaults)

    def update_or_create(self, defaults):
        if _object := self.filter_unique(**defaults):
            return _object
        _object = self.model(**defaults)
        self.dao.save(_object)
        return _object

    @abstractmethod
    def filter_unique(self):
        pass