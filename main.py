import metrics.metrics_factory as metrics

print("1 - Top 10 requested pages and the number of requests made for each")
for item in metrics.top_10_host_requests():
    element, times = item
    print(f"Page: {element} was called {times} times.")

print("\n----------------------------------------\n")

print("2 - Percentage of successful requests (anything in the 200s and 300s range)")
print(f"{metrics.successful_requests_percentage()}%")

print("\n----------------------------------------\n")

print("3 - Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)")
print(f"{metrics.unsuccessful_requests_percentage()}%")


print("\n----------------------------------------\n")

print("4 - Top 10 unsuccessful page requests")
for item in metrics.top_10_unsuccessful_page_requests():
    element, times = item
    print(f"Page: {element} was called {times} times.")

print("\n----------------------------------------\n")

print("5 - The top 10 hosts making the most requests, displaying the IP address and number of requests made.")
for item in metrics.top_10_page_requests():
    element, times = item
    print(f"Page: {element} was called {times} times.")
