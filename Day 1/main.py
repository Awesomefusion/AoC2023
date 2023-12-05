import re

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text


def calibration(text):
    return sum(int(i[0] + i[-1]) for i in re.sub(r"[A-z]", "", text).split("\n"))


text = open("day_one.txt").read()
print(calibration(text))
print(calibration(replace_words(text)))
