def big_diff(linea):
    '''Return the difference between the biggest and smallest int from a string of tab separated numbers'''
    nums = [int(c) for c in linea.split('\t')]
    return max(nums) - min(nums)

def even_div(linea):
    '''Return the division between two numbers with mod 0 from a string of tab separated numbers'''
    nums = sorted([int(c) for c in linea.split('\t')], reverse=True)
    zen = len(nums)
    sol = [nums[i]/nums[j] for i in range(0, zen) for j in range(i+1, zen) if nums[i]%nums[j] == 0]
    return sol[0]

def checksumo(inputo, func):
    return sum([func(linea) for linea in inputo.splitlines()])

def checksumo_1(inputo):
    return checksumo(inputo, big_diff)

def checksumo_2(inputo):
    return checksumo(inputo, even_div)
