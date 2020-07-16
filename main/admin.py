from django.contrib import admin
from django.apps import apps

main = apps.get_app_config('main')
common = apps.get_app_config('common')

my_apps = (main, common)

for app in my_apps:
    for model_name, model in app.models.items():
        admin.site.register(model)
