from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name='ecomapp'
urlpatterns = [

    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='procatdetail')
]

