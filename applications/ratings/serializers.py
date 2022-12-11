from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class ReviewersSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
