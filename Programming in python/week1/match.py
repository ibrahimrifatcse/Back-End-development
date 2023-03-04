http_server = 240
# The match statement compares a value to several different conditions until one of these conditions is met.
match http_server:
    case 200 | 2400:
        print("success")
    case 201:
        print("success")
    case 404:
        print("not found")
    case 500:
        print("internal server error")
    case _:
        print("fail")