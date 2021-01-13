# Receive SQS messages
def receive_messages(queue_url):
  print('Reading messages')
  while True:
     try:
      data = sqs.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages = 10,
        VisibilityTimeout = 60,
        WaitTimeSeconds = 20
      )
    # An error occurred
    except ParamValidationError as e:
      print("Parameter validation error: %s" % e)
    except ClientError as e:
      print("Client error: %s" % e)
  # Check if empty receive
  try:
    data['Messages']
  except KeyError:
    data = None
   if data is None:
    print('Queue empty waiting 60s')
    # Wait for 60 seconds
    time.sleep(60)
  else:
    print(data['Messages'])
    # Wait for 1 second
    time.sleep(1)
# Main program
def main():
  sqs_queue_url = create_sqs_queue('backspace-lab')
  print('Successfully created SQS queue URL '+ sqs_queue_url )
  create_messages(sqs_queue_url)
  print('Successfully created messages')
  receive_messages(sqs_queue_url)
