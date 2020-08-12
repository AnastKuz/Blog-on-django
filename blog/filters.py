import django_filters

from blog.models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['title']
