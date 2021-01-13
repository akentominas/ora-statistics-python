def log_generator():
    """
       Creates a Generator of lists with formatted HTTP Responses parsed from the log
       instead of keeping all the data in a list

       """
    with open('logs/access_log_Aug95', 'r') as f:
        for line in f:
            yield line.replace("-", "").replace("\"", "").replace("[", "").replace("]", "").split()
