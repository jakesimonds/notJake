# Slack Bot Auto-Reply Setup

Much easier than Gmail! Here's how to set it up:

## 1. Create a Slack App

1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name it something like "Auto-Reply Bot"
4. Select your workspace

## 2. Add Bot Token Scopes

1. Go to "OAuth & Permissions" in the left sidebar
2. Under "Scopes" → "Bot Token Scopes", add:
   - `channels:history` (read channel messages)
   - `channels:read` (view channels)
   - `chat:write` (send messages)
   - `groups:history` (read private channel messages)
   - `groups:read` (view private channels)
   - `im:history` (read DMs)
   - `im:read` (view DMs)
   - `mpim:history` (read group DMs)
   - `mpim:read` (view group DMs)

## 3. Install App to Workspace

1. Go to "OAuth & Permissions"
2. Click "Install to Workspace"
3. Authorize the app
4. Copy the "Bot User OAuth Token" (starts with `xoxb-`)

## 4. Update .env File

Replace the placeholder in `.env`:
```
SLACK_BOT_TOKEN=xoxb-your-actual-bot-token-here
```

## 5. Run the Bot

```bash
uv run python slack_auto_reply.py
```

## 6. Test It

1. Send a message in any channel where the bot is present
2. Or DM the bot directly
3. You should get an auto-reply: "test\nyup its working"

## Features

- ✅ Auto-replies to messages in channels and DMs
- ✅ Replies in threads to keep conversations organized
- ✅ Prevents duplicate replies
- ✅ Easy to test (just DM yourself!)
- ✅ Perfect for LLM integration later

## Cloud Deployment

When you're ready to deploy:
1. Same code works on any server
2. Just update the environment variable
3. No complex OAuth setup needed
4. Works great with AWS Lambda, Heroku, etc.

Much simpler than Gmail! 🎉 