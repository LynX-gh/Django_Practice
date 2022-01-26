from django.contrib.auth.models import User

from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from ads.models import Ad, Comment


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:snippet-detail")
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='api:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='api:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class CommentSerializer(serializers.ModelSerializer):
    text = serializers.ReadOnlyField()
    time = serializers.ReadOnlyField( source='created_at' )

    class Meta:
        model = Comment
        fields = ['text', 'time']

class AdSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField( source='owner.username' )
    tags = TagListSerializerField()
    comments = CommentSerializer( source='comment_set', read_only=True, many=True )
    url = serializers.HyperlinkedIdentityField( view_name='api:ad-detail' )
    browse = serializers.HyperlinkedIdentityField( view_name='ads:ad detail' )
    picture = serializers.HyperlinkedIdentityField( read_only=True, view_name='ads:ad picture' )
    last_updated = serializers.ReadOnlyField( source='updated_at' )

    class Meta:
        model = Ad
        fields = ['id', 'owner', 'title', 'price', 'text', 'tags', 'comments', 'url', 'browse', 'picture', 'last_updated']