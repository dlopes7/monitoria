import django_tables2 as tables
from webpagetester.models import Test

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

    class Meta:
        model = Test

        attrs = {'class': 'paleblue', 'id': 'alerts_table'}
        fields = ('selection', 'id', 'label', 'created_date', 'wpt_status_code','wpt_status_text', 'wpt_location','wpt_firstView_SpeedIndex','wpt_firstView_TTFB','wpt_firstView_bytesIn')
        #sequence = ("selection", "label", "wpt_status_code")
