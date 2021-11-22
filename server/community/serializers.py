from rest_framework import serializers
from movies.serializers import MovieSerializer
from .models import Review,Comment
from movies.models import Movie
from accounts.serializers import UserSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
            model = Comment
            fields = "__all__"
            read_only_fields=('user', 'review')

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = "__all__"
        movie = MovieSerializer(read_only=True)
    
    comment_set = CommentSerializer(many=True,read_only=True)
        
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('movie',' comment_set')



    