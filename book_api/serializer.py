from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No diet coke please")
        return value
    
    # The serializer inherently validates things for us, it validates that we're providing it with the correct fields, but we can also have our own validation, so right after the Meta class we declare a function with the name validate_property, and you can validate the whole object creating another methods called def validate(self, data)

"""
from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()

    # This method is going to be called in order to create a book in our database
    def create(self, data):
        return Book.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.publish_date = data.get('publish_date', instance.publish_date)
        instance.quantity = data.get('quantity', instance.quantity)

        instance.save()
        return instance
"""