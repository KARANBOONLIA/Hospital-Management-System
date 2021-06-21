from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'indexOFpats'),
    path('<int:no>/', views.details, name='details'),
    path('<int:no>/book/', views.book , name='book'),
    path('add/',views.PatientCreate.as_view(),name='add'),
    path('<int:pk>/update',views.PatientUpdate.as_view(),name='update'),
    path('<int:pk>/del',views.PatientDelete.as_view(),name='delete')

]