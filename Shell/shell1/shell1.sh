sed 's/.*:.:.*://g' | sed 's/,/\n/g' | sed '/^$/d' | sort | uniq -c | sort -r

