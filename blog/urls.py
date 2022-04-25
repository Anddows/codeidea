from django.urls import path
from .views import ( AboutPageView,
                     BlogListView,
                     BlogDetailView,
                     BlogCreateView,
                     BlogUpdateView,
                     CcsPageView,
                     SendOrderPageView,
                     ProjectsPageView,
                     ServicePageView,
                     SplashScreenPageView,
BlogDeleteView,
                     )

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post-delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'post-edit'),
    path('blog/news/', BlogCreateView.as_view(), name = 'post-new'),
    path('home/', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = "post-detail"),
    path('about/', AboutPageView.as_view(), name = "about"),
    path('projects/', ProjectsPageView.as_view(), name = "projects"),
    path('buyurtma/', SendOrderPageView.as_view(), name = "buyurtma"),
    path('ccs/', CcsPageView.as_view(), name = "ccs"),     
    path('', SplashScreenPageView.as_view(), name = 'splash-screen'),
    path('service/', ServicePageView.as_view(), name = 'service')
]