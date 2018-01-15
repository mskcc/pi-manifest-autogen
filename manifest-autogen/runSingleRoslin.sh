#!/bin/bash

curDir=$(pwd)

source $curDir/config.sh

cd $(dirname $0)

#run for ROSLIN
echo "Running single create manifest for ROSLIN with version ${roslinVersion}"
/home/reza/jdk/bin/java -jar -Dspring.profiles.active=dev,igo,hold /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${roslinVersion}.jar -p $1 $2

cd ${curDir}

