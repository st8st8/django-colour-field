from django.db import models
from forms import ColourPickerFormField
import re

class ColourPickerField(models.Field):
    """
    Store a colour as a CSS value (ie, #012345)
    
    We don't subclass models.CharField, as then the django admin would use
    it's AdminCharWidget or whatever, and we want to use our own.
    """
    
    __metaclass__ = models.SubfieldBase
    _south_introspects = True
    
    description = "A colour object"
    
    def to_python(self, value):
        # assert value[0] == "#" 
        # assert re.match('#[0-9a-fA-F]{6}', value)
        return value
    
    def formfield(self, *args, **kwargs):
        defaults = {'form_class': ColourPickerFormField}
        defaults.update(kwargs)
        return super(ColourPickerField, self).formfield(*args, **defaults)
    
    def db_type(self, connection):
        return 'char(7)'