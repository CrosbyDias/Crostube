from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login_user/', login_user, name='login_user'),
]
