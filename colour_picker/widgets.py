from django import forms
import staticmedia
from django.utils.safestring import mark_safe

class ColourPickerWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        rendered = super(ColourPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<div id="colourpicker_%s" class="colourpicker"></div>
                    <script type="text/javascript">
                    $('#colourpicker_%s').farbtastic('#id_%s');
                    $('#id_%s').focus(function(){
                        $('#colourpicker_%s').show();
                    });
                    $('#id_%s').blur(function(){
                        $('#colourpicker_%s').hide();
                    });
                    $('#colourpicker_%s').hide();
                    </script>''' % (name, name, name, name, name, name, name, name))
        
    class Media:
        css = {
            'all': (staticmedia.url('farbtastic.css'),)
        }
        js = (
            staticmedia.url('jquery.js'),
            staticmedia.url('farbtastic.js'),
        )