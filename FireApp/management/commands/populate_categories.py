from  FireApp.models import Category
from django.core.management.base import BaseCommand
from typing import Any


    
class Command(BaseCommand):
    help="This command inserts Category data"
    
    def handle(self, *args: Any, **options: Any):
        Category.objects.all().delete()
        
        categories=['Technology', 'Science', 'Art', 'Food', 'Sports']

        for category_name in categories:
            Category.objects.create(name= category_name)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        
        
       
    