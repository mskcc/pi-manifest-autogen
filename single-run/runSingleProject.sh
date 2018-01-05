#!/bin/bash

source /ifs/work/pi/pipelineKickoff/dev/config.sh

curDir=$(pwd)

cd $(dirname $0)

# run for BIC
/home/reza/jdk/bin/java -jar -Dspring.profiles.active=dev,igo /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${bicVersion}.jar -p $1 $2

#run for ROSLIN
/home/reza/jdk/bin/java -jar -Dspring.profiles.active=dev,igo /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${roslinVersion}.jar -p $1 $2

cd ${curDir}

