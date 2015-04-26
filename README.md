# PyGun
Simple python module for communicating with Mailgun API.

## How to install

```
pip install -e git+https://github.com/grafa/pygun#egg=pygun
```

## Usage
Module aims for simple usage. We don't want complicated API's for Python modules since Python is so simple and still powerful.

```python
m = PyGun("your api key", "your mailbox url")
m.sender("my@mail.com", "My Sandbox")
m.to("recipient@mail.com", "John Doe")
m.subject("My first email")
m.text("Hi there! Check this great API for sending email messages.")
response = m.send()
```

And you get pythojn dict response just like from Mailgun API:
```python
print response
{u'message': u'Queued. Thank you.', u'id': u'<20151426082848.27906.64814@sandboxbcf4ef3bde1d4b9e88c0a2d4e8afb579.mailgun.org>'}
```

## Roadmap
* Add HTML support
