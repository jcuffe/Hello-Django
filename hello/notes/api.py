from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note

    class Meta:
        model = Note
        fields = ('title', 'content', 'url')

class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = NoteSerializer
    queryset = Note.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Note.objects.none()
        else:
            return Note.objects.filter(user=user)