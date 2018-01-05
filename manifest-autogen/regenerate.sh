#!/bin/sh

source /ifs/work/pi/pipelineKickoff/config.sh
source /ifs/work/pi/lib/bash/b-log.sh

curDir=$(dirname $0)

source $curDir/constants.sh
source $curDir/notification-config.sh
source $curDir/log-config.sh
source $curDir/rest-config.sh

cd $curDir

$pythonPath regeneration/regenerate.py
