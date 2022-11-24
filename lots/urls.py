

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lot_list),
    path('<int:id>', views.lot_detail),

]
