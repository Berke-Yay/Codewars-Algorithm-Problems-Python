#This function returns the number of 1's in the binary value of an integer.
def count_bits(n):
    binary =[]
    while n!=1:
        binary.append(n%2)
        n=n//2
    return binary.count(1)+1
