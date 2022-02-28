"""

Copyright (C) 2019-2022 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""

from scompose.project import Project


def main(args, parser, extra):
    """execute a command to an instance."""
    # Initialize the project
    project = Project(
        filename=args.file, name=args.project_name, env_file=args.env_file
    )

    project.execute(args.name[0], extra)
