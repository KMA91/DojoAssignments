# # def odd_even():
# #     for i in range(1, 2001):
# #         if i % 2 == 1:
# #             print "number is", i, "This is an odd number"
# #         if i % 2 == 0:
# #             print "number is", i, "This is an even number"

# # odd_even()

# # def multiply(arr, num):
# #     for i in range(len(arr)):
# #         arr[i] *= num
# #     return arr

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
            print val_arr
        new_array.append(val_arr)
        print new_array
    # return new_array

x = layered_multiples(multiply([2,4,5],3))
print x