#!/bin/sh

curDir=$(dirname $0)
source $curDir/constants.sh
cd $curDir

$pythonPath regeneration/regenerate.py
