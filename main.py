import requests
import bs4
import smtplib

HEADERS = (
    {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en;q=0.8'
    }
)
PRODUCT_URL = "Copy and paste the product URL here"
response = requests.get(PRODUCT_URL, headers=HEADERS)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

PRODUCT_NAME = soup.find('span', id="productTitle").getText()
curr_price = float(soup.find("span", class_='a-offscreen').getText().replace(",", "")[1:])
watch_price = "Type the price you want to watch here in integer/decimal format"

if curr_price <= watch_price:
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "Paste your gmail id here "
    password = "Generate a google-app-password for this python program and paste it here"
    receiver_email = sender_email
    message = f"Subject:Amazon Price Alert!\n\n{PRODUCT_NAME}\ncurrent price:{curr_price}\n{PRODUCT_URL}"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=message
        )
        print("Email sent!")
        server.quit()
    except Exception as e:
        print("Error: unable to send email")
        print(e)

