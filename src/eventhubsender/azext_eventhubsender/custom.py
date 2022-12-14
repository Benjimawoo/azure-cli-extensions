# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_eventhubsender(cmd, resource_group_name, eventhubsender_name, location=None, tags=None):
    raise CLIError('TODO: Implement `eventhubsender create`')


def list_eventhubsender(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `eventhubsender list`')


def update_eventhubsender(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance