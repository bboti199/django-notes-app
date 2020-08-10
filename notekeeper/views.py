from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import NoteSerializer
from .firebase import FirebaseAuthentication


class NoteViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
    authentication_classes = (FirebaseAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
