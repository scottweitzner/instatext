import random
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import toml
from carriers import carrier2email
from scrape_insta import scrape_insta

config = toml.load('/Users/ScottWeitzner/Desktop/insta-text/config.toml')
EMAIL_CONFIG = config['email']


def main():
    # prepare numbers as emails appropriately based on carrier
    number_objects = config['sending']['to']
    to_emails = ','.join([f'{number_obj["number"]}{carrier2email[number_obj["carrier"]]["mms"]}'
                          for number_obj in number_objects])

    with smtplib.SMTP_SSL(EMAIL_CONFIG['host'], EMAIL_CONFIG['port']) as server:
        server.ehlo()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])

        # mime stands for "Multipurpose Internet Mail Extensions"
        msg = MIMEMultipart()
        msg['To'] = to_emails
        msg['From'] = EMAIL_CONFIG['email']

        for user in config['instagram']['profiles']:
            posts = scrape_insta(user)
            post = posts[random.randint(0, len(posts))]

            req = requests.get(post.image_url, stream=True)
            image = MIMEImage(req.content)
            msg.attach(image)

            caption = MIMEText(post.caption)
            msg.attach(caption)

            # send emails and close connection
            server.sendmail(from_addr=msg['From'], to_addrs=msg['To'], msg=msg.as_string())


if __name__ == '__main__':
    main()
