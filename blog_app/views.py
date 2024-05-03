from django.http import JsonResponse
from .models import Blog, BlogComment, Contact 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BlogSerializer, BlogCommentSerializer, ContactSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

# BLOG
@api_view(['GET'])
def blog_list(request):
    all_blogs  = Blog.objects.filter(is_public=True)
    serializer = BlogSerializer(all_blogs, many=True)  #CONVERT TO DICTIONARY
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk, is_public=True)
    serializer = BlogSerializer(blog)  #CONVERT TO DICTIONARY
    return Response(serializer.data)


# COMMENT
@api_view(['GET'])
def blogcomment_list(request):
    blog_comment  = BlogComment.objects.all()
    serializer    = BlogCommentSerializer(blog_comment, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blogcomment_detail(request, pk):
    blog_comment  = BlogComment.objects.get(pk=pk)
    serializer    = BlogCommentSerializer(instance=blog_comment)
    return Response(serializer.data)

# CONTACT
@api_view(['GET'])
def contact_list(request):
    contact    = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contact_detail(request, pk):
    contact    = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(instance=contact)
    return Response(serializer.data)