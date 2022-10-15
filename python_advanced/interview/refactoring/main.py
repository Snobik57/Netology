from email_class import EmailAccount


if __name__ == "__main__":
    email_account = EmailAccount(
        login='login@gmail.com',
        password='qwerty',
        subject='Subject',
        gmail_smtp="smtp.gmail.com",
        gmail_imap="imap.gmail.com"
    )

    email_account.send_message(
        recipients=['vasya@email.com', 'petya@email.com'],
        massage='Message',
    )

    email_account.receive()
