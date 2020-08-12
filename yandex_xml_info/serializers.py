from fastapi_contrib.serializers.common import ModelSerializer

from yandex_xml_info.models import SearchResult


class SearchResultSerializer(ModelSerializer):
    class Meta:
        model = SearchResult