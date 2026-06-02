from django.urls import path
from .views import (
    IndexView, InfoView, CartView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    BrandListView, BrandDetailView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    StoreListView, StoreDetailView, StoreCreateView, StoreUpdateView, StoreDeleteView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView,
)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('info/', InfoView.as_view(), name='info'),
    path('cart/', CartView.as_view(), name='cart'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<slug:category_slug>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<slug:category_slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<slug:product_slug>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<slug:product_slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/add/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/edit/', BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('stores/', StoreListView.as_view(), name='store_list'),
    path('stores/add/', StoreCreateView.as_view(), name='store_create'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
    path('stores/<int:pk>/edit/', StoreUpdateView.as_view(), name='store_update'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store_delete'),

    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),

    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/add/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
]