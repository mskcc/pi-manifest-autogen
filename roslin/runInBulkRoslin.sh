#!/bin/bash

curDir=$(pwd)

source $curDir/config.sh

cd $(dirname $0)

projects=(
07951_D
07951_E
07951_I
07951_H
93017
06287_H
07995
05851_L
04926_V
07958
07737_C
4773
04430_AE
04430_AD
07037_AH
06287_L
07037_AF
05526_J
07618_C
08010
05469_AB
05816_AL
05304_O
07391_K
08054
07618_D
10000_F
04430_AF
05469_AD
05469_AC
07078_G
05538_AB
06287_P
07737_C
07037_AG
06725_S
07951_F
07668_D
07814_C
07951_G
05791_F
06287_O
07668_C
05971_J
06208_H
06287_I
07951_C
07951_B
07951
07833_B
)

for project in ${projects[*]}
do
	echo "Running Create Manifest for project $project"
	sh ./runSingleRoslin.sh $project
done

cd ${curDir}

