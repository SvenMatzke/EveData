# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class DogmaEffectsDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/dogma/effects/{effect_id}/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_dogma_effects_effect_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_dogma_effects_effect_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'title': 'get_dogma_effects_effect_id_ok', 'type': 'object', 'properties': {'post_expression': {'format': 'int32', 'type': 'integer', 'description': 'post_expression integer', 'title': 'get_dogma_effects_effect_id_post_expression'}, 'is_offensive': {'type': 'boolean', 'description': 'is_offensive boolean', 'title': 'get_dogma_effects_effect_id_is_offensive'}, 'electronic_chance': {'type': 'boolean', 'description': 'electronic_chance boolean', 'title': 'get_dogma_effects_effect_id_electronic_chance'}, 'is_warp_safe': {'type': 'boolean', 'description': 'is_warp_safe boolean', 'title': 'get_dogma_effects_effect_id_is_warp_safe'}, 'range_chance': {'type': 'boolean', 'description': 'range_chance boolean', 'title': 'get_dogma_effects_effect_id_range_chance'}, 'disallow_auto_repeat': {'type': 'boolean', 'description': 'disallow_auto_repeat boolean', 'title': 'get_dogma_effects_effect_id_disallow_auto_repeat'}, 'duration_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'duration_attribute_id integer', 'title': 'get_dogma_effects_effect_id_duration_attribute_id'}, 'tracking_speed_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'tracking_speed_attribute_id integer', 'title': 'get_dogma_effects_effect_id_tracking_speed_attribute_id'}, 'display_name': {'type': 'string', 'description': 'display_name string', 'title': 'get_dogma_effects_effect_id_display_name'}, 'effect_id': {'format': 'int32', 'type': 'integer', 'description': 'effect_id integer', 'title': 'get_dogma_effects_effect_id_effect_id'}, 'falloff_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'falloff_attribute_id integer', 'title': 'get_dogma_effects_effect_id_falloff_attribute_id'}, 'icon_id': {'format': 'int32', 'type': 'integer', 'description': 'icon_id integer', 'title': 'get_dogma_effects_effect_id_icon_id'}, 'range_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'range_attribute_id integer', 'title': 'get_dogma_effects_effect_id_range_attribute_id'}, 'pre_expression': {'format': 'int32', 'type': 'integer', 'description': 'pre_expression integer', 'title': 'get_dogma_effects_effect_id_pre_expression'}, 'discharge_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'discharge_attribute_id integer', 'title': 'get_dogma_effects_effect_id_discharge_attribute_id'}, 'effect_category': {'format': 'int32', 'type': 'integer', 'description': 'effect_category integer', 'title': 'get_dogma_effects_effect_id_effect_category'}, 'name': {'type': 'string', 'description': 'name string', 'title': 'get_dogma_effects_effect_id_name'}, 'is_assistance': {'type': 'boolean', 'description': 'is_assistance boolean', 'title': 'get_dogma_effects_effect_id_is_assistance'}, 'published': {'type': 'boolean', 'description': 'published boolean', 'title': 'get_dogma_effects_effect_id_published'}, 'description': {'type': 'string', 'description': 'description string', 'title': 'get_dogma_effects_effect_id_description'}, 'modifiers': {'items': {'title': 'get_dogma_effects_effect_id_modifier', 'type': 'object', 'properties': {'modifying_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'modifying_attribute_id integer', 'title': 'get_dogma_effects_effect_id_modifying_attribute_id'}, 'modified_attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'modified_attribute_id integer', 'title': 'get_dogma_effects_effect_id_modified_attribute_id'}, 'func': {'type': 'string', 'description': 'func string', 'title': 'get_dogma_effects_effect_id_func'}, 'domain': {'type': 'string', 'description': 'domain string', 'title': 'get_dogma_effects_effect_id_domain'}, 'operator': {'format': 'int32', 'type': 'integer', 'description': 'operator integer', 'title': 'get_dogma_effects_effect_id_operator'}}, 'description': 'modifier object', 'required': ['func', 'domain', 'modified_attribute_id', 'modifying_attribute_id', 'operator']}, 'type': 'array', 'description': 'modifiers array', 'title': 'get_dogma_effects_effect_id_modifiers'}}, 'description': '200 ok object', 'required': ['effect_id']}, 'examples': {'application/json': {'post_expression': 131, 'is_offensive': False, 'electronic_chance': False, 'disallow_auto_repeat': False, 'range_chance': False, 'display_name': 'High power', 'effect_id': 12, 'is_warp_safe': False, 'description': 'Requires a high power slot.', 'pre_expression': 131, 'effect_category': 0, 'name': 'hiPower', 'is_assistance': False, 'published': True, 'icon_id': 293}}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'Information about a dogma effect'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'get_dogma_effects_effect_id_404_not_found'}}, 'description': 'Not found', 'title': 'get_dogma_effects_effect_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': 'Dogma effect not found'}}

    def get(self, effect_id, datasource="tranquility",**kwargs):
        """
                Get information on a dogma effect
        
        ---
        
        Alternate route: `/v1/dogma/effects/{effect_id}/`
        
        Alternate route: `/legacy/dogma/effects/{effect_id}/`
        
        Alternate route: `/dev/dogma/effects/{effect_id}/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type effect_id: int
        :param effect_id: A dogma effect ID
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"effect_id" : effect_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class DogmaAttributesDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/dogma/attributes/{attribute_id}/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_dogma_attributes_attribute_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_dogma_attributes_attribute_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'title': 'get_dogma_attributes_attribute_id_ok', 'type': 'object', 'properties': {'display_name': {'type': 'string', 'description': 'display_name string', 'title': 'get_dogma_attributes_attribute_id_display_name'}, 'attribute_id': {'format': 'int32', 'type': 'integer', 'description': 'attribute_id integer', 'title': 'get_dogma_attributes_attribute_id_attribute_id'}, 'icon_id': {'format': 'int32', 'type': 'integer', 'description': 'icon_id integer', 'title': 'get_dogma_attributes_attribute_id_icon_id'}, 'high_is_good': {'type': 'boolean', 'description': 'high_is_good boolean', 'title': 'get_dogma_attributes_attribute_id_high_is_good'}, 'default_value': {'format': 'float', 'type': 'number', 'description': 'default_value number', 'title': 'get_dogma_attributes_attribute_id_default_value'}, 'unit_id': {'format': 'int32', 'type': 'integer', 'description': 'unit_id integer', 'title': 'get_dogma_attributes_attribute_id_unit_id'}, 'published': {'type': 'boolean', 'description': 'published boolean', 'title': 'get_dogma_attributes_attribute_id_published'}, 'name': {'type': 'string', 'description': 'name string', 'title': 'get_dogma_attributes_attribute_id_name'}, 'stackable': {'type': 'boolean', 'description': 'stackable boolean', 'title': 'get_dogma_attributes_attribute_id_stackable'}, 'description': {'type': 'string', 'description': 'description string', 'title': 'get_dogma_attributes_attribute_id_description'}}, 'description': '200 ok object', 'required': ['attribute_id']}, 'examples': {'application/json': {'display_name': 'Maximum Velocity Bonus', 'attribute_id': 20, 'icon_id': 1389, 'high_is_good': True, 'default_value': 1, 'unit_id': 124, 'published': True, 'name': 'speedFactor', 'stackable': False, 'description': 'Factor by which topspeed increases.'}}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'Information about a dogma attribute'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'get_dogma_attributes_attribute_id_404_not_found'}}, 'description': 'Not found', 'title': 'get_dogma_attributes_attribute_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': 'Dogma attribute not found'}}

    def get(self, attribute_id, datasource="tranquility",**kwargs):
        """
                Get information on a dogma attribute
        
        ---
        
        Alternate route: `/v1/dogma/attributes/{attribute_id}/`
        
        Alternate route: `/legacy/dogma/attributes/{attribute_id}/`
        
        Alternate route: `/dev/dogma/attributes/{attribute_id}/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type attribute_id: int
        :param attribute_id: A dogma attribute ID
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"attribute_id" : attribute_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class DogmaAttributes(object):
    base_url = "https://esi.tech.ccp.is/latest/dogma/attributes/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_dogma_attributes_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_dogma_attributes_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'format': 'int32', 'type': 'integer', 'description': '200 ok integer', 'title': 'get_dogma_attributes_200_ok'}, 'type': 'array', 'description': '200 ok array', 'title': 'get_dogma_attributes_ok'}, 'examples': {'application/json': [1, 2, 3]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of dogma attribute ids'}}

    def get(self, datasource="tranquility",**kwargs):
        """
                Get a list of dogma attribute ids
        
        ---
        
        Alternate route: `/v1/dogma/attributes/`
        
        Alternate route: `/legacy/dogma/attributes/`
        
        Alternate route: `/dev/dogma/attributes/`
        
        
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


class DogmaEffects(object):
    base_url = "https://esi.tech.ccp.is/latest/dogma/effects/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_dogma_effects_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_dogma_effects_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'format': 'int32', 'type': 'integer', 'description': '200 ok integer', 'title': 'get_dogma_effects_200_ok'}, 'type': 'array', 'description': '200 ok array', 'title': 'get_dogma_effects_ok'}, 'examples': {'application/json': [1, 2, 3]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of dogma effect ids'}}

    def get(self, datasource="tranquility",**kwargs):
        """
                Get a list of dogma effect ids
        
        ---
        
        Alternate route: `/v1/dogma/effects/`
        
        Alternate route: `/legacy/dogma/effects/`
        
        Alternate route: `/dev/dogma/effects/`
        
        
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