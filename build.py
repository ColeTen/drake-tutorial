#  This program is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version. This program
#  is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
#  the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see
#  <https://www.gnu.org/licenses/>.

import os
from sphinx.application import Sphinx


def build_sphinx_docs(source_dir: str, build_dir: str, doctree_dir: str):
    """
    Build HTML documentation using Sphinx.

    Args:
        source_dir:
            Path to the Sphinx source directory (where conf.py and .rst files are
            located).

        build_dir:
            Path to the output directory for the generated HTML files.

        doctree_dir:
            Path to store intermediate doctree files.
    """
    # Ensure the output and doctree directories exist
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(doctree_dir, exist_ok=True)

    # Create the Sphinx application instance
    app = Sphinx(
        srcdir=source_dir,
        confdir=source_dir,  # Typically, conf.py is in the source directory
        outdir=build_dir,
        doctreedir=doctree_dir,
        buildername="html",  # Specify the builder (e.g., "html" for HTML documentation)
    )

    # Run the build process
    app.build()

    # Check if the build was successful
    if app.statuscode == 0:
        print(f"Documentation successfully built at: {build_dir}")
    else:
        print(f"Build failed with status code: {app.statuscode}")


if __name__ == "__main__":
    source_directory = "./docs/source"
    build_directory = "./docs/build"
    doctree_directory = "./docs/build/doctrees"

    build_sphinx_docs(source_directory, build_directory, doctree_directory)
