def get_successful_response_generator(request):
    yield {"host": request[0],
           "datetime": request[1],
           "datestamp": request[2],
           "method": request[3],
           "endpoint": request[4],
           "version": request[5],
           "status": request[6],
           "content_length": request[7]
           }
