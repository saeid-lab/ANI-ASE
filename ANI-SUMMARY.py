__author__ = "Saeid Ekrami"
__license__ = "GPL"
__version__ = "0.1"


import sys 
import torchani
from ase.io import read


file = open('output.txt', 'a')
sys.stdout = file


molecule = read(sys.argv[1], format=sys.argv[2])
model = torchani.models.ANI1x().double()
molecule.set_calculator(model.ase())

print('INPUT TYPE:',sys.argv[2],'\n')
print('START ENERGY CALCULATION:\n')
En = molecule.get_potential_energy()
print('Energy as EV:',En,'eV')

from ase.units import Hartree
print('Energy as hartee:',En/Hartree,'Hartree')
print('END OF ENERGY CALCULATION\n')




if sys.argv[3] == '1':
	from ase.optimize import BFGS
	print('START OPT CALCULATION:\n')
	dyn = BFGS(atoms=molecule,trajectory='Trajectory.traj')
	dyn.run(fmax=0.00001)
	print('\n***OPTED ENERGIES:\n')
	En = molecule.get_potential_energy()
	print('***Energy as EV:',En,'eV')
	from ase.units import Hartree
	print('***Energy as hartee:',En/Hartree,'Hartree')
	print('***END OF OPT CALCULATION\n')


elif sys.argv[4] == '0':
	print("***Without OPTIMIZITION***\n")

else:
	print("choose only 1 or 0")




print('START FREQ CALCULATION:\n')

from ase.vibrations import Vibrations
vib = Vibrations(molecule)
vib.run()
vib.combine()
print('END OF FREQ CALCULATION\n')
print('VIBRATIONAL SUMMARY:\n')
vib.summary()
print('\nWRITING NORMAL MODE\n')
vib.write_jmol()
print('.')
print('.')
print('use JMOL for viewing of the modes')
print('.')
print('.')
print('DONE\n\n')



from ase.thermochemistry import IdealGasThermo
print("Thermochemistry DATA:\n'BY Ideal-gas limit'")
vib_energies = vib.get_energies()
potentialenergy = molecule.get_potential_energy()

thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=potentialenergy,
                        atoms=molecule,
                        geometry='linear',
                        symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)


print('FINISH!')
print('{CODED BY SAEID EKRAMI}')


file.close()

