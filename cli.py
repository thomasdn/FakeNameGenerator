#!/usr/bin/env python3
#encoding=utf8
import random

def generate_username(full_name):
    username = ""
    first_name = full_name.split(" ")[0]
    last_name = full_name.split(" ")[-1]
    r = random.random()
    if r < 0.33:
        # initial + lastname + number
        username = "{}{}{}".format(first_name[0], last_name, int(r*100+18))
    elif r <0.66:
        # fullname + number
        username = "{}{}{}".format(first_name, last_name, int(r*100+18))
    else:
        # initials + number
        username = "{}{}{}".format(first_name[0], last_name[0], int(r*10000+18))

    #sanitize username
    username = username.lower()
    username = username.replace("æ", "ae")
    username = username.replace("ø", "oe")
    username = username.replace("å", "aa")
    username = username.replace("'", "")
    return username

def generate_full_name():

    first_names = []
    last_names = []
    middle_names = []
    with open("first_names.txt") as f:
        for line in f.readlines():
            if line.strip():
                first_names.append(line.strip())

    with open("last_names.txt") as f:
        for line in f.readlines():
            if line.strip():
                last_names.append(line.strip())

    with open("middle_names.txt") as f:
        for line in f.readlines():
            if line.strip():
                middle_names.append(line.strip())

    first_name = random.choice(first_names)
    middle_name = random.choice(first_names)
    last_name = random.choice(last_names)
    probability_middle_name = 0.5
    if random.random() > probability_middle_name:
        full_name = "{} {} {}".format(first_name, middle_name, last_name)
    else:
        full_name = "{} {}".format(first_name, last_name)
    return full_name

def main():
    full_name = generate_full_name()
    username = generate_username(full_name)

    print("Full name: {}".format(full_name))
    print("Username: {}".format(username))

def many():
    names = []
    for n in range(100):
        full_name = generate_full_name()
        name = {}
        name["full_name"] = full_name
        name["username"] = generate_username(full_name)
        names.append(name)

    return render_template("many.html", names = names)



if __name__ == '__main__':
    main()
