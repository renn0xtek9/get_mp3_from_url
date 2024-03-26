#!/bin/bash
set -euxo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"/..
pip uninstall -y get_mp3_from_url
pip install -e get_mp3_from_url

#Check
python3 -c "import get_mp3_from_url"

# Consider running get_mp3_from_url with -h to check
# that it runs correctly after installation
# get_mp3_from_url -h
