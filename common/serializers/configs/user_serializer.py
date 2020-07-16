from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # value = serializers.StringRelatedField(source='RelationTypeId')
    # label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = User
        # fields = ('value', 'label')
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "value": representation['id'],
            "label": "{} {}".format(representation['first_name'], representation['last_name'])
        }

        return to_represent
