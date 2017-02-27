# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class MarketsDetailOrders(object):
    base_url = "https://esi.tech.ccp.is/latest/markets/{region_id}/orders/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_markets_region_id_orders_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_markets_region_id_orders_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'title': 'get_markets_region_id_orders_200_ok', 'type': 'object', 'properties': {'duration': {'format': 'int32', 'type': 'integer', 'description': 'duration integer', 'title': 'get_markets_region_id_orders_duration'}, 'price': {'format': 'float', 'type': 'number', 'description': 'price number', 'title': 'get_markets_region_id_orders_price'}, 'location_id': {'format': 'int64', 'type': 'integer', 'description': 'location_id integer', 'title': 'get_markets_region_id_orders_location_id'}, 'min_volume': {'format': 'int32', 'type': 'integer', 'description': 'min_volume integer', 'title': 'get_markets_region_id_orders_min_volume'}, 'range': {'enum': ['station', 'region', 'solarsystem', '1', '2', '3', '4', '5', '10', '20', '30', '40'], 'type': 'string', 'description': 'range string', 'title': 'get_markets_region_id_orders_range'}, 'issued': {'format': 'date-time', 'type': 'string', 'description': 'issued string', 'title': 'get_markets_region_id_orders_issued'}, 'is_buy_order': {'type': 'boolean', 'description': 'is_buy_order boolean', 'title': 'get_markets_region_id_orders_is_buy_order'}, 'order_id': {'format': 'int64', 'type': 'integer', 'description': 'order_id integer', 'title': 'get_markets_region_id_orders_order_id'}, 'volume_total': {'format': 'int32', 'type': 'integer', 'description': 'volume_total integer', 'title': 'get_markets_region_id_orders_volume_total'}, 'volume_remain': {'format': 'int32', 'type': 'integer', 'description': 'volume_remain integer', 'title': 'get_markets_region_id_orders_volume_remain'}, 'type_id': {'format': 'int32', 'type': 'integer', 'description': 'type_id integer', 'title': 'get_markets_region_id_orders_type_id'}}, 'description': '200 ok object', 'required': ['order_id', 'type_id', 'location_id', 'volume_total', 'volume_remain', 'min_volume', 'price', 'is_buy_order', 'duration', 'issued', 'range']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_markets_region_id_orders_ok'}, 'examples': {'application/json': [{'duration': 90, 'price': 9.9, 'location_id': 60005599, 'min_volume': 1, 'range': 'region', 'issued': '2016-09-03T05:12:25Z', 'is_buy_order': False, 'order_id': 4623824223, 'volume_total': 2000000, 'volume_remain': 1296000, 'type_id': 34}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of orders'}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Unprocessable entity message', 'title': 'get_markets_region_id_orders_422_unprocessable_entity'}}, 'description': 'Unprocessable entity', 'title': 'get_markets_region_id_orders_unprocessable_entity'}, 'examples': {'application/json': {'error': 'Unprocessable entity message'}}, 'description': 'Not found'}}

    def get(self, region_id, datasource="tranquility",order_type="all",page=1,**kwargs):
        """
                Return a list of orders in a region
        
        ---
        
        Alternate route: `/v1/markets/{region_id}/orders/`
        
        Alternate route: `/legacy/markets/{region_id}/orders/`
        
        Alternate route: `/dev/markets/{region_id}/orders/`
        
        
        ---
        
        This route is cached for up to 300 seconds

:type region_id: int
        :param region_id: Return orders in this region
:type datasource: str
        :param datasource: The server name you would like data from
:type order_type: str
        :param order_type: Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders.

:type page: int
        :param page: Which page to query, only used for querying without type_id. Starting at 1

:param kwargs: type_id, user_agent, X-User-Agent
    """
        kwargs_dict ={
"region_id" : region_id, "datasource" : datasource, "order_type" : order_type, "page" : page, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class MarketsStructuresDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/markets/structures/{structure_id}/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_markets_structures_structure_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_markets_structures_structure_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'get_markets_structures_structure_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'get_markets_structures_structure_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-markets.structure_markets.v1'}}, 'description': 'Forbidden'}, '200': {'schema': {'items': {'title': 'get_markets_structures_structure_id_200_ok', 'type': 'object', 'properties': {'duration': {'format': 'int32', 'type': 'integer', 'description': 'duration integer', 'title': 'get_markets_structures_structure_id_duration'}, 'price': {'format': 'float', 'type': 'number', 'description': 'price number', 'title': 'get_markets_structures_structure_id_price'}, 'location_id': {'format': 'int64', 'type': 'integer', 'description': 'location_id integer', 'title': 'get_markets_structures_structure_id_location_id'}, 'min_volume': {'format': 'int32', 'type': 'integer', 'description': 'min_volume integer', 'title': 'get_markets_structures_structure_id_min_volume'}, 'range': {'enum': ['station', 'region', 'solarsystem', '1', '2', '3', '4', '5', '10', '20', '30', '40'], 'type': 'string', 'description': 'range string', 'title': 'get_markets_structures_structure_id_range'}, 'issued': {'format': 'date-time', 'type': 'string', 'description': 'issued string', 'title': 'get_markets_structures_structure_id_issued'}, 'is_buy_order': {'type': 'boolean', 'description': 'is_buy_order boolean', 'title': 'get_markets_structures_structure_id_is_buy_order'}, 'order_id': {'format': 'int64', 'type': 'integer', 'description': 'order_id integer', 'title': 'get_markets_structures_structure_id_order_id'}, 'volume_total': {'format': 'int32', 'type': 'integer', 'description': 'volume_total integer', 'title': 'get_markets_structures_structure_id_volume_total'}, 'volume_remain': {'format': 'int32', 'type': 'integer', 'description': 'volume_remain integer', 'title': 'get_markets_structures_structure_id_volume_remain'}, 'type_id': {'format': 'int32', 'type': 'integer', 'description': 'type_id integer', 'title': 'get_markets_structures_structure_id_type_id'}}, 'description': '200 ok object', 'required': ['order_id', 'type_id', 'location_id', 'volume_total', 'volume_remain', 'min_volume', 'price', 'is_buy_order', 'duration', 'issued', 'range']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_markets_structures_structure_id_ok'}, 'examples': {'application/json': [{'duration': 90, 'price': 9.9, 'location_id': 60005599, 'min_volume': 1, 'range': 'region', 'issued': '2016-09-03T05:12:25Z', 'is_buy_order': False, 'order_id': 4623824223, 'volume_total': 2000000, 'volume_remain': 1296000, 'type_id': 34}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of orders'}}

    def get(self, structure_id, datasource="tranquility",page=1,**kwargs):
        """
                Return all orders in a structure
        
        ---
        
        Alternate route: `/v1/markets/structures/{structure_id}/`
        
        Alternate route: `/legacy/markets/structures/{structure_id}/`
        
        Alternate route: `/dev/markets/structures/{structure_id}/`
        
        
        ---
        
        This route is cached for up to 300 seconds

:type structure_id: int
        :param structure_id: Return orders in this structure
:type datasource: str
        :param datasource: The server name you would like data from
:type page: int
        :param page: Which page to query, starting at 1
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"structure_id" : structure_id, "datasource" : datasource, "page" : page, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class MarketsDetailHistory(object):
    base_url = "https://esi.tech.ccp.is/latest/markets/{region_id}/history/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_markets_region_id_history_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_markets_region_id_history_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'title': 'get_markets_region_id_history_200_ok', 'type': 'object', 'properties': {'date': {'format': 'date', 'type': 'string', 'description': 'The date of this historical statistic entry', 'title': 'get_markets_region_id_history_date'}, 'highest': {'format': 'float', 'type': 'number', 'description': 'highest number', 'title': 'get_markets_region_id_history_highest'}, 'average': {'format': 'float', 'type': 'number', 'description': 'average number', 'title': 'get_markets_region_id_history_average'}, 'order_count': {'format': 'int64', 'type': 'integer', 'description': 'Total number of orders happened that day', 'title': 'get_markets_region_id_history_order_count'}, 'lowest': {'format': 'float', 'type': 'number', 'description': 'lowest number', 'title': 'get_markets_region_id_history_lowest'}, 'volume': {'format': 'int64', 'type': 'integer', 'description': 'Total', 'title': 'get_markets_region_id_history_volume'}}, 'description': '200 ok object', 'required': ['date', 'order_count', 'volume', 'highest', 'average', 'lowest']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_markets_region_id_history_ok'}, 'examples': {'application/json': [{'date': '2015-05-01', 'highest': 5.27, 'average': 5.25, 'order_count': 2267, 'lowest': 5.11, 'volume': 16276782035}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of historical market statistics'}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Unprocessable entity message', 'title': 'get_markets_region_id_history_422_unprocessable_entity'}}, 'description': 'Unprocessable entity', 'title': 'get_markets_region_id_history_unprocessable_entity'}, 'examples': {'application/json': {'error': 'Unprocessable entity message'}}, 'description': 'Not found'}}

    def get(self, region_id, type_id, datasource="tranquility",**kwargs):
        """
                Return a list of historical market statistics for the specified type in a region
        
        ---
        
        Alternate route: `/v1/markets/{region_id}/history/`
        
        Alternate route: `/legacy/markets/{region_id}/history/`
        
        Alternate route: `/dev/markets/{region_id}/history/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type region_id: int
        :param region_id: Return statistics in this region
:type type_id: int
        :param type_id: Return statistics for this type
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"region_id" : region_id, "type_id" : type_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class MarketsPrices(object):
    base_url = "https://esi.tech.ccp.is/latest/markets/prices/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_markets_prices_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_markets_prices_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'title': 'get_markets_prices_200_ok', 'type': 'object', 'properties': {'adjusted_price': {'format': 'float', 'type': 'number', 'description': 'adjusted_price number', 'title': 'get_markets_prices_adjusted_price'}, 'average_price': {'format': 'float', 'type': 'number', 'description': 'average_price number', 'title': 'get_markets_prices_average_price'}, 'type_id': {'format': 'int32', 'type': 'integer', 'description': 'type_id integer', 'title': 'get_markets_prices_type_id'}}, 'description': '200 ok object', 'required': ['type_id']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_markets_prices_ok'}, 'examples': {'application/json': [{'adjusted_price': 306988.09, 'average_price': 306292.67, 'type_id': 32772}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of prices'}}

    def get(self, datasource="tranquility",**kwargs):
        """
                Return a list of prices
        
        ---
        
        Alternate route: `/v1/markets/prices/`
        
        Alternate route: `/legacy/markets/prices/`
        
        Alternate route: `/dev/markets/prices/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)