from django.urls import path
from .views import search_page, search_drugs
from adminp import views
urlpatterns = [
    path('', search_page, name='search_page'),  # Root URL serving the search page
    path('search/', search_drugs, name='search_drugs'),  # Search functionality
    path('login/', views.login_view, name='login_view')
]
