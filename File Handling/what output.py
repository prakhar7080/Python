def count(s):
    for str in s.split():
        x = "&".join(str)
        return x
print(count("Python is fun to learn"))