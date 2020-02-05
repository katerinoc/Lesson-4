from website_alive import check_response


def make_request(url):
    r = check_response.check_response(url)
    if r.status_code == 200:
        return True
    else:
        return False
