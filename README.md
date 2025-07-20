# Gmail Auto-Reply System

A local Python application that monitors your Gmail inbox and automatically sends replies to new emails.

## Features

- 🔍 Monitors Gmail inbox for new unread messages
- 📧 Automatically sends replies to incoming emails
- 🔐 Secure OAuth2 authentication with Gmail API
- 🚫 Prevents duplicate replies to the same message
- 📝 Marks processed messages as read

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Gmail API Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it
4. Create OAuth 2.0 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - Choose "Desktop application"
   - Download the credentials file
5. Rename the downloaded file to `credentials.json` and place it in this directory

### 3. Run the Application

```bash
python gmail_auto_reply.py
```

On first run, you'll be prompted to authenticate with your Gmail account. A browser window will open for OAuth2 authorization.

## How It Works

1. **Authentication**: Uses OAuth2 to securely access your Gmail account
2. **Monitoring**: Checks for new unread messages every 30 seconds
3. **Processing**: For each new email:
   - Extracts sender, subject, and body
   - Sends an auto-reply with "test\nyup its working"
   - Marks the original message as read
   - Prevents duplicate processing

## Configuration

### Auto-Reply Message
To change the auto-reply content, edit the `reply_text` variable in the `send_auto_reply` method:

```python
reply_text = "Your custom auto-reply message here"
```

### Check Interval
To change how often the system checks for new emails, modify the `check_interval` parameter in the `run()` method:

```python
auto_reply.run(check_interval=60)  # Check every 60 seconds
```

## Security Notes

- Credentials are stored locally in `token.json`
- Never commit `credentials.json` or `token.json` to version control
- The application only requests necessary Gmail permissions

## Troubleshooting

### Common Issues

1. **"credentials.json not found"**
   - Make sure you've downloaded and renamed the OAuth2 credentials file

2. **Authentication errors**
   - Delete `token.json` and re-authenticate
   - Ensure your Google Cloud project has Gmail API enabled

3. **Permission denied**
   - Check that your OAuth2 credentials have the correct scopes
   - Verify the Gmail API is enabled in your Google Cloud project

## Next Steps

This local setup can be extended to:
- Integrate with LLM APIs for intelligent responses
- Deploy to AWS Lambda for serverless operation
- Add more sophisticated email filtering and routing
- Implement conversation threading and context awareness

## Files

- `gmail_auto_reply.py` - Main application
- `requirements.txt` - Python dependencies
- `credentials.json` - Gmail API credentials (you need to add this)
- `token.json` - OAuth2 tokens (generated automatically) 