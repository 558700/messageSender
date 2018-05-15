# README

You will need

- A google sheet, with phone numbers in the A column, and a message in the B column.
    - Make sure numbers are correctly formatted, i.e. "079892 443 993" becomes "+4479892443993"
- A twilio account, with paid-up billing.

You will need a Google developer account to use the sheets API. https://developers.google.com/sheets/api/quickstart/python

I believe I wrote this with Python3 in mind, but it might still be using Python. Make sure you have installed the following:

```
pip3 install google-api-python-client httplib2 oauth2client twilio-python
```

If needed, you can bypass the Google sheets interface entirely, just comment out the apiclient and oauth2client imports on lines 3 and 4, and lines 9-23.
You can then directly input an array of correctly formatted numbers in the `numbers` variable on line 32, and uncomment the message variable on line 50.

## DEADLY IMPORTANT

To save on costly messages, make sure your message content is correctly GSM encoded. Check any outgoing messages here first:  http://chadselph.github.io/smssplit/.
Remove any red-underlined content.
