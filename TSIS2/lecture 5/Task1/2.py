def file_read(fname, n):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, n):
                        print(line)
file_read('test.txt',2)