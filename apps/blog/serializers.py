from rest_framework import serializers
from .models import Tag, Post, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField(read_only=Tag)

    def get_tag(self, obj):
        tag = obj.tag.all()
        serializer = TagSerializer(tag, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'content', 'tag', 'created_at']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'content', 'tag', 'created_at']

    def create(self, validated_data):
        tag = validated_data.pop('tag', [])
        instance = Post.objects.create(**validated_data)
        for i in tag:
            instance.tag.add(i)
        return instance
