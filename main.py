from fastapi import FastAPI, Depends
from fastapi_contrib.pagination import Pagination

from yandex_xml_info.serializers import SearchResultSerializer

TEXT = (
    'Плоский мир – это планета, которая плывет сквозь космическое пространство'
    ' на спинах четырех слонов и гигантской черепахи. Там свои законы физики:'
    ' свет движется медленно, магия материальна, в радуге восемь цветов. В'
    ' Плоском мире живут тролли, гномы, эльфы, големы, вампиры, оборотни,'
    ' зомби. Эти магические расы борются за свои права и равенство при приеме '
    'на работу.'
)


app = FastAPI()


@app.get("/start")
async def root():
    """Endpoint для старта разбора текста."""

    #todo тут должна стартоваться


@app.get("/search_result/")
async def list(pagination: Pagination = Depends()):
    return await pagination.paginate(
        serializer_class=SearchResultSerializer
    )
