# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

"""
Non-database domain objects used to describe content types.
"""

class TypeDescriptor:
    """
    Carries information on a single type descriptor.
    """

    def __init__(self, filename, contents):
        """
        @param filename: name of the file from which the contents were
                         extracted (used for identification purposes in
                         logging and errors)
        @type  filename: str

        @param contents: contents read from the descriptor
        @type  contents: str
        """
        self.filename = filename
        self.contents = contents
        self.parsed = None  # stores the parsed version of the contents

class TypeDefinition:
    """
    Once a type descriptor has been parsed, instances of this class will
    describe the types to be loaded.
    """

    def __init__(self, id, display_name, description, unique_indexes, search_indexes, child_types):
        self.id = id
        self.display_name = display_name
        self.description = description

        if not isinstance(unique_indexes, list) and not isinstance(unique_indexes, tuple):
            unique_indexes = [unique_indexes]

        if not isinstance(search_indexes, list) and not isinstance(search_indexes, tuple):
            search_indexes = [search_indexes]

        if not isinstance(child_types, list) and not isinstance(child_types, tuple):
            child_types = [child_types]

        self.unique_indexes = unique_indexes
        self.search_indexes = search_indexes
        self.child_types = child_types
