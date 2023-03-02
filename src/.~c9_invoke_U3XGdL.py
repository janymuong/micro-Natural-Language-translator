import boto3

client = boto3.clinet('translate', region_name='us-east-1')
text_data = 'semper fidelis'

response = client.translate_text(Twex)