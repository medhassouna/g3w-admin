# coding=utf-8
""""

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2020-09-15'
__copyright__ = 'Copyright 2015 - 2020, Gis3w'

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import QplotlyLinkWidget2LayerView, QplotlyDownloadView, QplotlyWidgetShowOnStartClientView

urlpatterns = [
    path('layer/<int:layer_pk>/widgets/link/<int:pk>/',
        login_required(QplotlyLinkWidget2LayerView.as_view()), name='qplotly-project-layer-widget-link'),
    path('showonstartclient/<int:pk>/',
        login_required(QplotlyWidgetShowOnStartClientView.as_view()),
        name='qplotly-project-layer-widget-showonstartclient'),
    path('download/xml/<int:pk>/', login_required(QplotlyDownloadView.as_view()),
        name='qplotly-download-xml')
]