from django.db.models import Prefetch
from db.models import Products, Platforms, Genres

# Define the prefetch object for platform and genre
platforms_prefetch = Prefetch('platform', queryset=Platforms.objects.only('title'))
genres_prefetch = Prefetch('genre', queryset=Genres.objects.only('title'))

# Prompt the user for a product id
product_id = input("Enter product id: ")

# Retrieve the product with the matching id and its related platform and genre
try:
    product = Products.objects.prefetch_related(platforms_prefetch, genres_prefetch).get(id=product_id)
except Products.DoesNotExist:
    print(f"No product found with id {product_id}\n")
else:
    # Display the product details along with platform and genre name
    platform_names = [p.title for p in product.platform.all()]
    genre_names = [g.title for g in product.genre.all()]
    print(f"Title: {product.title}\n")
    print(f"Description: {product.description}\n")
    print(f"Platforms: {', '.join(platform_names)}\n")
    print(f"Publisher: {product.publisher.title}\n")
    print(f"Release Date: {product.releaseDate}\n")
    print(f"Price: {product.price} тг\n")
    print(f"Content Rating: {product.contentRating.title}\n")
    print(f"Genres: {', '.join(genre_names)}\n")
    print(f"Is Available: {product.isAvailable}")
