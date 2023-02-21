from db.models import Product

product = Product(title='Product1', price=100)
product.save()
