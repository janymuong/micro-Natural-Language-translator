import boto3
import click

@click.command()
@click.option('--phrase', prompt='Put in a phrase you want to translate',
    help='CLI tool that translates text')

def translate_txt(phrase)
    '''
    Translate text command line tool
    '''
    client = boto3.client('translate', region_name='us-east-1')
    click.echo(click.style(f"Translate phrase: {phrase}", fg='red'))
    response_txt = client.translate_text(Text=phrase, SourceLanguageCode='auto',
        TargetLanguageCode='en')
    text = response_txt['TranslatedText']
    click.echo(click.style(f"{text}", fg='white', bg='blue'))
    
if __name__ = '__main__':
    translate_txt()