# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class SqlStoredProcedure(Resource):
    """An Azure Cosmos DB stored procedure.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The unique resource identifier of the database account.
    :vartype id: str
    :ivar name: The name of the database account.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param sql_stored_procedure_id: Name of the Sql Stored Procedure
    :type sql_stored_procedure_id: str
    :param body: Body of the Stored Procedure
    :type body: str
    :param _rid: A system generated property. A unique identifier.
    :type _rid: str
    :param _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :type _ts: object
    :param _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :type _etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sql_stored_procedure_id': {'key': 'properties.id', 'type': 'str'},
        'body': {'key': 'properties.body', 'type': 'str'},
        '_rid': {'key': 'properties._rid', 'type': 'str'},
        '_ts': {'key': 'properties._ts', 'type': 'object'},
        '_etag': {'key': 'properties._etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SqlStoredProcedure, self).__init__(**kwargs)
        self.sql_stored_procedure_id = kwargs.get('sql_stored_procedure_id', None)
        self.body = kwargs.get('body', None)
        self._rid = kwargs.get('_rid', None)
        self._ts = kwargs.get('_ts', None)
        self._etag = kwargs.get('_etag', None)
