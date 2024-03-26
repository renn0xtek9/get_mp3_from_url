#!/bin/bash
set -euxo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"/..
pip uninstall -y package_foobar
pip install -e package_foobar

#Check
python3 -c "import package_foobar"

# Consider running package_foobar with -h to check
# that it runs correctly after installation
# package_foobar -h
