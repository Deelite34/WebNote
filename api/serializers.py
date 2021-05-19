from .models import Note
from rest_framework import serializers


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    views_count = serializers.ReadOnlyField()  # Computed within views, adding or editing by user is forbidden
    id = serializers.ReadOnlyField()           # Editing primary key is forbidden. Added for ease of viewing notes.

    class Meta:
        model = Note
        fields = ('id', 'content', "views_count")
