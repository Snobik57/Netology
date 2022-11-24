from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter, FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']
