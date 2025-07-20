from fastapi import FastAPI, Request
import os
import requests
from dotenv import load_dotenv
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI()

# Slack bot token
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_API_URL = "https://slack.com/api"

@app.post("/slack/events")
async def slack_events(request: Request):
    """Handle Slack events."""
    data = await request.json()
    
    # Handle URL verification challenge
    if data.get('type') == 'url_verification':
        print("🔗 URL verification challenge received")
        return {"challenge": data['challenge']}
    
    # Handle events
    if data.get('type') == 'event_callback':
        event = data['event']
        
        # Handle direct messages
        if event.get('type') == 'message' and event.get('channel_type') == 'im':
            # Skip bot's own messages
            if event.get('bot_id'):
                return {"status": "ok"}
            
            print(f"📧 New DM received: {event.get('text', '')}")
            
            # Send auto-reply
            send_reply(event['channel'], event['ts'])
    
    return {"status": "ok"}

def send_reply(channel_id, thread_ts):
    """Send a reply to a message."""
    reply_text = "test\nyup its working"
    
    headers = {
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'channel': channel_id,
        'text': reply_text
    }
    
    try:
        response = requests.post(
            f'{SLACK_API_URL}/chat.postMessage',
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            print("✅ Auto-reply sent!")
        else:
            print(f"❌ Error sending reply: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 Starting Slack Webhook Server")
    print("📡 Server will be available at: http://localhost:8000/slack/events")
    print("🔗 Use ngrok to expose this URL to Slack")
    uvicorn.run(app, host="0.0.0.0", port=8000) 