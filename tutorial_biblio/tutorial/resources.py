from tutorial.models import Book
from import_export import resources

class BookResource(resources.ModelResource):
    class Meta:
        model = Book