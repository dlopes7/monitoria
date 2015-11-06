from django.utils.safestring import mark_safe

import django_tables2 as tables

from webpagetester.models import Test

from webpagetester.utils import ms_to_sec, size

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name

class TestTable(tables.Table):
    selection = CheckBoxColumnWithName(accessor='pk', orderable=False, verbose_name='C')
    update = tables.TemplateColumn(verbose_name= ('Update'),
                                    template_name='small/update.html',
                                    sortable=False,
                                    accessor='pk')

    wpt_firstView_TTFB = tables.Column(verbose_name='First Byte')
    wpt_firstView_SpeedIndex = tables.Column(verbose_name='Speed Index')
    wpt_location = tables.Column(verbose_name='Location')
    wpt_status_code = tables.Column(verbose_name='Status')
    wpt_status_text = tables.Column(verbose_name='Description')
    wpt_firstView_breakdown_css_bytes  = tables.Column(verbose_name='CSS')
    wpt_firstView_breakdown_flash_bytes  = tables.Column(verbose_name='Flash')
    wpt_firstView_breakdown_html_bytes  = tables.Column(verbose_name='HTML')
    wpt_firstView_breakdown_image_bytes  = tables.Column(verbose_name='IMG')
    wpt_firstView_breakdown_js_bytes  = tables.Column(verbose_name='Js')
    wpt_firstView_breakdown_other_bytes  = tables.Column(verbose_name='Other')
    wpt_userUrl = tables.Column(verbose_name='Link')
    url = tables.Column(verbose_name='Url')
    created_date = tables.Column(verbose_name='Data')
    label = tables.Column(verbose_name='Name')

    def render_wpt_userUrl(self, value):
        return mark_safe('<a href="{link}" target="_blank">open</a>'.format(link=value))

    def render_wpt_firstView_TTFB(self, value):
        return '{sec:.2f}s'.format(sec=ms_to_sec(value))

    def render_wpt_firstView_SpeedIndex(self, value):
        return '{sec:.2f}s'.format(sec=ms_to_sec(value))

    def render_wpt_firstView_breakdown_css_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    def render_wpt_firstView_breakdown_flash_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    def render_wpt_firstView_breakdown_html_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    def render_wpt_firstView_breakdown_image_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    def render_wpt_firstView_breakdown_js_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    def render_wpt_firstView_breakdown_other_bytes(self, value):
        return '{tamanho}'.format(tamanho=size(value))

    class Meta:
        model = Test

        attrs = {'class': 'dark',
                 'id': 'alerts_table'}

        fields = (
                  'selection',
                  'id',
                  'label',
                  'url',
                  'wpt_userUrl',
                  'created_date',
                  'wpt_status_code',
                  'wpt_status_text',
                  'wpt_location',
                  'wpt_firstView_SpeedIndex',
                  'wpt_firstView_TTFB',
                  'wpt_firstView_breakdown_css_bytes',
                  'wpt_firstView_breakdown_flash_bytes',
                  'wpt_firstView_breakdown_html_bytes',
                  'wpt_firstView_breakdown_image_bytes',
                  'wpt_firstView_breakdown_js_bytes',
                  'wpt_firstView_breakdown_other_bytes',
                  )

        order_by = '-id'
