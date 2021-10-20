import imaplib, email, os

user = 'diegordatos@gmail.com'
password = 'sashalanegra'
imap_url = 'imap.gmail.com'
attachment_dir = 'C:/Users/Diego/Downloads'
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))

def search(key,  con):
    result, data = con.search(None,key)
    return data

def get_emails(result_bytes):
    msgs=[]
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs
con = imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select('INBOX')



result, data = con.fetch(b'10','(RFC822)')
msgs = get_emails(search('From diegordatos@gmail.com UnSeen' ,  con))

for msg in msgs:
    get_attachments((email.message_from_bytes(msg[0][1])))
