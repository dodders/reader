import boto3

# initialize aws connection.
# credentials are loaded from environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
print('aws starting...')
# session = boto3.Session(profile_name='dep')
sns = session.pclient('sns')
s3 = session.resource('s3')


def send_daily(blog_title, published, msg):
    resp = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:397678393215:george',
        Subject=blog_title + ' on ' + published,
        Message=msg
    )
    print('email sent', resp)


def get_config():
    print('fetching config...')
    resp = s3.Object('blog-reader-config', 'sites.txt').get()
    print('config found:', resp)
    body = resp['Body'].read().decode('utf-8')
    return body
