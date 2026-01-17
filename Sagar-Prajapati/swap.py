def swap_two_nums(a,b):
    print("Old Values of a and b", a , b)
    a=a+b #25
    b=a-b #10
    a=a-b #15
    print("New values of a and b is",a , b)

a,b=10,15
swap_two_nums(a,b)