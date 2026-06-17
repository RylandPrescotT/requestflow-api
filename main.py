requests_queue = []

def add_request(request):
    requests_queue.append(request)

add_request("User Login")

print(requests_queue)
