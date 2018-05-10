#!/bin/bash

curDir=$(pwd)

source $curDir/config.sh

cd $(dirname $0)

#run for ROSLIN
echo "Running single create manifest for ROSLIN with version ${roslinVersion}"
/ifs/work/pi/lib/jdk1.8.0_131/bin/java -jar -Dspring.profiles.active=dev,igo,hold -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5006 /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${roslinVersion}.jar -p $1 $2

cd ${curDir}

