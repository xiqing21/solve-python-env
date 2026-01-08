#!/usr/bin/env python
"""
Simple Python Environment Test Script
"""

import sys
import os

print("=" * 60)
print("Python Environment Test")
print("=" * 60)

print(f"\nPython Version: {sys.version}")
print(f"Python Executable: {sys.executable}")
print(f"Current Directory: {os.getcwd()}")

# Test random number
import random
print(f"\nRandom number test: {random.randint(1, 100)}")

# Test list comprehension
numbers = [i**2 for i in range(10)]
print(f"List comprehension test: {numbers}")

# Test math calculation
import math
print(f"Math calculation: pi = {math.pi:.6f}, e = {math.e:.6f}")

print("\n" + "=" * 60)
print("All tests passed! Python environment is working")
print("=" * 60)
