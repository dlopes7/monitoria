import django_tables2 as tables
from webpagetester.models import Test

class TestTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    class Meta:
        model = Test

        attrs = {"class": "paleblue"}
        sequence = ("selection", "label", "wpt_status_code")