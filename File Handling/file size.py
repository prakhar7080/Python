def size(file_name):
    import os
    return os.stat(file_name).st_size
print(size("space.txt"))