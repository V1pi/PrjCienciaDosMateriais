from ase.build import graphene_nanoribbon
from ase.visualize import view
from ase import units
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md import MDLogger
from ase.md.npt import NPT
import numpy as np

gnrb = graphene_nanoribbon(20, 20, type="armchair", saturated=True, vacuum = 3.5)
view(gnrb)
gnrb.set_calculator(EMT())
dyn = VelocityVerlet(gnrb, dt=5.0 * units.fs)
# dyn = Langevin(gnrb, 5 * units.fs, units.kB * 123, 0.002)
stress = 2
# dyn = NPT(gnrb, 5*units.fs, 300*units.kB, stress, 25*units.fs, 75*units.fs)
dyn.attach(MDLogger(dyn, gnrb, 'md2.log', header=True, stress=False,
           peratom=True, mode="w"), interval=1)
dyn.run(100)
# view(gnrb)
