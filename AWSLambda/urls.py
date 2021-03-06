from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from graphene_django.views import GraphQLView
from AWSLambda.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ingredients', GraphQLView.as_view(graphiql=True, schema=schema)),
]
