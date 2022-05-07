import requests
r = requests.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
with open ("r", "w") as f:
    f.write(str(r))
def parse_log_line(log_line: str):
    ip_address, log_line = log_line.split(' - - ')
    date, log_line = log_line.split('] ')
    date = date.lstrip('[')
    request, other_info = log_line.rsplit(' "-" ')
    other_info = other_info.strip('"')
    request = request.replace('"', '').split(' ')

    return ip_address, date, *request, other_info


lines = requests.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
parsed_lines = [parse_log_line(line) for line in lines]