from logparser.log_parser import log_generator
import generator.response_generator as gen
import utils.metrics_helper as helper


def top_10_host_requests():
    """
        Challenge number: 1

        Top 10 requested pages and the number of requests made for each

        This function will use the get_successful_response_generator() from the generator package
        and store the generator's results in a dictionary as a hashmap

        Assumptions: Function checking for non malformed entries
    """
    frequency = {}
    for dict_response in log_generator():
        if len(dict_response) == 8:
            for item2 in gen.get_successful_response_generator(dict_response):
                if item2['endpoint'] in frequency:
                    frequency[item2['endpoint']] += 1
                else:
                    frequency[item2['endpoint']] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda item3: item3[1], reverse=True)

    return sorted_frequency[0:10]


def successful_requests_percentage():
    """
        Challenge number: 2

        Percentage of successful requests (anything in the 200s and 300s range)

        Assumptions: Function checking for non malformed entries

    """
    total_requests = sum(1 for x in log_generator() if len(x) == 8)
    successful_requests = sum(1 for element in log_generator() if len(element) == 8 and
                              (200 <= int(element[7]) < 300))
    percentage = helper.calculate_percentage(successful_requests, total_requests)
    return round(percentage, 2)


def unsuccessful_requests_percentage():
    """
        Challenge number: 3

        Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)

        Assumptions: Function checking for non malformed entries

    """
    total_requests = sum(1 for x in log_generator() if len(x) == 8)

    unsuccessful_requests = sum(1 for element in log_generator() if len(element) == 8
                                and (int(element[7]) < 200 or int(element[7]) >= 300))
    percentage = helper.calculate_percentage(unsuccessful_requests, total_requests)
    return round(percentage, 2)


def top_10_unsuccessful_page_requests():
    """
        Challenge number: 4

        Top 10 requested pages and the number of requests made for each

        This function will use the get_successful_response_generator() from the generator package
        and store the generator's results in a dictionary as a hashmap

        Assumptions: Function checking for non malformed entries
    """
    frequency = {}
    for dict_response in log_generator():
        if len(dict_response) == 8 and (int(dict_response[7]) < 200 or int(dict_response[7]) >= 300):
            for item2 in gen.get_successful_response_generator(dict_response):
                if item2['host'] in frequency:
                    frequency[item2['endpoint']] += 1
                else:
                    frequency[item2['endpoint']] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda item3: item3[1], reverse=True)

    return sorted_frequency[0:10]


def top_10_page_requests():
    """
        Challenge number: 5

        Top 10 requested pages and the number of requests made for each

        This function will use the get_successful_response_generator() from the generator package
        and store the generator's results in a dictionary as a hashmap

        Assumptions: Function checking for non malformed entries
    """
    frequency = {}
    for dict_response in log_generator():
        if len(dict_response) == 8:
            for item2 in gen.get_successful_response_generator(dict_response):
                if item2['host'] in frequency:
                    frequency[item2['host']] += 1
                else:
                    frequency[item2['host']] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda item3: item3[1], reverse=True)

    return sorted_frequency[0:10]

