from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
# from account import views


urlpatterns = [
    
    # path(
    #     "",
    #     views.PasswordReset.as_view(),
    #     name="request-password-reset",
    # ),
    # path(
    #     "password-reset/<str:encoded_pk>/<str:token>/",
    #     views.ResetPasswordAPI.as_view(),
    #     name="reset-password",
    # ),
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


