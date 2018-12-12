#### Catch MailGun WebHooks with Python3 + SQLAlchemy + Webhook Signature Verification


API Routes:
```
{
  "clicks": "/api/v1/wh/mg/lead/email/click", 
  "delivered": "/api/v1/wh/mg/lead/email/delivered", 
  "dropped": "/api/v1/wh/mg/lead/email/dropped", 
  "hard-bounce": "/api/v1/wh/mg/lead/email/bounced", 
  "opens": "/api/v1/wh/mg/lead/email/open", 
  "spam-complaint": "/api/v1.0/wh/mg/lead/email/spam/complaint", 
  "unsubscribe": "/api/v1.0/wh/mg/lead/email/unsubscribe"
}
```

Signature Verification:

```
def verify(api_key, token, timestamp, signature):
    hmac_digest = hmac.new(key=mailgun_api_key,
                           msg='{}{}'.format(timestamp, token).encode('utf-8'),
                           digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, hmac_digest)
```
