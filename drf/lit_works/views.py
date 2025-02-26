# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.forms.models import model_to_dict
from .models import LitWork, Author
from .serializers import LitWorkSerializer, AuthorSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAuthorOrReadOnly, IsAuthor

# from rest_framework import mixins
# from rest_framework.viewsets import GenericViewSet
# class LitWorkViewSet(  # вместо viewsets.ModelViewSet
#                        mixins.CreateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.DestroyModelMixin,
#                        mixins.ListModelMixin,
#                        GenericViewSet):
#     queryset = LitWork.objects.all()
#     serializer_class = LitWorkSerializer


from rest_framework import generics

from rest_framework.permissions import (BasePermission, IsAuthenticatedOrReadOnly, IsAdminUser,
                                        IsAuthenticated,SAFE_METHODS)


class LitWorksListAPIView(generics.ListAPIView):
    queryset = LitWork.objects.all()
    serializer_class = LitWorkSerializer

class LitWorksCreateAPIView(generics.CreateAPIView):
    queryset = LitWork.objects.all()
    serializer_class = LitWorkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



# class LitWorkAPIUpdate(generics.UpdateAPIView):
#     queryset = LitWork.objects.all()
#     serializer_class = LitWorkSerializer

class LitWorkAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LitWork.objects.all()
    serializer_class = LitWorkSerializer
    permission_classes = (IsAuthorOrReadOnly, ) #IsAdminOrReadOnly,)  # IsAdminUser,)


class AuthorAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)
# class LitWorksAPIView(APIView):
#     def get(self, request):
#         works = LitWork.objects.all().values()
#         return Response({'litworks': LitWorkSerializer(works, many=True).data})
#
#     def post(self, request):
#         serializer = LitWorkSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'lit_work': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "В запросе PUT отсутствует идентификатор"})
#
#         try:
#             instance = LitWork.objects.get(pk=pk)
#         except:
#             return Response({"error": "Объект не существует"})
#
#         serializer = LitWorkSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "В запросе DELETE отсутствует идентификатор"})
#
#         try:
#             instance = LitWork.objects.get(pk=pk)
#         except:
#             return Response({"error": "Объект не существует"})
#
#         instance.delete()
#
#         return Response({"post": "delete post " + str(pk)})

