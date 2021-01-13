# Send 50 SQS messages
def create_messages(queue_url):
  # Create 50 messages
  TempMessages = []
  for a in range(50):
    tempStr = 'This is the content for message ' + str(a)
    TempMessages.append(tempStr)
  # Deliver messages to SQS queue_url
  for message in TempMessages:
    try:
      data = sqs.send_message(
        QueueUrl = queue_url,
        MessageBody = message
       )
      print(data['MessageId'])
    # An error occurred
    except ParamValidationError as e:
      print("Parameter validation error: %s" % e)
    except ClientError as e:
      print("Client error: %s" % e)# Main program
def main():
	sqs_queue_url = create_sqs_queue('backspace-lab')
	print('Successfully created SQS queue URL '+ sqs_queue_url )
	create_messages(sqs_queue_url)
	print('Successfully created messages')
