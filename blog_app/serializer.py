from rest_framework import serializers
from . models import Blog, BlogComment, Contact
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
        
class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    author_username = serializers.SerializerMethodField()
    author_email = serializers.SerializerMethodField()
    
    
    class Meta:
        model  = Blog
        fields = ('id', 'name', 'description', 'mini_description', 'post_date', 'is_public', 'slug', 'author', 'author_username', 'author_email')
    
    def get_author_id(self, obj):
        return obj.author.id
    
    def get_author_username(self, obj):
        return obj.author.username

    def get_author_email(self, obj):
        return obj.author.email

class BlogCommentSerializer(serializers.ModelSerializer):
    # Ensure that the queryset parameter in PrimaryKeyRelatedField includes all the available Blog instances so that the serializer can validate and accept the blog ID provided in the request data.
    blog   = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())    
    class Meta:
        model  = BlogComment
        fields =('id', 'description','blog', 'comment_date')
    

class ContactSerializer(serializers.ModelSerializer):
     class Meta:
        model  = Contact
        fields ="__all__"