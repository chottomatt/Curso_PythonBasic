# nomes = ['matheus', 'luiz', 'otávio']
# x = nomes.index('matheus')
# y = nomes.index('luiz')
# print(x)
# print(y)

def twoSum(self, nums, target):
    nums = [2,7,11,15]
    target = 9
    vistos = {}

    for i, num in enumerate(nums):
        falta = target - num

        if falta in vistos:
            return [vistos[falta], i]
        
        vistos [num] = i 
