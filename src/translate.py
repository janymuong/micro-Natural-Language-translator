import boto3

client = boto3.client('translate', region_name='us-east-1')
text_data = 'semper fidelis'

response = client.translate_text(Text=text_data, SourceLanguageCode='auto',
    TargetLanguageCode='en')

print(response['TranslatedText'])