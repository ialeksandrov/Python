# def book_reader(iterabl):


def read_file(filepath, delim):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.split('#')


