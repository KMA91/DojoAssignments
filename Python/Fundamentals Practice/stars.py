part 1

def stars(nums):
    
    for i in nums:
        print "*" * i

nums = [4, 6, 1, 3, 5, 7, 25]

stars(nums)

part2

def draw_stars(nums):
    
nums = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]    

for i in nums:
    if isinstance(i, str):
        string = i[0]
        string = string.lower()
        print string * len(i)
    else:
        print "*" * i
        