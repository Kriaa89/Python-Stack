from django.shortcuts import render, redirect
from decimal import Decimal
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_order(request):
    if request.method == "POST":
        # Get product and calculate total
        product_id = request.POST["product_id"]
        quantity = int(request.POST["quantity"])
        product = Product.objects.get(id=product_id)
        total = product.price * quantity
        
        # Create order using correct field names
        Order.objects.create(
            product=product,
            quantity_ordered=quantity,  # Ensure this matches the model field name
            total_price=total  # Ensure this matches the model field name
        )
        return redirect("/checkout")
    return redirect("/")


def checkout(request):
    all_orders = Order.objects.all()
    last_order = Order.objects.last()
    
    total_spent = sum([order.total_price for order in all_orders], Decimal('0.00'))
    total_quantity = sum(order.quantity_ordered for order in all_orders)

    context = {
        "last_order": last_order,
        "total_quantity": total_quantity,
        "total_spent": total_spent
    }
    return render(request, "store/checkout.html", context)