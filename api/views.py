from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

class ArticleView(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class ArticleListView(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArtileListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleListView2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

    def get(self, request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


class ArtileListDetailView2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self, request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

# class ArticleList(APIView):
#     def get(self, request, format=None):
#         article=Article.objects.all()
#         serializer=ArticleSerializer(article, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# class ArtileListDetail(APIView):
#     def get_object(self, pk):
#         try:
#             article=Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return Http404
#     def get(self, request, pk, format=None):
#         article=Article.objects.get(pk=pk)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         article=Article.objects.get(pk=pk)
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         article=Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method=="GET":
#         article=Article.objects.all()
#         serializer=ArticleSerializer(article, many=True)
#         return Response(serializer.data)

#     elif request.method=="POST":
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['GET', 'PUT','DELETE'])
# def article_detail(request, pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=="GET":
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method=="PUT":
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method=="DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @csrf_exempt
# def article_list(request):
#     if request.method=="GET":
#         article=Article.objects.all()
#         serializer=ArticleSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method=="POST":
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error, status=400)
        

# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method=="GET":
#         serializer=ArticleSerializer(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method=="PUT":
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.error, status=400)
    
#     elif request.method=="DELETE":
#         article.delete()
#         return HttpResponse(status=404)


