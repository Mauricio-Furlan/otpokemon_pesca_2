from imgurpython import ImgurClient
from twilio.rest import Client

def load_img(file_name):
    client_id = '<CLIENT_ID>'
    client_secret = '<SECRET>'
    client = ImgurClient(client_id, client_secret)
    result = client.upload_from_path(file_name)
    print('Upload realizado com sucesso!')
    return result['link']

def send_watsapp_msg(url):
    account_sid = '<ACCOUNT_SID>'
    auth_token = '<AUTH_TOKEN>'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+<YOURCODE>',
    body=url,
    to='whatsapp:+55<PHONE_NUMBER>'
    )
    print('Mensagem enviada com sucesso!')