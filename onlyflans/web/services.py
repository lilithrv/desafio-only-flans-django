from .models import Flan

def create_flan(name, description, image_url, slug, is_private, price):
    try:
        new_flan = Flan(name=name, description=description, image_url=image_url, slug=slug, is_private=is_private, price=price)
        new_flan.save()
        return new_flan
    except Exception as e:
        print(f"Error al crear el usuario: {e}")
        return None

