# Text Translator
---

## How It Works
This is an AWS Lambda function-like text translator created with Python and Boto3.

## Setup
- create a siloed Python virtual environment: `make setup`
    > this is a directive in [Makefile](./Makefile)

- activate the virtual environment: `source ~/.nl-lambda/bin/activate`
- install the dependencies via Makefile: `make install`

## Running the Translator as a `CLI`    
```bash
python3 cli-translate.py
```

`Sample anaologous behavior in Git Bash for Windows`:   
```bash
me@HP MINGW64 ~/aws-cloud-devops/micro-Natural-Language-translator/src (main)
$ python cli-translate.py
Put in a phrase you want to translate: Salut, je nes suis un robot
Translate phrase: Salut, je nes suis un robot
Hi, I'm not a robot
(.nl-lambda)
me@HP MINGW64 ~/aws-cloud-devops/micro-Natural-Language-translator/src (main)
$
```

----------------------------------------------------------------- 
        You can decide to work on Amazon Linux 2
         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
## Reference
`translate_text(**kwargs)`
Translates input text from the source language to the target language.

### Request Syntax      
```bash
response = client.translate_text(
    Text='string',
    TerminologyNames=[
        'string',
    ],
    SourceLanguageCode='string',
    TargetLanguageCode='string',
    Settings={
        'Formality': 'FORMAL'|'INFORMAL',
        'Profanity': 'MASK'
    }
)
```

### Return type
`dict`

Returns
Response Syntax:

```dict
{
    'TranslatedText': 'string',
    'SourceLanguageCode': 'string',
    'TargetLanguageCode': 'string',
    'AppliedTerminologies': [
        {
            'Name': 'string',
            'Terms': [
                {
                    'SourceText': 'string',
                    'TargetText': 'string'
                },
            ]
        },
    ],
    'AppliedSettings': {
        'Formality': 'FORMAL'|'INFORMAL',
        'Profanity': 'MASK'
    }
}
```

### Parameters - Request syntax
`Text`  
(string) --     
[REQUIRED]      

The text to translate. The text string can be a maximum of 10,000 bytes long. Depending on your character set, this may be fewer than 10,000 characters.

`TerminologyNames`      
(list) --       
The name of the terminology list file to be used in the TranslateText request. You can use 1 terminology list at most in a TranslateText request. Terminology lists can contain a maximum of 256 terms.

(string) --

`SourceLanguageCode`             
(string) --         
[REQUIRED]

The language code for the language of the source text. The language must be a language supported by Amazon Translate. For a list of language codes, see Supported languages.

To have Amazon Translate determine the source language of your text, you can specify auto in the `SourceLanguageCode` field. If you specify `auto` , Amazon Translate will call [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) to determine the source language.

> **Note**        
> If you specify `auto` , you must send the `TranslateText` request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported.

`TargetLanguageCode`        
(string) --     
[REQUIRED]      

The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.

`Settings`      
(dict) --       
Settings to configure your translation output, including the option to set the formality level of the output text and the option to mask profane words and phrases.

`Formality`     
(string) --     
You can optionally specify the desired level of formality for translations to supported target languages. The formality setting controls the level of formal language usage (also known as register ) in the translation output. You can set the value to informal or formal. If you don't specify a value for formality, or if the target language doesn't support formality, the translation will ignore the formality setting.

If you specify multiple target languages for the job, translate ignores the formality setting for any unsupported target language.

For a list of target languages that support formality, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.

`Profanity`     
(string) --     
Enable the profanity setting if you want Amazon Translate to mask profane words and phrases in your translation output.

To mask profane words and phrases, Amazon Translate replaces them with the grawlix string “?$#@$“. This 5-character sequence is used for each profane word or phrase, regardless of the length or number of words.

Amazon Translate doesn't detect profanity in all of its supported languages. For languages that don't support profanity detection, see Unsupported languages in the Amazon Translate Developer Guide.

If you specify multiple target languages for the job, all the target languages must support profanity masking. If any of the target languages don't support profanity masking, the translation job won't mask profanity for any target language.