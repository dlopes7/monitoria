import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

import datetime
import time

from django.utils import timezone

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from webpagetester.models import Metric

metric_id = "wpt_firstView_SpeedIndex"
m = Metric.objects.filter(metric_id = metric_id)
if len(m) == 0:
    m = Metric()
    m.name = "Speed Index"
    m.metric_id = metric_id
    m.description_enUS = """
                        The Speed Index is a calculated metric that represents
                        how quickly the page rendered the user-visible content
                        (lower is better).
                        """
    m.description_ptBR = """
                        O Speed Index é uma métrica calculada que representa
                        quão rapidamente a página desenhou o conteúdo
                        visível ao usuário (quanto menor, melhor).
                        """
    m.save()


metric_id = "wpt_firstView_bytesIn"
m = Metric.objects.filter(metric_id = metric_id)
if len(m) == 0:
    m = Metric()
    m.name = "Page Size"
    m.metric_id = metric_id
    m.description_enUS = """
                        Number of bytes transferred to the browser while
                        the page is loaded
                        """
    m.description_ptBR = """
                        Número de bytes transferidos ao navegador enquanto
                        a página é carregada
                        """
    m.save()
