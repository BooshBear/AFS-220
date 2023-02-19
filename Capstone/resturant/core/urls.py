from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.urls import path 


from order.views import add_to_order, order, hx_menu_order, update_order
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name="browser"),
    path('order/', order, name='order'),
    path('add_to_order/<int:meal_id>/', add_to_order, name='add_to_order'),
    path('update_order/<int:meal_id>/<str:action>/', update_order, name='update_order'),
    path('hx_menu_order/', hx_menu_order, name="hx_menu_order"),
    path('contacts/', views.contact, name='contacts'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_req, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)