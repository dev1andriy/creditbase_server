from django.contrib.postgres.fields import JSONField
from django.core import serializers
from django.db import models

from common.models import TimeStampedModel, InsertableModel, UpdateableModel, RankableModel, PrintableModel


class SearchTemplates(TimeStampedModel, InsertableModel, UpdateableModel, RankableModel):
    TemplateId = models.AutoField(primary_key=True, null=False, blank=False)
    TemplateName = models.CharField(null=True, blank=True, max_length=200)
    Enabled = models.BooleanField(default=True, null=True)
    OrderingRank = models.IntegerField(default=100, null=False)

    # objects = models.Manager()

    def __str__(self):
        return "{} - {} ".format(self.TemplateId, self.TemplateName)

    class Meta:
        verbose_name = "SearchTemplates"
        db_table = "SearchTemplates"


class SearchCriteria(TimeStampedModel, InsertableModel, UpdateableModel, RankableModel):
    CriteriaId = models.AutoField(primary_key=True, null=False, blank=False)
    CriteriaName = models.CharField(max_length=50, null=True, blank=True)
    CriteriaSymbol = models.CharField(max_length=10, null=True, blank=True)
    IsExcludeCondition = models.BooleanField(null=True, default=False)
    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CriteriaId, self.CriteriaName)

    class Meta:
        verbose_name = "SearchCriteria"
        db_table = "SearchCriteria"


class SearchFields(TimeStampedModel, InsertableModel, UpdateableModel, RankableModel):
    FieldId = models.AutoField(primary_key=True, null=False, blank=False)
    FieldType = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    ActiveFlag = models.BooleanField(default=True)
    AllowNullFlag = models.BooleanField(default=True)
    LookupKey = models.CharField(max_length=50, null=True, blank=True)
    LookupValue = models.CharField(max_length=50, null=True, blank=True)
    DefaultCriteriaId = models.ForeignKey(SearchCriteria, null=True, on_delete=models.PROTECT)
    ApplicableCriteria = JSONField(null=True,
                                   blank=True)  # default=serializers.serialize('json', [SearchCriteria.objects.all().values('CriteriaId'),]))
    FieldModelPath = models.CharField(max_length=300, null=True, blank=True, default=None)
    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FieldId, self.Description)

    class Meta:
        verbose_name = "SearchFields"
        db_table = "SearchFields"


class SearchTemplateParams(TimeStampedModel, InsertableModel, UpdateableModel, RankableModel):
    ParamId = models.AutoField(primary_key=True, null=False, blank=False)
    TemplateId = models.ForeignKey(SearchTemplates, null=True, blank=True, on_delete=models.PROTECT)
    TemplateField = models.ForeignKey(SearchFields, null=True, blank=True, on_delete=models.PROTECT)
    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.ParamId, self.TemplateId.TemplateName, self.TemplateField.Description)

    class Meta:
        verbose_name = "SearchTemplateParams"
        db_table = "SearchTemplateParams"


# class SearchGridParams(TimeStampedModel, InsertableModel, UpdateableModel, RankableModel):
#    GridParamId = models.AutoField(primary_key=True, null=False, blank=False)

class SearchGridConfig(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    SearchGridId = models.AutoField(primary_key=True, null=False, blank=False)
    TemplateId = models.OneToOneField(SearchTemplates, null=True, blank=True, on_delete=models.SET_NULL)
    GridConfig = JSONField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.SearchGridId, self.TemplateId.TemplateName)

    class Meta:
        verbose_name = "SearchGridConfig"
        db_table = "SearchGridConfig"
