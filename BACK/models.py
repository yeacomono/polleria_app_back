from django.db import models

class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)  # Ejemplo: "M1", "M2"
    capacity = models.IntegerField()  # Capacidad de personas
    status = models.CharField(max_length=20, default="available")  # "available", "occupied", "reserved"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Roles y Usuarios
class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Productos y Combos
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_combo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Pedidos
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')  # Mesero
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')  # Mesa asignada
    status = models.CharField(max_length=50)  # "pending", "preparing", "ready", "delivered"
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

# Inventario
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity_available = models.IntegerField()
    unit = models.CharField(max_length=50)  # "kg", "units", "liters"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InventoryUsage(models.Model):
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_usage')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='usage')
    quantity_used = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='inventory_usages')

# Facturación
class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=50, unique=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Reportes
class Report(models.Model):
    report_type = models.CharField(max_length=50)  # "daily_sales", "top_products"
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
