#!/bin/bash

set -u
set -e


name="__my_new_app_name__fix_me__"

if [[ $name == "__my_new_app_name__fix_me__" ]];
then
    echo "edit this script and edit the variable 'name'"
fi

find '.vscode' -type f '*.*' -exec sed -i "s/example_ds_app/${name}/g" {}/;
find example_ds_app -iname '*.py' -exec sed -i "s/example_ds_app/${name}/g" {}/;

mv example_ds_app $name

sed -i "s/example_ds_app/${name}/g" pyproject.toml
sed -i "s/example_ds_app/${name}/g" launch.sh
sed -i "s/example_ds_app/${name}/g" docker-compose.yml

