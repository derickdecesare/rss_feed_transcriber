import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import dotenv


dotenv.load_dotenv()

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')



def send_email(transcription):

    # create the email message
    message = Mail(
        from_email=('spanish@derick.io', 'Podcast Transcription'),
        to_emails='deerriicckk@gmail.com',
        subject='Transcription and Translation For Lastest Podcast',
        plain_text_content=transcription
        # html_content=transcription
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("Email sent successfully.")
    except Exception as e:
        print(str(e))
    


# def send_email(content):
#     message = Mail(
#         from_email=('newsletter@derick.io', 'Spanish Snacks'),
#         to_emails='deerriicckk@gmail.com',
#         subject='Daily Spanish Lesson',
#         # plain_text_content=content
#         html_content=content
#     )
#     try:
#         sg = SendGridAPIClient(SENDGRID_API_KEY)
#         response = sg.send(message)
#         print("Email sent successfully.")
#     except Exception as e:
#         print(str(e))




if __name__ == "__main__":

        # fetch the transcription_and_translation.txt file
    with open('transcription_and_translation.txt', 'r', encoding='utf-8') as file:
        transcription = file.read()

    send_email(transcription)
