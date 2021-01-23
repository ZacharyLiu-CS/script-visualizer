#!/bin/bash
cpu=`top -b -n1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' '{split($1, vs, ","); v=vs[length(vs)]; sub(/\s+/, "", v);sub(/\s+/, "", v); printf "%.2f", 100-v;}'`
echo $cpu
mem_used_persent=`free -m | awk -F '[ : ]+' 'NR==2{printf "%.2f", $3/$2*100}'`
echo $mem_used_persent
mem_cached_persent=`free -m | awk -F '[ : ]+' 'NR==2{printf "%.2f", $6/$2*100}'`
echo $mem_cached_persent
