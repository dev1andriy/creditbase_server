from django.core import serializers

from common.models.search import SearchTemplates, SearchCriteria, SearchFields, SearchTemplateParams


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'


class SearchTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTemplates
        fields = '__all__'
        depth = 2


class SearchCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchCriteria
        fields = '__all__'


class SearchFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchFields
        fields = '__all__'


class SearchTemplateParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTemplateParams
        fields = '__all__'
