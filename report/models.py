from django.db import models
import datetime
import os


class TheCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    name_company = models.CharField(max_length=45, blank=True, null=True)
    tag_company = models.CharField(max_length=45, db_collation='utf8_general_ci')
    discrip_company = models.CharField(max_length=500, db_collation='utf8_general_ci')
    cat_company = models.CharField(max_length=50)
    img_company = models.ImageField(upload_to="")
    time_create = models.DateTimeField(blank=True, null=True)
    time_update = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = "the_company"
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'

    def __int__(self):
        return self.name_company
