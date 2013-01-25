#!/bin/bash

#Creates symbolic Link to workflows in Alfred

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
WORKFLOW_DIR=~/Library/Application\ Support/Alfred\ 2/Alfred.alfredpreferences/workflows
DOMAIN=com.peteokma

cd "$WORKFLOW_DIR"
IFS=$'\n';for f in $(ls -d $DIR/workflows/*)
do
    ln -fs $f com.peteokma.`basename $f`
done