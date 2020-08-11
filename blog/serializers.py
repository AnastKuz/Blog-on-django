from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
