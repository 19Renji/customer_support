import imaplib
import email
from workflows.support_graph import (
    support_graph
)

EMAIL2 = "johndoeherecomes@gmail.com"
APP_PASSWORD2 = "zezn odjg qjuv vagx"



def process_emails():

    mail = imaplib.IMAP4_SSL(
        "imap.gmail.com"
    )

    mail.login(
        EMAIL2,
        APP_PASSWORD2
    )

    mail.select("inbox")

    status, messages = mail.search(
        None,
        "UNSEEN"
    )

    mail_ids = messages[0].split()

    for mail_id in mail_ids:

        status, msg_data = mail.fetch(
            mail_id,
            "(RFC822)"
        )

        raw_email = (
            msg_data[0][1]
        )

        msg = email.message_from_bytes(
            raw_email
        )

        sender_email = (
            msg["From"]
        )

        subject = (
            msg["Subject"]
        )

        body = ""

        if msg.is_multipart():

            for part in msg.walk():

                if (
                    part.get_content_type()
                    ==
                    "text/plain"
                ):

                    body = (

                        part.get_payload(
                            decode=True
                        )

                        .decode()
                    )

        else:

            body = (

                msg.get_payload(
                    decode=True
                )

                .decode()
            )

        print(
            "Processing Email:",
            sender_email
        )

        support_graph.invoke(

            {

                "transcript":
                    body,

                "customer_email":
                    sender_email
            }
        )

    try:

        mail.close()

        mail.logout()

    except Exception as e:

        print(
        "Connection already closed:",
        e
    )