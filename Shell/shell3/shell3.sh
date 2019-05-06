#!/bin/bash
now=$(date --date='-1 month' +%s)

function maze_explorer {

	local compress_dir=0
	local arr=()
	for dir in "$1"/* 
	do
		if [ -d $dir ];	then
			pushd $dir > /dev/null
			# Use parentheses because if yoy dont do it dir is seen as#
			# a global variable so its walue is overwritten by each call 
			# function, the () execute the new call in a new subshell so no
			# variabe is shered
			(maze_explorer $dir)
			local ret="$?"
			compress_dir=$(($compress_dir|$ret))
			popd > /dev/null
			if (($ret == 0)); then
				arr+=$dir
			fi

		fi
	done

	local compress=0
	if [ -z "$2" ]; then
		for file in "$1"/* 
		do
		if [ ! -d $file ];	then
			tmp=$(stat -c %X $file)
			if [ "$tmp" -gt "$now" ]; then
				compress=1
			fi
		fi
		done

			local ret_value=$(($compress|$compress_dir))
			if [ "$ret_value" -ne "0" ]; then
			 	for i in "${arr[@]}"; do
					tar --remove-files -zcf $(basename $i).tgz $i 2> /dev/null
			 	done
			fi 
			return $ret_value
	fi

}

path=$(pwd)

maze_explorer $path 0