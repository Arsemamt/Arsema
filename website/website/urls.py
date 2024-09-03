from django.contrib import admin
from django.urls import path
from myapp.views import home, book, contact_form,course, book_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('book/', book, name='book'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('course/', course, name='course'),
    path('contact/', contact_form, name='contact_form'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
