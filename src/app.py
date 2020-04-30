import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

from src.carriers import carrier2email
from src.constants import RECIPIENTS, EMAIL_CONFIG, PROFILES
from src.scrape_insta import get_latest_post_for_profile


def main():
    # prepare numbers as emails appropriately based on carrier
    to_emails = ','.join([f'{number_obj["number"]}{carrier2email[number_obj["carrier"]]["mms"]}'
                          for number_obj in RECIPIENTS])

    with smtplib.SMTP_SSL(EMAIL_CONFIG['host'], EMAIL_CONFIG['port']) as server:
        server.ehlo()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])

        # mime stands for "Multipurpose Internet Mail Extensions"
        msg = MIMEMultipart()
        msg['To'] = to_emails
        msg['From'] = EMAIL_CONFIG['email']

        for user in PROFILES:
            post = get_latest_post_for_profile(user)
            req = requests.get(post.image_url, stream=True)
            image = MIMEImage(req.content)
            msg.attach(image)

            caption = MIMEText(post.caption)
            msg.attach(caption)

            # send emails and close connection
            server.sendmail(from_addr=msg['From'], to_addrs=msg['To'], msg=msg.as_string())


if __name__ == '__main__':
    main()
