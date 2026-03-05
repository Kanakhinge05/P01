import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    sns.publish(
        TopicArn='your-sns-topic-arn',
        Message='Deployment Started',
        Subject='DevOps Alert'
    )
    return "Done"
