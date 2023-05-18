def steinglenth(my_string):
    count = 0
    for i in my_string:
        count += 1
    return count

def space(my_string):
    count = 0
    for i in my_string:
        if i == " ":
            count += 1
    return count
#without spaces in the string
your_string = input('Enter your string: ')
print(steinglenth(your_string)-space(your_string))
