#!/bin/bash
FILES=/Users/ikeharakansuke/Documents/College_stuff/Course_Material/Network_Analysis_and_Modeling/Homework/Project/Partition/group_songs_tab/*
i = 0
for f in $FILES
do 
	cat $f | sort > ${i}.txt
	i=$((i+1))
done