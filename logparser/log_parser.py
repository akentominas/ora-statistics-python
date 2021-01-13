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

    try:
        with ZipFile("logs/access_log_Aug95.zip") as zf:
            with io.TextIOWrapper(zf.open("access_log_Aug95"), encoding="cp1252") as f:
                for line in f:
                    yield line.replace("-", "").replace("\"", "").replace("[", "").replace("]", "").split()
    except FileNotFoundError as ex:
        print(f"Could not find the zip file specified!{ex}")
