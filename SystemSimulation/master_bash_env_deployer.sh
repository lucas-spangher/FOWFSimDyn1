#!/bin/bash

module load python/3.6
python csv_initializer.py 

for i in $(seq 1 $1); do 
    echo $i
    sbatch bash_env_deployer.sh 
done
