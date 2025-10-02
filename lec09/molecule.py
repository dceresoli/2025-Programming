#!/usr/bin/env python

# Python class that repsresents a molecule
# 2025/2026 Programming for Chemistry @ University of Milano
import math


class Molecule:
    def __init__(self, name=""):
        """Create a empty molecule"""
        self.name = name
        self.atoms = []       # list of element symbols (e.g., ["C", "H", "H"])
        self.coordinates = [] # list of (x, y, z) tuples


    def add_atom(self, element, x, y, z):
        """Add one atom to the molecule"""
        self.atoms.append(element)
        self.coordinates.append((float(x), float(y), float(z)))


    def __len__(self):
        """Return the number of atoms"""
        return len(self.atoms)


    def __getitem__(self, idx):
        """Return the atom at position [idx]"""
        return self.atoms[idx], self.coordinates[idx]


    def __str__(self):
        """Return the name of the molecule"""
        return self.name if len(self.name) > 0 else "just a molecule"


    def __repr__(self):
        """Return more information"""
        return f'class Molecule: name={self.name} len={len(self.natoms)} atoms={self.atoms}'


    def __add__(a, b):
        """Join two molecules"""
        c = Molecule(f'{a.name} + {b.name}')
        
        for i in range(len(a)):
            atom, coord = a[i]
            c.add_atom(atom, *coord)
        
        for i in range(len(b)):
            atom, coord = b[i]
            c.add_atom(atom, *coord)
        return c


    def translate(self, dx, dy, dz):
        """Translate the molecule"""
        for i in range(len(self)):
            x, y, z = self.coordinates[i]
            self.coordinates[i] = (x+dx, y+dy, z+dz)


    def get_center(self):
        """Return the center of the molecule"""
        cx = cy = cz = 0.0
        natoms = len(self)
        for i in range(natoms):
            x, y, z = self.coordinates[i]
            cx += cx
            cy += cy
            cz += cz
        return cx/natoms, cy/natoms, cz/natoms
        
    
    def center(self):
        """Center the molecule to the origin"""
        cx, cy, cz = sefl.get_center()
        self.translate(-cx, -cy, -cz)
        
            
    @classmethod
    def from_xyz(cls, filename):
        """Create a molecule from an XYZ file."""
        with open(filename, "r") as f:
            lines = f.readlines()

        natoms = int(lines[0])
        name = lines[1].strip()
        
        mol = cls(name)
        for line in lines[2:2+natoms]:
            parts = line.split()
            element, x, y, z = parts[0], parts[1], parts[2], parts[3]
            mol.add_atom(element, x, y, z)
        return mol


    def to_xyz(self, filename):
        """Save molecule to an XYZ file."""
        with open(filename, "w") as f:
            f.write(f"{len(self.atoms)}\n")
            f.write(f"{self.name}\n")
            for atom, (x, y, z) in zip(self.atoms, self.coordinates):
                f.write(f"{atom:2s} {x:15.8f} {y:15.8f} {z:15.8f}\n")
                

    # this is a class variable
    __bohr = 0.52917721

    def bohr_to_angstrom(self):
       """Convert the coordinates from bohr to angstrom"""
       for i in range(len(self)):
           x, y, z = self.coordinates[i]
           self.coordinates[i] = (x*Molecule.__bohr, y*Molecule.__bohr, z*Molecule.__bohr)
           
    def angstrom_to_bohr(self):
       """Convert the coordinates from angstrom to bohr"""
       for i in range(len(self)):
           x, y, z = self.coordinates[i]
           self.coordinates[i] = (x/Molecule.__bohr, y/Molecule.__bohr, z/Molecule.__bohr)


    def get_distance(self, i, j):
        """Return the distance between two atoms"""
        x0, y0, z0 = self.coordinates[i]
        x1, y1, z1 = self.coordinates[j]
        return math.sqrt((x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2)
        
    

if __name__ == 'main':
    mol = Molecule('water')
    mol.add_atom("O", 0.0, 0.0, 0.0)
    mol.add_atom("H", 0.96, 0.0, 0.0)
    mol.add_atom("H", -0.24, 0.93, 0.0)
    print(len(mol))

