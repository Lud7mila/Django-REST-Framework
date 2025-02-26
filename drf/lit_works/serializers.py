from rest_framework import serializers
from .models import LitWork, Author


class LitWorkSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(read_only=True)
    class Meta:
        model = LitWork
        fields = "__all__" #('title', "description", 'category_id', "author_id")


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Author
        fields = "__all__"

# class LitWorkModel:
#     def __init__(self, title, description, text):
#         self.title = title
#         self.description = description
#         text = models.TextField(verbose_name="Текст")
#         time_create = models.DateTimeField(auto_now_add=True)
#         time_update = models.DateTimeField(auto_now=True)  # дата и время обновления
#         slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
#         author = models.ForeignKey(Author, on_delete=models.CASCADE,
#                                    related_name='author')  # автор данного литературного произведения
#         category = models.ForeignKey(Category, on_delete=models.CASCADE,
#                                      related_name='Category')

# class LitWorkSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     text = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     author_id = serializers.IntegerField()
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return LitWork.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.text = validated_data.get("text", instance.text)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.author_id = validated_data.get("author_id", instance.author_id)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save()
#         return instance
