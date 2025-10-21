# We import the entire 'math' module, giving us access to all its tools
import math

# To use a tool, we use dot notation: module.function()

number = 16
square_root = math.sqrt(number)

print(f"The square root of {number} is {square_root}")

# The math module also has built-in variables, like pi
print(f"The value of pi is: {math.pi}")

# --- Another way to import ---
# You can also import just one specific tool from the module

from math import pow # 'pow' is used for "to the power of"

# Because we imported 'pow' directly, we don't need to use 'math.'

three_squared = pow(3, 2) # This means 3 to the power of 2
print(f"3 to the power of 2 is: {three_squared}")
