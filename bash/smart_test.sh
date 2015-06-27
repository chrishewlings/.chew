#!/bin/bash

set -eo pipefail


export IFS=$'\n\t'
export TEMP="/var/tmp"

declare -a disk_array
declare -a compatible_disks_array

i=0
for disk in /dev/disk?
do
	disk_array[i]=$disk
    ((++i))
done

for element in ${disk_array[@]}
do
    diskutil info "$element" | grep -q -E "Protocol: +SATA" 
    OUT=$?
    if [ $OUT -eq 0 ]; then
        compatible_disks_array=("${compatible_disks_array[@]}" "$element")
    fi
done

for disk in ${compatible_disks_array[@]}
do
	printf "Status of $disk:\n\n"
    $TEMP/smartctl -A -f brief $disk | grep -E "Reallocated_S|Runtime_Bad|Uncorrectable|Pending|UDMA_CRC" | /usr/bin/awk '{print $2,"\t","\t",$NF}'
    printf "\n"
done


#cd $TEMP

#curl -s -L http://bit.ly/1KgMRde | tar -xvf- -C . > /dev/null
#$TEMP/smartctl 
