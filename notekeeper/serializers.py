from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from . import models


class NoteSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = models.Note
        fields = ('id', 'title', 'content', 'tags', 'created_at',)
        read_only_fields = ('id',)
