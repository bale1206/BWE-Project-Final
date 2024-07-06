from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('explorer', views.explorer, name='explorer'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('plans', views.plans, name='plans'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('usr', views.usr, name='usr'), #ingresar al crud de la pagina usando /usr
]


