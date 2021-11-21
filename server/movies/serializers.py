from rest_framework import serializers

from .models import Movie, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    # class CommentSerializer(serializers.ModelSerializer):
    #     model = Comment
    #     fields = "__all__"
    comment_set = CommentSerializer(many=True,read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('comment_set',)