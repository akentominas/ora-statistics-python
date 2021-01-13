from zipfile import ZipFile
import io


def log_generator():
    """
       Creates a Generator of lists with formatted HTTP Responses parsed from the log
       instead of keeping all the data in a list

       """
    # with open('logs/access_log_Aug95', 'r') as f:
    #     for line in f:
    #         yield line.replace("-", "").replace("\"", "").replace("[", "").replace("]", "").split()

    # with ZipFile("../logs/access_log_Aug95.zip") as zipped:
    #     info = zipped.read('access_log_Aug95')
    #     # for line in info:
    #     #     print(line)
    #     print(type(info))

    with ZipFile("logs/access_log_Aug95.zip") as zf:
        with io.TextIOWrapper(zf.open("access_log_Aug95"), encoding="cp1252") as f:
            for line in f:
                yield line.replace("-", "").replace("\"", "").replace("[", "").replace("]", "").split()
