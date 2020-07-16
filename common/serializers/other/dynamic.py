from rest_framework import serializers
from django.apps import apps


class DynamicModelSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = None
        fields = ('value', 'label')

    def get_value(self, instance):
        return getattr(instance, self.value_field)

    def get_label(self, instance):
        return getattr(instance, self.label_field)

    def __init__(self, *args, **kwargs):
        self.Meta.model = apps.get_registered_model('common', kwargs.pop('model', None))
        self.value_field = kwargs.pop('value_field', None)
        self.label_field = kwargs.pop('label_field', None)

        super(DynamicModelSerializer, self).__init__(*args, **kwargs)

