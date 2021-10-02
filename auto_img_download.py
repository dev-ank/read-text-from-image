import imaplib, email, os
from credentials import attachment_dir



#dowloads the image from the recent mail
def get_attachment(user,password,imap_url):

    con = imaplib.IMAP4_SSL(imap_url)
    try:
        con.login(user,password)
        inbox = con.select('INBOX')
        result, data = con.fetch(inbox[1][0], '(RFC822)')
        raw = email.message_from_bytes(data[0][1])

        for part in raw.walk():
            filename = part.get_filename()

            if filename is not None:
                filepath = os.path.join(attachment_dir, filename)
                with open(filepath,'wb') as f:
                    f.write(part.get_payload(decode=True))
                    return filepath
            else:
                continue

        return None

    except Exception as e:
        print('Exception occured in get_attachment:',e)

















