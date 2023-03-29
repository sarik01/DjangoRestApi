from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Post

        fields = ('id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status', 'category')


class PostSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = ('id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status', 'category')

    # def create(self, validated_data):
    #     instance = self.Meta.model(**validated_data)
    #
    #     instance.save()
    #     return instance


class PostSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = ('id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status', 'category')

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.save()
    #     return instance
