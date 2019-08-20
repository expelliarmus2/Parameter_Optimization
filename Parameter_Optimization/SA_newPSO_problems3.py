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


def run(eng, theta, final_state):
    qureg = eng.allocate_qureg(14)
    run_circuit(qureg, theta)
    eng.flush()
    pro = eng.backend.get_probability(final_state, qureg)
    All(Measure) | qureg
    return pro


def calculate_theta(eng, final_state):
    #采用模拟退货算法。
    num = 30
    T_max = 100
    T_min = 0.001
    Trate = 0.95
    theta = 2 * np.pi * np.random.random(5)
    theta = theta.tolist()
    # 储存上一次的结果，以及最好的结果。
    pro_max=[]
    theta_max=[]
    pro_max .append(run(eng, theta, final_state))
    proLast = run(eng, theta, final_state)
    theta_max.append(theta)
    thetaLast = theta
    while (T_max>T_min):
        n=0
        while n<num:
            theta_i = list(0.1 * np.random.random(5))
            theta = [x+y for x,y in zip(thetaLast,theta_i)]
            pro = run(eng, theta, final_state)
            if pro >= pro_max[-1] or pro>0.002:
                pro_max.append(pro)
                theta_max.append(theta)
                print(pro_max[-1], theta_max[-1])
            res = proLast - pro
            if res < 0:
                thetaLast = theta
                proLast = pro
            elif res > 0:
                #最开始T_max大，那么p也很大。应该是很大的概率可以
                p = np.exp(-res / T_max)
                if np.random.random() < p:
                    thetaLast = theta
                    proLast = pro
            n=n+1
        T_max = T_max * Trate

    #下面采用PSO算法优化结果
    print("\nPSO:")
    theta=theta_max
    theta.append([0, 0, 0, 0, 0])
    theta.append([2 * np.pi, 2 * np.pi, 2 * np.pi, 2 * np.pi, 2 * np.pi])
    for i in range(5):
        matrix1 = [0] * 5
        matrix2 = [2 * np.pi] * 5
        matrix1[i] = 2 * np.pi
        matrix2[i] = 0
        theta.append(matrix1)
        theta.append(matrix2)
    for i in range(4):
        for j in range(i + 1):
            matrix1 = [0] * 5
            matrix1[j] = 2 * np.pi
            matrix1[i + 1] = 2 * np.pi
            theta.append(matrix1)
            matrix2 = [2 * np.pi] * 5
            matrix2[j] = 0
            matrix2[i + 1] = 0
            theta.append(matrix2)
    n=len(theta)
    pro=[0]*n

    times = 40
    p_min=0.7
    p_max=0.95
    for k in range(times):
        for j in range(len(theta)):
            pro[j] = run(eng, theta[j], final_state)
        max_pro = max(pro)
        location = pro.index(max_pro)
        print(max_pro, location, p, theta[location])
        for j in range(n):
            p = p_min + (p_max- p_min) * np.log10(k + 1) / np.log10(times)
            theta[j] = [p * x + (1 - p) * y for x, y in zip(theta[j], theta[location])]
        if max_pro >= 0.018:
            break
    print(len(theta))
    return theta[location]


if __name__ == "__main__":
    for k in range(1):
        print("\n\nThe %d time:"%k)
        # use projectq simulator
        eng = MainEngine()
        # use hiq simulator

        '''backend = SimulatorMPI(gate_fusion=True)
        cache_depth = 10
        rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
        engines = [TagRemover(), LocalOptimizer(cache_depth)
                   , AutoReplacer(rule_set)
                   , TagRemover()
                   , LocalOptimizer(cache_depth)
                   , GreedyScheduler()
                   ]
        # make the compiler and run the circuit on the simulator backend
        eng = HiQMainEngine(backend, engines)'''

        final_state = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]

        # Function that need to be implemented by the contestants
        theta = calculate_theta(eng, final_state)
        qureg = eng.allocate_qureg(14)
        run_circuit(qureg, theta)

        eng.flush()

        print(eng.backend.get_probability(final_state, qureg))

        All(Measure) | qureg
'''输出结果：
The first step:
0.0015011207493061582
The Second step with p=0.5: 


0.013252322531114536 5 [4.67345, 5.4132, 1.592096, 4.975939, 5.439311]
0.01325232253111452 5 [4.67345, 5.4132, 1.592096, 4.975939, 5.439311]
0.013252322531114533 5 [4.67345, 5.4132, 1.592096, 4.975939, 5.439311]
0.013252322531114514 5 [4.67345, 5.4132, 1.592096, 4.975939, 5.439311]
0.01646722968521052 2 [4.696316412600654, 5.4569634805157925, 1.5694507346501565, 5.030885871452138, 5.13230769711085]
0.02072521547591703 15 [4.7351874346496885, 5.462268781107259, 1.5310203673250782, 5.044263882825431, 5.312180420654787]
The Second step with p=0.9: 


0.022097767046075623 2 [4.715751923625171, 5.459616130811526, 1.5502355509876173, 5.037574877138784, 5.2222440588828185]
0.02209776704607563 2 [4.715751923625171, 5.459616130811526, 1.5502355509876173, 5.037574877138784, 5.2222440588828185]
0.022097767046075637 2 [4.715751923625171, 5.459616130811526, 1.5502355509876173, 5.037574877138784, 5.2222440588828185]
0.022097767046075648 2 [4.715751923625171, 5.459616130811526, 1.5502355509876173, 5.037574877138784, 5.2222440588828185]
0.02209776704607563 2 [4.715751923625171, 5.459616130811526, 1.5502355509876173, 5.037574877138784, 5.2222440588828185]
0.022126451072511686 15 [4.727228398530037, 5.461182494284653, 1.5388891771867248, 5.0415246681066925, 5.275350581145548]
0.022382142168615823 6 [4.714315865638148, 5.443353780561327, 1.5775166982261706, 5.00809676251316, 5.264379811602304]
0.02254287801527669 2 [4.716641200567906, 5.4581308684990875, 1.5519424920693923, 5.034982546863334, 5.231237221158413]
0.022644210612574142 6 [4.714548399131124, 5.444831489355103, 1.5749592776104926, 5.0107853409481775, 5.261065552557915]
0.02285813542566213 15 [4.72396163560931, 5.457828621659408, 1.5467998147727366, 5.035154284125863, 5.26906324355494]
0.022865247281738426 6 [4.715489722778943, 5.4461312025855335, 1.572143331326717, 5.013222235265946, 5.261865321657618]
0.02302351564899617 15 [4.723114444326273, 5.456658879752021, 1.5493341664281346, 5.032961079239871, 5.268343451365208]
0.023023515648996178 15 [4.723114444326273, 5.456658879752021, 1.5493341664281346, 5.032961079239871, 5.268343451365208]
0.023311288810070753 9 [4.723114444326273, 5.456658879752021, 1.5742888758427886, 5.032961079239871, 5.268343451365208]
0.023320260081127763 15 [4.723114444326273, 5.456658879752021, 1.5518296373696001, 5.032961079239871, 5.268343451365208]
The Second way with p=0.95: 


0.02352908672167448 9 [4.723114444326273, 5.456658879752021, 1.5720429519954697, 5.032961079239871, 5.268343451365208]
0.023529086721674454'''
