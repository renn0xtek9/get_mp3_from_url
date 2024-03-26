DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"/../get_mp3_from_url/

python3 setup.py sdist bdist_wheel
twine upload dist/*
