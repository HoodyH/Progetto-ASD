#!/bin/bash
# Dove il primo parametro ($1) sarà il nome dello studente
# il secondo ($2) serve a lanciare il programma
# il terzo ($3) serve per il file

clear
path="test"
mkdir $path/$1
for i in {1..5}
do
echo "run test on in-$i"
./$2 $3 < $path/in-$i > $path/$1/out-$i
done
