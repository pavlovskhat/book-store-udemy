from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    """
    To test many to many data relationship
    """
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)


class Address(models.Model):
    """
    To test 1 to 1 data relationship
    """
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"

    class Meta:
        """
        Special class to control admin meta data behavior
        """
        verbose_name_plural = "Address Entries"  # changes plural display of tables


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):  # To recall dynamically from templates
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    """
    1 to many data relationship with Author.
    """
    title = models.CharField(max_length=50)
    rating = models.IntegerField(  # https://docs.djangoproject.com/en/4.2/ref/validators/
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name="books")  # Related table name: QOL improvement to manage.py shell
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="",
                            # editable=False,  # Created admin class
                            null=False,
                            db_index=True,  # db_index isolates field for efficient searching
                            unique=True)
    published_countries = models.ManyToManyField(Country)  # Creates 3rd mapping table & auto deletes dependencies

    def get_absolute_url(self):
        """
        Reverse the destination "book-detail" to return url path.
        Uses slug to identify specific book.
        """
        return reverse("book-detail", args=[self.slug])

    # NOTE: admin.py => prepopulated_fields()
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
