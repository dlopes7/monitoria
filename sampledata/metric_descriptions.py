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
m = Metric.objects.get(metric_id = metric_id)
if m is None:
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
m = Metric.objects.get(metric_id = metric_id)
if m is None:
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

metric_id = "wpt_firstView_requests"
m = Metric.objects.get(metric_id = metric_id)
if m is None:
    m = Metric()
m.name = "Requests"
m.metric_id = metric_id
m.description_enUS = """
                    Number of requests that had to be made by the browser
                    for pieces of content on the page (images, javascript, css, etc).
                    """
m.description_ptBR = """
                    Número de requisições que foram feitas pelo navegador
                    para obter todo o conteúdo da página (imagens, javascript, css, etc)
                    """
m.save()

metric_id = "wpt_firstView_breakdown_image_bytes"
m = Metric.objects.get(metric_id = metric_id)
if m is None:
    m = Metric()
m.name = "Image Bytes"
m.metric_id = metric_id
m.description_enUS = """
                    Number of bytes the browser had to download for
                    files of the image type
                    """
m.description_ptBR = """
                    Número de bytes de Imagens baixados pelo navegador
                    """
m.save()

metric_id = "wpt_firstView_breakdown_css_bytes"
m = Metric.objects.get(metric_id = metric_id)
if m is None:
    m = Metric()
m.name = "CSS Bytes"
m.metric_id = metric_id
m.description_enUS = """
                    Number of bytes the browser had to download for
                    files of the CSS type
                    """
m.description_ptBR = """
                    Número de bytes de CSS baixados pelo navegador
                    """
m.save()

metric_id = "wpt_firstView_breakdown_js_bytes"
m = Metric.objects.get(metric_id = metric_id)
if m is None:
    m = Metric()
m.name = "Javascript Bytes"
m.metric_id = metric_id
m.description_enUS = """
                    Number of bytes the browser had to download for
                    files of the Javascript type
                    """
m.description_ptBR = """
                    Número de bytes de arquivos Javascript baixados pelo navegador
                    """
m.save()

