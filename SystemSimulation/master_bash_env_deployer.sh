#!/bin/bash

for i in $(seq 1 $1); do 
    echo $i
    sbatch bash_env_deployer.sh i
done
