from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'


def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]


def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)


class ColourPickerWidget(forms.TextInput):
    """
    Widget to display a Colour Picker with js.
    """

    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        rendered = super(ColourPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(
            u"""<div id="colourpicker_%(name)s" class="colourpicker"></div>
            <script type="text/javascript">
            $(function () {
              $('#colourpicker_%(name)s').farbtastic('#id_%(name)s');
              $('#id_%(name)s').focus(function(){
              $('#colourpicker_%(name)s').show();
              });
              $('#id_%(name)s').blur(function(){
              $('#colourpicker_%(name)s').hide();
              });
              $('#colourpicker_%(name)s').hide();
            });
            </script>""" % {'name': name}
        )

    class Media:
        css = {
            'all': (settings.STATIC_URL + 'colour_field/css/farbtastic.css',)
        }

        js = (
            settings.STATIC_URL + 'colour_field/js/farbtastic.js',
        )
        
        
class PikPikColourPickerWidget(forms.TextInput):
    
    defaults = ["ff0000", "00ff00", "0000ff"]
    
    def __init__(self, defaults=None, attrs=None, renderer=None, **kwargs):
        if defaults:
            self.defaults = defaults
        super(PikPikColourPickerWidget, self).__init__(attrs, **kwargs)
        
    def render(self, name, value, attrs=None):
        rendered = super(PikPikColourPickerWidget, self).render(name, value, attrs)
        rgb_list = [rgb(x) for x in self.defaults]
        rgbs = ", ".join([' {{"r": "{0}", "g": "{1}", "b": "{2}"}}'.format(x[0], x[1], x[2]) for x in rgb_list])
        return rendered + mark_safe(
            u"""<div id="colourpicker_{0}" class="colourpicker"></div>
            <script type="text/javascript">
                jsColorPicker("input#id_{0}", {{
                    memoryColors: [{1}]
                }});
            </script>""".format(name, rgbs)
        )

    class Media:
        js = (
            settings.STATIC_URL + 'colour_field/js/colors.js',
            settings.STATIC_URL + 'colour_field/js/jsColorPicker.min.js',
            settings.STATIC_URL + 'colour_field/js/jsColor.js',
        )
