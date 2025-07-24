
from rest_framework_nested import routers
from django.urls import path
from .views import BookViewSet , CategoryViewSet, DiscountViewSet , BookDetail
from rest_framework.routers import SimpleRouter, DefaultRouter

from rest_framework_nested import routers
from . import views  # assuming your viewsets are here



router = routers.DefaultRouter()


router.register('book', BookViewSet,basename='book')
book_router = routers.NestedDefaultRouter(router,'book',lookup='book')

router.register(r'book-categories', CategoryViewSet, basename='book-category')
category_router = routers.NestedDefaultRouter(router, r'book-categories', lookup='book_category')
category_router.register(r'books', BookViewSet, basename='book-category-books')



book_router.register('comments',DiscountViewSet,basename='product-comments')


urlpatterns = router.urls + book_router.urls + category_router.urls + [
    path('book-detail/<int:pk>',BookDetail.as_view(),name='book-detail'),
]


