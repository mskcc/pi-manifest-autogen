source /ifs/work/pi/pipelineKickoff/dev/config.sh

curDir=$(pwd)

cd $(dirname $0)

/home/reza/jdk/bin/java -jar -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5006 -Dspring.profiles.active=dev,igo /ifs/work/pi/pipelineKickoff/lib/pipeline-kickoff-${roslinVersion}.jar -p $1 $2

cd ${curDir}

