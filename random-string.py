import string
import random

def sting_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    length = input('Desired String Length: ')
    print sting_generator(length)




if __name__ == "__main__":
    main()
