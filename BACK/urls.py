from django.urls import path
from BACK.views import *  # Ajusta según tus vistas

urlpatterns = [
    # Roles
    path("roles/", RoleListCreateView.as_view(), name="role-list-create"),
    path("roles/<int:pk>/", RoleDetailView.as_view(), name="role-detail"),
    # Usuarios
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    # Productos
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    # Pedidos
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    # Inventario
    path("inventory/", InventoryListCreateView.as_view(), name="inventory-list-create"),
    path("inventory/<int:pk>/", InventoryDetailView.as_view(), name="inventory-detail"),
    # Facturación
    path("invoices/", InvoiceListCreateView.as_view(), name="invoice-list-create"),
    path("invoices/<int:pk>/", InvoiceDetailView.as_view(), name="invoice-detail"),
    # Reportes
    path("reports/", ReportListCreateView.as_view(), name="report-list-create"),
    path("reports/<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
    # Mesas
    path("tables/", TableListCreateView.as_view(), name="table-list-create"),
    path("tables/<int:pk>/", TableDetailView.as_view(), name="table-detail"),
]
