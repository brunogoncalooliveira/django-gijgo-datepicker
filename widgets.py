# -*- coding: utf-8 -*-
#from django import forms
from django.forms.utils import flatatt
from django.forms.widgets import DateTimeInput
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text

from pprint import pprint

class DatePicker(DateTimeInput):
    class Media:
        css = {'all': ('gijgo/combined/css/gijgo.min.css',),}
        js = ('gijgo/combined/js/gijgo.min.js',)

    html_template = """
     <input%(initattrs)s%(attrs)s name="%(name)s" value="%(value)s"/>
     """

    js_template = '''
 <script>
     $('#%(id)s').datepicker(%(options)s);
 </script>
'''

    def __init__(self, attrs=None, format=None, options=None, div_attrs=None, icon_attrs=None):
        super(DatePicker, self).__init__(attrs, format)
        self.options = options
        if attrs == None:
            self.attrs = {}
        else:
            self.attrs = attrs


    def render(self, name, value, attrs=None):
        print("attrs['id']")
        pprint(attrs)
        pprint(name)
        pprint(value)
        html = self.html_template % dict(attrs=flatatt(attrs), initattrs=flatatt(self.attrs), value=value, name=name)
        js = self.js_template % dict(id=attrs['id'], options=self.options)

        return mark_safe(force_text(html + js))
