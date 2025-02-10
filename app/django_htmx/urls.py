"""
URL configuration for django_htmx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from books.views import create_book, update_book_details, book_detail, delete_book, update_book_status, book_list_sort, book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", book_list, name="book_list"), # BookList.as_view()
    path("create_book/", create_book, name="create_book"),
    path("update_book_details/<int:pk>/", update_book_details, name="update_book_details"),
    path("book_detail/<int:pk>/", book_detail, name="book_detail"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
    path("update_book_status/<int:pk>/", update_book_status, name="update_book_status"),
    path("book_list_sort/<filter>/<direction>/", book_list_sort, name="book_list_sort"),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)