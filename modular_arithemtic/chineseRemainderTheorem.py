'''
how can we solve this using the chinese remainder theorem and break down the process

Given the following set of linear congruences:

x ≡ 2   mod5
x ≡ 3   mod11
x ≡ 5   mod17

Find the integer aa such that x ≡ a  mod935

'''
modules = [5, 11, 17]
remainders = [2, 3, 5]
N = 5 * 11 * 17  # Total product of all moduli

niL = []
yiL = []


result = 0
for mod, rem in zip(modules, remainders): 
    ni = N // mod
    niL.append(ni)
    yi = pow(ni, -1, mod)
    yiL.append(yi)
    result += rem * ni * yi
x = result % N



print(f'\nNIs: {niL}')
print(f'YIs: {yiL}\n')


print(f"The solution is: x ≡ {x} mod {N}\nmath proof: {result} % {N} = {x}")

