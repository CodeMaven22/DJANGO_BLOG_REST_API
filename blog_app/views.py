from django.http import JsonResponse
from .models import Blog, BlogComment, Contact 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import BlogSerializer, BlogCommentSerializer, ContactSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

# BLOG
@api_view(['POST'])
def create_blog(request):
    serializer =BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def blog_list(request):
    all_blogs  = Blog.objects.filter(is_public=True)
    serializer = BlogSerializer(all_blogs, many=True)  #CONVERT TO DICTIONARY
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def blog_detail(request, pk):
    blog       = Blog.objects.get(pk=pk, is_public=True)
    serializer = BlogSerializer(blog)  #CONVERT TO DICTIONARY
    return Response(serializer.data)


@api_view(['PATCH'])
def blog_update(request, pk):
    blog       = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

 
# COMMENT
@api_view(['POST'])
def create_comment(request):
    serializer = BlogCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
        
@api_view(['GET'])
def blogcomment_list(request):
    blog_id = request.GET.get('blog')
    blog_comment = BlogComment.objects.filter(blog_id=blog_id)
    serializer = BlogCommentSerializer(blog_comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def blogcomment_detail(request, pk):
    blog_comment  = BlogComment.objects.get(pk=pk)
    serializer    = BlogCommentSerializer(instance=blog_comment)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def blockcomment_update(request, pk):
    comment    = get_object_or_404(BlogComment, pk=pk)
    serializer = BlogCommentSerializer(data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def blockcomment_delete(request, pk):
    contact = get_object_or_404(BlogCommentSerializer, pk=pk)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# CONTACT  
@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['PATCH'])
def contact_update(request, pk):
    contact    = get_object_or_404(Contact, pk=pk)
    serializer =ContactSerializer(data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)