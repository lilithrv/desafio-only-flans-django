from django.db import models
from django.forms import ModelForm
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.customer_name} - {self.customer_email}"

class ContactFormModelForm(ModelForm):
     class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Email',
            'message': 'Mensaje'
        }
        error_messages = {
            'customer_name': {
                'max_length': 'El nombre es demasiado largo'
            },
            'customer_email': {
                'invalid': 'El formato de email es incorrecto'
            }
        }
    
     def __init__(self, *args, **kwargs):
        super(ContactFormModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' 
        self.fields['message'].widget.attrs['rows'] = 3
    
     