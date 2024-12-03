import base64
import requests
import datetime

# Replace with your actual Consumer Key and Secret
consumer_key = 'lCAGLXnxknxNeZ3efY2iFSfEmJmNYteeo1YPCxi0OyFpBOPh'
consumer_secret = 't3jaxeThbHYG6xVQo01yFHvMCI9AVR7ZY6nlhdtNtGHxLPj3DgrG0kVcqGJAuymj'

# Step 1: Generate Access Token
api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
auth = base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {auth}'
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access Token:", access_token)

    # Step 2: STK Push API
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "BusinessShortcode": "your_shortcode",  # Replace with your shortcode
        "LipaNaMpesaOnlineShortcode": "your_shortcode",  # Replace with your shortcode
        "LipaNaMpesaOnlineShortcodePassword": "your_shortcode_password",  # Replace with your password
        "PhoneNumber": "customer_phone_number",  # Replace with the customer's phone number
        "Amount": 100,  # Replace with the amount to be paid
        "AccountReference": "Account1234",  # Your account reference
        "TransactionDesc": "Payment for goods"
    }

    stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    response = requests.post(stk_push_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("STK Push Request Successful")
        print(response.json())  # Print the response from the API
    else:
        print(f"Error in STK Push: {response.status_code}")
        print(response.text)

else:
    print(f"Error: {response.status_code}")
