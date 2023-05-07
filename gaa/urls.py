from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('',views.index,name='index'),
    path('list/',views.list,name='list'),
    path('rp/',views.ranked_panchayats,name='list'),
    path('pd/',views.panchayat_details,name='panchayat_details'),
    path('panchayat_list/',views.panchayat_list,name='panchayat_list'),
    path('panchayat/(?P<pk>\d+)/', views.panchayat, name='panchayat'),
    path('vd/',views.vd,name='weight_change'),
    path('contact/', TemplateView.as_view(template_name='gaa/contact.html'),name='contact'),
    # path('weight_change.html/',views.,name='weight_change')
]
