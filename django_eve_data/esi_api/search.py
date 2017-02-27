# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class Search(object):
    base_url = "https://esi.tech.ccp.is/latest/search/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_search_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_search_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'type': 'object', 'properties': {'alliance': {'items': {'format': 'int32', 'type': 'integer', 'description': 'alliance integer', 'title': 'get_search_alliance'}, 'type': 'array', 'description': 'alliance array', 'title': 'get_search_alliance'}, 'faction': {'items': {'format': 'int32', 'type': 'integer', 'description': 'faction integer', 'title': 'get_search_faction'}, 'type': 'array', 'description': 'faction array', 'title': 'get_search_faction'}, 'constellation': {'items': {'format': 'int32', 'type': 'integer', 'description': 'constellation integer', 'title': 'get_search_constellation'}, 'type': 'array', 'description': 'constellation array', 'title': 'get_search_constellation'}, 'inventorytype': {'items': {'format': 'int32', 'type': 'integer', 'description': 'inventorytype integer', 'title': 'get_search_inventorytype'}, 'type': 'array', 'description': 'inventorytype array', 'title': 'get_search_inventorytype'}, 'character': {'items': {'format': 'int32', 'type': 'integer', 'description': 'character integer', 'title': 'get_search_character'}, 'type': 'array', 'description': 'character array', 'title': 'get_search_character'}, 'station': {'items': {'format': 'int32', 'type': 'integer', 'description': 'station integer', 'title': 'get_search_station'}, 'type': 'array', 'description': 'station array', 'title': 'get_search_station'}, 'corporation': {'items': {'format': 'int32', 'type': 'integer', 'description': 'corporation integer', 'title': 'get_search_corporation'}, 'type': 'array', 'description': 'corporation array', 'title': 'get_search_corporation'}, 'agent': {'items': {'format': 'int32', 'type': 'integer', 'description': 'agent integer', 'title': 'get_search_agent'}, 'type': 'array', 'description': 'agent array', 'title': 'get_search_agent'}, 'wormhole': {'items': {'format': 'int32', 'type': 'integer', 'description': 'wormhole integer', 'title': 'get_search_wormhole'}, 'type': 'array', 'description': 'wormhole array', 'title': 'get_search_wormhole'}, 'region': {'items': {'format': 'int32', 'type': 'integer', 'description': 'region integer', 'title': 'get_search_region'}, 'type': 'array', 'description': 'region array', 'title': 'get_search_region'}, 'solarsystem': {'items': {'format': 'int32', 'type': 'integer', 'description': 'solarsystem integer', 'title': 'get_search_solarsystem'}, 'type': 'array', 'description': 'solarsystem array', 'title': 'get_search_solarsystem'}}, 'description': '200 ok object', 'title': 'get_search_ok'}, 'examples': {'application/json': {'solarsystem': [30002510], 'station': [60004588, 60004594, 60005725, 60009106, 60012721, 60012724, 60012727]}}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of search results'}}

    def get(self, categories, search, datasource="tranquility",language="en-us",strict="False",**kwargs):
        """
                Search for entities that match a given sub-string.
        
        ---
        
        Alternate route: `/v1/search/`
        
        Alternate route: `/legacy/search/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type categories: list
        :param categories: Type of entities to search for
:type search: str
        :param search: The string to search on
:type datasource: str
        :param datasource: The server name you would like data from
:type language: str
        :param language: Search locale
:type strict: boolean
        :param strict: Whether the search should be a strict match
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"categories" : categories, "search" : search, "datasource" : datasource, "language" : language, "strict" : strict, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)