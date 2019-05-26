from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Date
from elasticsearch_dsl import DocType
from elasticsearch_dsl import Index
from elasticsearch_dsl import Integer
from elasticsearch_dsl import Nested
from elasticsearch_dsl import Text

from accounts import models


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


class ProfileDocument(DocType):
    """Profile index definition."""
    user = Nested(properties={'id': Integer(), 'username': Text()})
    slug = Text()
    first_name = Text()
    last_name = Text()
    address = Text()
    description = Text()

    class Index:
        name = 'profile-document'
        settings = {
            "number_of_shards": 2,}

    def save(self, **kwargs):
       return super().save(**kwargs)

def initialize_document():
    """Initialize Documents."""
    es = Elasticsearch()
    if ProfileDocument:
        # Delete entire index to prepare for re-initialization.
        es.indices.delete(index=ProfileDocument.Index.name, ignore=[400, 404])
    ProfileDocument.init()

    # create and save profile
    profile_objects = models.Profile.objects.all()
    for item in profile_objects:
        profile = ProfileDocument(meta={'id': item.id},
            user={'id': item.user.id, 'username': item.user.username},
            slug=item.slug,
            first_name=item.first_name, last_name=item.last_name,
            address = item.address, description = item.description)

        profile.save()
