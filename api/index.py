from flask import Flask, request, jsonify, render_template_string
import os
import json
from datetime import datetime

app = Flask(__name__)

# Load the product.md context
def load_product_context():
    try:
        with open('product.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Knowledge base not found."

# Simplified Kiro response generator (same logic as test_app.py)
def get_kiro_response(user_query, context):
    query_lower = user_query.lower()

    # TRAFFIC & ROUTE QUERIES
    if any(word in query_lower for word in ["sitabuldi", "traffic", "jam", "route", "how to get", "commute"]):
        if "sitabuldi" in query_lower and ("6" in query_lower or "evening" in query_lower or "5" in query_lower):
            return """🔥 **Sitabuldi at evening peak? Bhau, you're braver than me!**

**Reality Check:**
- Normal time: 20-25 mins
- Reality at 5-7 PM: 45-60 mins (sometimes 90+ mins)
- Root cause: Office rush + bus convergence + narrow roads

**Your Survival Options:**
1. **Escape Plan A (Best)**: Leave office at 5 PM sharp, beat the rush
2. **Escape Plan B (Smart)**: Take Route 1 bus ₹8 (15 mins platform wait, but moves fast)
3. **Escape Plan C (Rich)**: Uber/Ola ₹70-100 (guaranteed time, but surge pricing brutal)

**If Already Stuck:**
- Chai corner near Sitabuldi railway station (strong chai, ₹10)
- Settle in, it'll move in 30 mins
- Check Ramdaspeth shops if REALLY stuck

**Pro Move:** Work from a cafe in Sitabuldi till 7 PM, then leave when traffic clears.

**Jaldi chal, bhau!** ✅"""

        elif "dharampeth" in query_lower:
            return """**Dharampeth route – Good news, this is solid! ✅**

**Traffic Profile:**
- Status: Moderate, usually manageable
- Peak jam: 7-9 AM (office commute), 5-7 PM (return rush)
- Normal time: 15-20 mins to most places
- Chaos level: Yellow ⚠️

**Best Routes from Dharampeth:**
- To Sitabuldi: Via Warora Road (20 mins) OR Ring Road detour (25 mins, clearer)
- To South Nagpur: Direct is best, ~20 mins
- To Ramdaspeth: Via Congress Nagar, ~15 mins

**Transport Options:**
- Auto: ₹60-100 (negotiate for ₹50 if regular)
- Bus: Route 4 ideal, ₹8-12, reliable timing
- Walking: 15-minute walk to Congress Nagar bus stop

**Time Estimate Today:**
- Morning (7-9 AM): +10 mins buffer
- Afternoon (12-4 PM): On-time, no buffer needed ✅"""

    # METRO QUERIES
    if any(word in query_lower for word in ["metro", "subway", "underground"]):
        return """🚇 **Nagpur Metro – The Real Game Changer!**

**Been running since 2019** - not some distant dream anymore!

**Your Options:**
- **Aqua Line**: Sitabuldi ↔ Airport (15 stations, 13.8 km) - connects city to airport in 25 mins
- **Orange Line**: Khapri ↔ Automotive Square (11 stations, 9.6 km) - serves industrial areas

**Real Impact:**
- **Traffic Reduction**: 30% less autos on roads, breathing easier in Nagpur
- **Time Savings**: Sitabuldi to Airport now 25 mins instead of 90 mins in traffic
- **Safety**: Well-lit stations, women-only coaches - peace of mind
- **Environment**: 50,000+ cars off roads daily, cleaner air for our kids

**Practical Tips:**
- Buy smart card ₹50 (rechargeable, saves ₹2 per trip)
- Women-only compartments during peak hours
- Free WiFi at all stations
- Frequency: Every 3-5 mins during peak hours
- Operating Hours: 6:00 AM - 11:00 PM daily

**Bottom Line:** Why suffer in traffic when metro saves you 1+ hour daily and costs less?

Try it tomorrow, bhau! ✅"""

    # FARE QUERIES
    if any(word in query_lower for word in ["fare", "cost", "price", "kitna lagega"]):
        return """💰 **Auto Fare Guide – Know Before You Go!**

**Zone 1 (Central/Downtown):**
- Within Sitabuldi/Ramdaspeth/Zero Mile: ₹30-50 (no meter usually)
- Short hop: ₹40-60

**Zone 2 (Mid-Distance):**
- Dharampeth→Civil Lines: ₹80-120
- Ramdaspeth→Ambazari: ₹100-150
- Sitabuldi→South Nagpur: ₹120-180

**Zone 3 (Long Distance):**
- Zero Mile→Gorewada: ₹150-250
- Sitabuldi→Warora Road: ₹200-300

**Negotiation Script:**
1. Ask: "Kitna lagega?" (How much will it cost?)
2. Driver quotes: "₹120, bhau"
3. Counter: "Bhau, 80 de na?" (Give me ₹80?)
4. Close: "Theek hai, chal!" (Okay, let's go!)

**Pro Tips:**
- Most autos WON'T use meters – it's normal in Nagpur
- Negotiate hard, but be fair
- Night fares are 1.5x (9 PM-6 AM)
- Keep small change ready

**Remember:** Haggling is part of the culture, but respect the driver! ✅"""

    # SAFETY QUERIES
    if any(word in query_lower for word in ["safe", "safety", "alone", "night", "woman", "female"]):
        return """🛡️ **Safety First – Your Security Matters!**

**For Women/Evening Travel:**
- **Best Option**: Ola/Uber (tracked, safer, ₹150-250)
- **Women-Only Metro**: Available during peak hours
- **Avoid**: Walking alone at night, sharing autos with strangers

**General Safety Rules:**
- Always confirm fare BEFORE entering auto
- Keep phone charged and location sharing ON
- Avoid isolated areas, especially at night
- Trust your instincts – if something feels wrong, don't proceed

**Emergency Contacts:**
- Police: 100
- Women Helpline: 181
- Auto driver complaints: Local RTO

**Real Talk:** Your safety is worth the extra cost. Better to pay more and reach home safely than risk shortcuts.

Stay safe, bhau! 🛡️✅"""

    # DEFAULT RESPONSE
    return f"""🚕 **Nagpur Daily Commuter Guide**

I understand you're asking about: "{user_query}"

**Quick Answers:**
- For traffic/routes: Ask about specific locations (e.g., "Dharampeth to Sitabuldi")
- For fares: Mention pickup and drop locations
- For safety: Be specific about time and situation
- For metro: Ask about routes or general info

**Popular Queries:**
- "How do I get from Dharampeth to Sitabuldi at 6 PM?"
- "What's the auto fare from Sitabuldi to Ramdaspeth?"
- "Tell me about Nagpur Metro"
- "Is it safe to travel alone at night?"

Try one of these, or ask something specific about Nagpur commuting! ✅"""

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚕 Nagpur Daily Commuter Guide</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        h1 {
            color: #d32f2f;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .chat-container {
            margin: 20px 0;
        }
        .message {
            margin: 10px 0;
            padding: 15px;
            border-radius: 10px;
            line-height: 1.6;
        }
        .user-message {
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            margin-left: 20%;
        }
        .kiro-message {
            background-color: #fff9e6;
            border-left: 4px solid #ff9800;
            margin-right: 20%;
        }
        .input-container {
            margin: 20px 0;
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            padding: 12px 24px;
            background: #d32f2f;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }
        button:hover {
            background: #b71c1c;
        }
        .sample-queries {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .sample-queries h3 {
            margin-top: 0;
            color: #666;
        }
        .query-btn {
            background: #2196f3;
            color: white;
            border: none;
            padding: 8px 16px;
            margin: 5px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        .query-btn:hover {
            background: #1976d2;
        }
        .status {
            text-align: center;
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚕 Nagpur Daily Commuter Guide</h1>
        <p style="text-align: center; color: #666; margin-bottom: 30px;">
            <strong>AI-powered hyper-local assistant for navigating Nagpur's traffic chaos</strong><br>
            Powered by Kiro with real-time local expertise
        </p>

        <div class="chat-container" id="chat-container">
            <div class="message kiro-message">
                <strong>🚕 Kiro:</strong><br>
                Namaste! I'm your Nagpur commuting buddy. Ask me anything about traffic, fares, safety, or metro routes. What can I help you with today?
            </div>
        </div>

        <div class="input-container">
            <input type="text" id="user-input" placeholder="Ask about Nagpur traffic, fares, safety..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Send</button>
        </div>

        <div class="sample-queries">
            <h3>💡 Try these sample queries:</h3>
            <button class="query-btn" onclick="setQuery('How do I get from Dharampeth to Sitabuldi at 6 PM?')">Dharampeth → Sitabuldi at 6 PM</button>
            <button class="query-btn" onclick="setQuery('What\\'s the auto fare from Sitabuldi to Ramdaspeth?')">Auto fare Sitabuldi → Ramdaspeth</button>
            <button class="query-btn" onclick="setQuery('Tell me about Nagpur Metro')">About Nagpur Metro</button>
            <button class="query-btn" onclick="setQuery('Is it safe to travel alone at night?')">Night safety</button>
            <button class="query-btn" onclick="setQuery('What\\'s the traffic like in monsoon?')">Monsoon traffic</button>
        </div>

        <div class="status" id="status">
            Ready to help with your Nagpur commuting questions!
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();
            if (!message) return;

            // Add user message
            addMessage(message, 'user-message', 'You');

            // Clear input
            input.value = '';

            // Show typing indicator
            document.getElementById('status').innerHTML = '🤔 Thinking...';

            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message }),
                });

                const data = await response.json();

                // Add Kiro response
                addMessage(data.response, 'kiro-message', '🚕 Kiro');

            } catch (error) {
                addMessage('Sorry, I encountered an error. Please try again.', 'kiro-message', '🚕 Kiro');
            }

            document.getElementById('status').innerHTML = 'Ready to help with your Nagpur commuting questions!';
        }

        function addMessage(text, className, sender) {
            const container = document.getElementById('chat-container');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${className}`;
            messageDiv.innerHTML = `<strong>${sender}:</strong><br>${text.replace(/\n/g, '<br>')}`;
            container.appendChild(messageDiv);
            container.scrollTop = container.scrollHeight;
        }

        function setQuery(query) {
            document.getElementById('user-input').value = query;
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # Load context and generate response
    context = load_product_context()
    response = get_kiro_response(user_message, context)

    return jsonify({'response': response})

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'knowledge_base_size': len(load_product_context())
    })

if __name__ == '__main__':
    app.run(debug=True)