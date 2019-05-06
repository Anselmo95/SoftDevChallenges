cat auth.log | -- remenber to delete this line
egrep '(Failed|Accepted)' |
sed 's/^.\+\(Accepted\).\+from/A/' |
sed 's/^.\+\(Failed\).\+from/F/' |
sed 's/ port.\+$//' |
sort |
awk '
{ 
	if($1 == "A"){
		accepted[$2]++
	}else{
		failed[$2]++
	}
}
END {	for (ip in accepted){
			if(failed[ip] > accepted[ip])
				print ip, failed[ip], accepted[ip]
		} 
}'

