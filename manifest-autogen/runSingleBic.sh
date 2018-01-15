#!/bin/bash

curDir=$(pwd)

source $curDir/config.sh

cd $(dirname $0)

#run for BIC
echo "Running single create manifest for BIC with version ${bicVersion}"

/home/reza/jdk/bin/java -jar -Dspring.profiles.active=dev,igo /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${bicVersion}.jar -p $1 $2

cd ${curDir}

