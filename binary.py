""" 
Copyright Alex Clark October 2017

A basic script to convert an IP address into binary. I think there might be a more efficient way to 
write this, but I don't know how yet. Either with recursion or using variables in more loops or something like that. 

Let me know if you have any questions!
Alex
"""

ip = []
binary = []

print "\nPlease enter your IP address, pressing enter after each number group."
for i in range (4):
    ip_numbers = raw_input("        \n > ")
    ip += [ip_numbers]


def number8(new_number7):
    global binary
    if 1 <= new_number7:
        binary += ["1"]
        new_number8 = new_number7 - 1

    else:
        binary += ["0"]
        new_number8 = new_number7


def number7(new_number6):
    global binary
    if 2 <= new_number6:
        binary += ["1"]
        new_number7 = new_number6 - 2
        number8(new_number7)
    else:
        binary += ["0"]
        new_number7 = new_number6
        number8(new_number7)


def number6(new_number5):
    global binary
    if 4 <= new_number5:
        binary += ["1"]
        new_number6 = new_number5 - 4
        number7(new_number6)
    else:
        binary += ["0"]
        new_number6 = new_number5
        number7(new_number6)


def number5(new_number4):
    global binary
    if 8 <= new_number4:
        binary += ["1"]
        new_number5 = new_number4 - 8
        number6(new_number5)
    else:
        binary += ["0"]
        new_number5 = new_number4
        number6(new_number5)


def number4(new_number3):
    global binary
    if 16 <= new_number3:
        binary += ["1"]
        new_number4 = new_number3 - 16
        number5(new_number4)
    else:
        binary += ["0"]
        new_number4 = new_number3
        number5(new_number4)


def number3(new_number2):
    global binary
    if 32 <= new_number2:
        binary += ["1"]
        new_number3 = new_number2 - 32
        number4(new_number3)
    else:
        binary += ["0"]
        new_number3 = new_number2
        number4(new_number3)


def number2(new_number):
    global binary
    if 64 <= new_number:
        binary += ["1"]
        new_number2 = new_number - 64
        number3(new_number2)
    else:
        binary += ["0"]
        new_number2 = new_number
        number3(new_number2)


def number1(ip_number):
    global binary
    if 128 <= ip_number:
        binary += ["1"]
        new_number = ip_number - 128
        number2(new_number)
    else:
        binary += ["0"]
        new_number = ip_number
        number2(new_number)


for i in range (4):
    ip_number = int(ip[0])
    ip.remove(ip[0])
    number1(ip_number)

glue = ';'
s = glue.join(binary)
my_str = "".join(binary)

parts = [my_str[i:i+8] for i in range(0, len(my_str), 8)]
part0 = parts[0]
part1 = parts[1]
part2 = parts[2]
part3 = parts[3]

print "\n", part0, ":", part1, ":", part2, ":", part3, "\n"

