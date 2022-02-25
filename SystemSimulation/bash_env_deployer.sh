#!/bin/bash
# Job name:
#SBATCH --job-name=offshore_wind_turbines
#
# Account:
#SBATCH --account=fc_ntugame
#
# Partition:
#SBATCH --partition=savio2_gpu
#
# Number of nodes:
#SBATCH --nodes=1
#
# Number of tasks (one for each GPU desired for use case) (example):
#SBATCH --ntasks=1
#
# Processors per task (please always specify the total number of processors twice the number of GPUs):
#SBATCH --cpus-per-task=2
#
#Number of GPUs, this can be in the format of "gpu:[1-4]", or "gpu:K80:[1-4] with the type included
#SBATCH --gres=gpu:K80:1
#
# Wall clock limit (8hrs):
#SBATCH --time=20:00:00
#
# Run 48 examples concurrently
#SBATCH --array=0

module load matlab/r2021b
python csv_initializer.py $1
matlab -nosplash -nodesktop -r "run('/global/scratch/users/lucas_spangher/FOWFSimDyn1/SystemSimulation/MainScript.m'); exit;"