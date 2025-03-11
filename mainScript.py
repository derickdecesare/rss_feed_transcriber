from openai import OpenAI
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sqlite3
from datetime import date
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI()

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')



## NOTES
# we should have the model format in markdown and then maybe we can use that directly in the email?
# bonus if we can use markdown in the email or just  have it format  as html?? that would be good too..

# eventualy want to move this to o1 for planning the lesson -- and maybe searching for some current events or something like that to inspire the story/lesson so that it is always fresh...
def generate_lesson():
    prompt = "Generate a simple Spanish lesson for beginners focusing on a specific grammar point and vocabulary, followed by a short story that includes these elements. Format the output as HTML, using appropriate tags for headings, paragraphs, and emphasis."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Spanish lessons formatted in HTML."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800
    )
    return response.choices[0].message.content.strip()




def send_email(content):
    message = Mail(
        from_email=('newsletter@derick.io', 'Spanish Snacks'),
        to_emails='deerriicckk@gmail.com',
        subject='Daily Spanish Lesson',
        # plain_text_content=content
        html_content=content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("Email sent successfully.")
    except Exception as e:
        print(str(e))



def main():
    # Generate the lesson
    lesson_content = generate_lesson()
    
    # Send the email with the lesson content
    send_email(lesson_content)


if __name__ == "__main__":
    main()