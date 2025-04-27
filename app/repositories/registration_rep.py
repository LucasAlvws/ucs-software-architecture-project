from app.dao import RegistrationDao
from app.models import Registration


class RegistrationRepository:

    def __init__(self):
        self.dao = RegistrationDao()
        self.model = Registration

    def filter(self, defaults):
        return self.dao.get_by_attributes(defaults)

    def update_or_create(self, defaults):
        if _object := self.filter_unique(**defaults):
            return _object
        _object = self.model(**defaults)
        self.dao.save(_object)
        return _object

    def update_by_dataframe(self, dataframe):
        self.dao.save_dataframe(dataframe)

    def filter_unique(
        self, institution_name, institution_category, course_detailed_name, course_modality, course_degree, **_
    ):
        defaults = {
            'institution_name': institution_name,
            'institution_category': institution_category,
            'course_detailed_name': course_detailed_name,
            'course_modality': course_modality,
            'course_degree': course_degree,
        }
        return self.dao.get_by_attributes(defaults)
