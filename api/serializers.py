from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['user']

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)
    tags = TagSerializers(many=True)
    review = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'

    def get_review(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializers(reviews, many=True)
        return serializer.data