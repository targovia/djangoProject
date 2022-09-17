from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#Importnat here is that in path, first argument is string that points to url, the second is the method

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('business', views.business, name='business'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name=' logout'),
    path('profile/', user_views.profile, name='profile'),
    # path('gsonback', views.gsonback, name='gsonback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)