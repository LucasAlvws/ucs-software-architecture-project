class BaseRepository:
    def filter(self, defaults):
        from IPython import embed;embed(header='asdasd')
        return self.dao.get_by_attributes(defaults)

    def update_or_create(self, defaults):
        if _object := self.filter(defaults):
            return _object
        _object = self.model(**defaults)
        self.dao.save(_object)
        return _object
