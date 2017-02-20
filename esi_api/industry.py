# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class IndustryFacilities(object):
    base_url = "https://esi.tech.ccp.is/latest/industry/facilities/"

    get_responses = {'200': {'headers': {'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of prices', 'examples': {'application/json': [{'owner_id': 1000126, 'facility_id': 60012544, 'solar_system_id': 30000032, 'type_id': 2502, 'tax': 0.1, 'region_id': 10000001}]}, 'schema': {'title': 'get_industry_facilities_ok', 'type': 'array', 'description': '200 ok array', 'items': {'title': 'get_industry_facilities_200_ok', 'type': 'object', 'description': '200 ok object', 'required': ['facility_id', 'owner_id', 'type_id', 'solar_system_id', 'region_id'], 'properties': {'owner_id': {'type': 'integer', 'format': 'int32', 'description': 'Owner of the facility', 'title': 'get_industry_facilities_owner_id'}, 'facility_id': {'type': 'integer', 'format': 'int64', 'description': 'ID of the facility', 'title': 'get_industry_facilities_facility_id'}, 'solar_system_id': {'type': 'integer', 'format': 'int32', 'description': 'Solar system ID where the facility is', 'title': 'get_industry_facilities_solar_system_id'}, 'type_id': {'type': 'integer', 'format': 'int32', 'description': 'Type ID of the facility', 'title': 'get_industry_facilities_type_id'}, 'tax': {'type': 'number', 'format': 'float', 'description': 'Tax imposed by the facility', 'title': 'get_industry_facilities_tax'}, 'region_id': {'type': 'integer', 'format': 'int32', 'description': 'Region ID where the facility is', 'title': 'get_industry_facilities_region_id'}}}}}, '500': {'description': 'Internal server error', 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'schema': {'title': 'get_industry_facilities_internal_server_error', 'type': 'object', 'description': 'Internal server error', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_industry_facilities_500_internal_server_error'}}}}}
    parameter = [{'name': 'datasource', 'default': 'tranquility', 'enum': ['tranquility', 'singularity'], 'type': 'string', 'in': 'query', 'description': 'The server name you would like data from'}, {'name': 'user_agent', 'type': 'string', 'in': 'query', 'description': 'Client identifier, takes precedence over headers'}, {'name': 'X-User-Agent', 'type': 'string', 'in': 'header', 'description': 'Client identifier, takes precedence over User-Agent'}]
    def get(self, datasource= "tranquility",**kwargs
    ):
        """
                Return a list of industry facilities
        
        ---
        
        Alternate route: `/v1/industry/facilities/`
        
        Alternate route: `/legacy/industry/facilities/`
        
        Alternate route: `/dev/industry/facilities/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

        :type datasource: str
        :param datasource: The server name you would like data from

        :type user_agent: str
        :param user_agent: Client identifier, takes precedence over headers

        :type x_user_agent: str
        :param x_user_agent: Client identifier, takes precedence over User-Agent

        """
        kwargs_dict ={"datasource" : datasource, "user_agent" : user_agent, "X-User-Agent" : x_user_agent, }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class IndustrySystems(object):
    base_url = "https://esi.tech.ccp.is/latest/industry/systems/"

    get_responses = {'200': {'headers': {'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of cost indicies', 'examples': {'application/json': [{'cost_indices': [{'activity': 'invention', 'cost_index': 0.00480411064973412}], 'solar_system_id': 30011392}]}, 'schema': {'title': 'get_industry_systems_ok', 'type': 'array', 'description': '200 ok array', 'items': {'title': 'get_industry_systems_200_ok', 'type': 'object', 'description': '200 ok object', 'required': ['solar_system_id', 'cost_indices'], 'properties': {'cost_indices': {'title': 'get_industry_systems_cost_indices', 'type': 'array', 'description': 'cost_indices array', 'items': {'title': 'get_industry_systems_cost_indice', 'type': 'object', 'description': 'cost_indice object', 'required': ['activity', 'cost_index'], 'properties': {'activity': {'title': 'get_industry_systems_activity', 'type': 'string', 'description': 'activity string', 'enum': ['none', 'manufacturing', 'researching_technology', 'researching_time_efficiency', 'researching_material_efficiency', 'copying', 'duplicating', 'invention', 'reverse_engineering']}, 'cost_index': {'type': 'number', 'format': 'float', 'description': 'cost_index number', 'title': 'get_industry_systems_cost_index'}}}}, 'solar_system_id': {'type': 'integer', 'format': 'int32', 'description': 'solar_system_id integer', 'title': 'get_industry_systems_solar_system_id'}}}}}, '500': {'description': 'Internal server error', 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'schema': {'title': 'get_industry_systems_internal_server_error', 'type': 'object', 'description': 'Internal server error', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_industry_systems_500_internal_server_error'}}}}}
    parameter = [{'name': 'datasource', 'default': 'tranquility', 'enum': ['tranquility', 'singularity'], 'type': 'string', 'in': 'query', 'description': 'The server name you would like data from'}, {'name': 'user_agent', 'type': 'string', 'in': 'query', 'description': 'Client identifier, takes precedence over headers'}, {'name': 'X-User-Agent', 'type': 'string', 'in': 'header', 'description': 'Client identifier, takes precedence over User-Agent'}]
    def get(self, datasource= "tranquility",**kwargs
    ):
        """
                Return cost indices for solar systems
        
        ---
        
        Alternate route: `/v1/industry/systems/`
        
        Alternate route: `/legacy/industry/systems/`
        
        Alternate route: `/dev/industry/systems/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

        :type datasource: str
        :param datasource: The server name you would like data from

        :type user_agent: str
        :param user_agent: Client identifier, takes precedence over headers

        :type x_user_agent: str
        :param x_user_agent: Client identifier, takes precedence over User-Agent

        """
        kwargs_dict ={"datasource" : datasource, "user_agent" : user_agent, "X-User-Agent" : x_user_agent, }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)