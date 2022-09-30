# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    eventhubsender_name_type = CLIArgumentType(options_list='--eventhubsender-name-name', help='Name of the Eventhubsender.', id_part='name')

    with self.argument_context('eventhubsender') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventhubsender_name', eventhubsender_name_type, options_list=['--name', '-n'])

    with self.argument_context('eventhubsender list') as c:
        c.argument('eventhubsender_name', eventhubsender_name_type, id_part=None)
