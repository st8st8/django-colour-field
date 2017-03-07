from django.db import models
from forms import ColourFormField


class ColourField(models.Field):
    """
    Store a colour as a CSS value (ie, #012345)

    We don't subclass models.CharField, as then the django admin would use
    it's AdminCharWidget or whatever, and we want to use our own.
    """

    # I think these can both go.
    # __metaclass__ = models.SubfieldBase
    # _south_introspects = True

    description = "A colour object"

    def get_prep_value(self, value):
        if not (value and value.strip()) and self.null:
            return None
        return value

    def value_to_string(self, value):
        if value:
            return value.strip() or None

    def formfield(self, *args, **kwargs):
        defaults = {'form_class': ColourFormField}
        defaults.update(kwargs)
        return super(ColourField, self).formfield(*args, **defaults)

    def db_type(self, connection):
        return 'char(7)'
