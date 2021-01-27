from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id', 'author', 'content', 'created_at', 'is_public']
        fields='__all__'


# class ArticleSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     author=serializers.CharField(max_length=100)
#     title=serializers.CharField(max_length=150)
#     content=serializers.CharField(style={'base_template': 'textarea.html'})
#     created_at=serializers.DateTimeField()
#     is_public=serializers.BooleanField()

#     def create(self, validated_data):
        
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):

#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.is_public = validated_data.get('is_public', instance.is_public)
#         instance.save()
#         return instance