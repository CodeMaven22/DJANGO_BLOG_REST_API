from rest_framework import serializers
from . models import Blog, BlogComment, Contact


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Blog
        fields = "__all__"
        

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogComment
        fields ="__all__"
        

class ContactSerializer(serializers.ModelSerializer):
     class Meta:
        model  = Contact
        fields ="__all__"