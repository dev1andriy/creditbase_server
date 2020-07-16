from rest_framework import serializers
from common.models.other.note import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('Note',)

