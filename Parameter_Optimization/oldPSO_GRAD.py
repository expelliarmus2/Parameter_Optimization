import math
from projectq import MainEngine
from projectq.ops import X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.cengines import (MainEngine,
                               AutoReplacer,
                               LocalOptimizer,
                               TagRemover,
                               InstructionFilter,
                               DecompositionRuleSet)
import projectq.setups.decompositions
import numpy as np
'''from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from mpi4py import MPI'''
import time


def run_circuit(qureg, theta):
    X | qureg[0]
    X | qureg[1]
    X | qureg[2]
    X | qureg[3]
    X | qureg[4]
    X | qureg[5]
    X | qureg[6]
    X | qureg[7]
    X | qureg[8]
    X | qureg[9]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[6]
    H | qureg[7]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    H | qureg[10]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    Rz(theta[0]) | qureg[10]
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[10]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    H | qureg[1]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[9]
    H | qureg[8]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    H | qureg[13]
    H | qureg[12]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[1]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    H | qureg[1]
    H | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    H | qureg[13]
    H | qureg[12]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[1]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[1]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    H | qureg[11]
    H | qureg[10]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[0]
    H | qureg[1]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[1]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    H | qureg[5]
    H | qureg[1]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    H | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    H | qureg[4]
    H | qureg[5]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[5]
    H | qureg[4]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[3]
    H | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    H | qureg[12]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    H | qureg[3]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[3]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[3]
    H | qureg[1]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[4]
    H | qureg[1]
    H | qureg[2]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    H | qureg[12]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[3]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[3]
    H | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[12]
    H | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[11]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[12]
    H | qureg[4]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[2]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    H | qureg[4]
    H | qureg[2]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[10]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    Rz(theta[1]) | qureg[10]
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[10]
    H | qureg[0]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[3]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    H | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    H | qureg[13]
    H | qureg[12]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[3]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    H | qureg[0]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[3]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[0]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[0]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[3]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[1]
    H | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    H | qureg[11]
    H | qureg[10]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    Rx(theta[2]) | qureg[13]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    H | qureg[11]
    H | qureg[10]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[4]
    H | qureg[12]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    H | qureg[12]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    H | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[10]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    Rz(theta[3]) | qureg[10]
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[10]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[2]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[3]
    H | qureg[11]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[3]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    H | qureg[11]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    Rx(theta[0]) | qureg[10]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    Rz(theta[2]) | qureg[10]
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[10]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[0]
    H | qureg[3]
    H | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[4]
    H | qureg[3]
    H | qureg[0]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[4]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[1]
    H | qureg[11]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[11]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[3]
    H | qureg[4]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    H | qureg[11]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    H | qureg[7]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[7]
    H | qureg[6]
    H | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[1]
    H | qureg[0]
    H | qureg[2]
    H | qureg[3]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[3]
    H | qureg[2]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[12]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[1], qureg[12])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[0]
    H | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[5], qureg[12])
    CX | (qureg[4], qureg[5])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[1]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[0]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[3], qureg[12])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[7], qureg[12])
    CX | (qureg[6], qureg[7])
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[2]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    H | qureg[8]
    H | qureg[9]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[4]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[1]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[11]
    H | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[1]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[1]
    H | qureg[8]
    H | qureg[9]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[9], qureg[12])
    CX | (qureg[8], qureg[9])
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[13]
    CX | (qureg[5], qureg[6])
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[8])
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    CX | (qureg[7], qureg[8])
    CX | (qureg[6], qureg[7])
    CX | (qureg[5], qureg[6])
    H | qureg[13]
    Rx(theta[2]) | qureg[5]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[0]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[3]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    H | qureg[4]
    H | qureg[0]
    H | qureg[0]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[4]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[4], qureg[11])
    CX | (qureg[3], qureg[4])
    H | qureg[12]
    H | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[1]
    H | qureg[1]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[3]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[1]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[5], qureg[11])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    CX | (qureg[0], qureg[1])
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    H | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    Rz(theta[2]) | qureg[12]
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[12]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[5])
    CX | (qureg[5], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[4]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[5], qureg[10])
    CX | (qureg[4], qureg[5])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[8], qureg[9])
    CX | (qureg[9], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[0]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[9], qureg[10])
    CX | (qureg[8], qureg[9])
    H | qureg[11]
    H | qureg[10]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[3], qureg[10])
    CX | (qureg[2], qureg[3])
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | (qureg[6], qureg[7])
    CX | (qureg[7], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[2]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[7], qureg[10])
    CX | (qureg[6], qureg[7])
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[7]
    H | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[10]
    H | qureg[11]
    CX | (qureg[0], qureg[1])
    CX | (qureg[1], qureg[10])
    CX | (qureg[10], qureg[11])
    Rz(theta[1]) | qureg[11]
    CX | (qureg[10], qureg[11])
    CX | (qureg[1], qureg[10])
    CX | (qureg[0], qureg[1])
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | (qureg[1], qureg[2])
    CX | (qureg[2], qureg[3])
    CX | (qureg[3], qureg[4])
    CX | (qureg[4], qureg[10])
    CX | (qureg[10], qureg[11])
    CX | (qureg[11], qureg[12])
    CX | (qureg[12], qureg[13])
    Rz(theta[1]) | qureg[13]
    CX | (qureg[12], qureg[13])
    CX | (qureg[11], qureg[12])
    CX | (qureg[10], qureg[11])
    CX | (qureg[4], qureg[10])
    CX | (qureg[3], qureg[4])
    CX | (qureg[2], qureg[3])
    CX | (qureg[1], qureg[2])
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]

def run(eng,theta,final_state):
    qureg=eng.allocate_qureg(14)
    run_circuit(qureg,theta)
    eng.flush()
    pro = eng.backend.get_probability(final_state, qureg)
    All(Measure) | qureg
    return pro

def calculate_theta(eng, final_state):
    m=30
    time=100
    theta = 2*np.pi*np.random.random((m,5))
    theta=theta.tolist()
    #g存放全局最优接。
    theta_g=2*np.pi*np.random.random((2,5))
    theta_g=theta_g.tolist()
    max_pro_g=[]
    max_pro_g.append(run(eng,theta_g[0],final_state))
    max_pro_g.append(run(eng, theta_g[1], final_state))
    #下面十更新速度以及一些参数。
    max_pro_p=0
    v=[0]*5
    c1=1.4
    c2=1.4
    c3=1
    v_max=1
    weight=0.8
    location=0
    pro=[0]*m
    #0.005452703005976826 0.0007955449538926794 20 [ 2.9706074   3.45605731  3.40125491  3.39205966 -0.05104171]
    for i in range(time):
        for j in range(m):
            pro[j]=run(eng,theta[j],final_state)
        max_pro_p=max(pro)
        location=pro.index(max_pro_p)#当前最优的位置
        if max_pro_p>=max_pro_g[-1]:
            theta_g.append(theta[location])
            max_pro_g.append(max_pro_p)
        print(max_pro_g[-1],max_pro_p,theta_g[-1])
        if max_pro_p>0.18:
            break
        for j in range(m):
            v=[weight*x+c1*np.random.random()*(y-z)+c2*np.random.random()*(k-z)+c3*np.random.random()*(l-z) for x,y,z,k,l in zip(v,theta[location],theta[j],theta_g[-1],theta[-2])]
            for k in range(5):
                if v[k]>=v_max:
                    v[k]=v_max
                if v[k]<=-v_max:
                    v[k]=-v_max
            theta[j]=[x+y for x,y in zip(theta[j],v)]

    #利用PSO的数据进行下一步梯度下降,但是这种方法的效率不是很高。
    theta=theta_g[2:]
    n=len(theta)
    pro=[0]*n
    print("Grad Desent with %d data:"%n)
    for i in range(100):
        for j in range(n):
            theta_i=0.01*np.random.random(5)
            theta_i=theta_i.tolist()
            theta_i=[x+y for x,y in zip(theta_i,theta[j])]
            prob=run(eng,theta_i,final_state)
            if prob>pro[j]:
                pro[j]=prob
                theta[j]=theta_i
        max_pro=max(pro)
        location=pro.index(max_pro)#当前最优的位置
        print(max_pro,theta[location])
    return theta[location]


if __name__ == "__main__":
    # use projectq simulator
    # eng = MainEngine()
    # use hiq simulator3549

    backend = SimulatorMPI(gate_fusion=True)
    cache_depth = 10
    rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
    engines = [TagRemover(), LocalOptimizer(cache_depth)
               , AutoReplacer(rule_set)
               , TagRemover()
               , LocalOptimizer(cache_depth)
               , GreedyScheduler()
               ]
    # make the compiler and run the circuit on the simulator backend
    eng = HiQMainEngine(backend, engines)
    start_time=time.time()

    # Just an example, you need to design more final state cases for testing..
    final_state = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    # Function that need to be implemented by the contestants
    theta = calculate_theta(eng, final_state)

    qureg = eng.allocate_qureg(14)
    run_circuit(qureg, theta)
    eng.flush()
    print(eng.backend.get_probability(final_state, qureg))
    All(Measure) | qureg
    end_time=time.time()
    print(end_time-start_time)
