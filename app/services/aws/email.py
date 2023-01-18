from app.services.aws.s3 import ses

class EmailService(object):
    def __init__(self, *args, **kwargs):
        self.conn = ses

    def send_aws(self, RECIPIENT, SUBJECT, TEXT,
                 SENDER='Jornada Ser <no-reply@minimegaleitor.com.br>'):

        CHARSET = "UTF-8"
        BODY_TEXT = TEXT
        BODY_HTML = TEXT

        try:
            response = self.conn.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False
        except:
            return False
