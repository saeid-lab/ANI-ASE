# ANI-ASE
A Simple code for calculating Energy, Frequencies, Thermochemistry, and Optimization structure using TorchANI and USE Interface


### Requirements
```
1.Pytorch:
conda install pytorch torchvision cpuonly -c pytorch
or
pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

2.TorhcANI:
pip install torchani

3.ASE:
conda install -c conda-forge ase 

```

## Usage
```python3 ANI-SUMMARY.py [Input] [Input_format] [Optimize(0 or 1)]```

```
Input: can be given in any format.
Input_format: Specify input format file: pdb,xyz,gaussian,...
Optimize: o for not opt, 1 for opt
```

outputs:
>1. output.txt
Energies, Frequencies, Thermochemistry can be found in output.txt

> 2.Trajectory.traj
Trajectories during optimization

> 3.vib.xyz
Normal Modes of given system, and can be open using Jmol.
