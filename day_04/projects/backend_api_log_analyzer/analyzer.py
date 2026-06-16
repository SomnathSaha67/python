def open_log_file():
  total_requests, response_200, response_404, response_500= 0, 0, 0, 0
  file_open= open('api_logs.txt', 'r')
  for response in file_open:
    total_requests, response_200, response_404, response_500, failure_rate= process_log(response, total_requests, response_200, response_404, response_500)
  generate_report(total_requests, response_200, response_404, response_500, failure_rate)
def process_log(response, requests, response200, response404, response500):
  if not response.isspace():
    requests+=1
    if "200" in response:
      response200+=1
    elif "404" in response:
      response404+=1
    else:
      response500+=1
  rate= round((response404+response500)/requests,2)
  return requests, response200, response404, response500, rate
def generate_report(total_requests, response_200, response_404, response_500, failure_rate):
  print(f"Total Requests: {total_requests}")
  print(f"200 Responses: {response_200}")
  print(f"404 Responses: {response_404}")
  print(f"500 Responses: {response_500}")
  print(f"Failure Rate: {failure_rate}")
open_log_file()