from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Load the product.md context
def load_product_context():
    try:
        # Try multiple paths for Vercel deployment
        paths_to_try = [
            'product.md',
            '../product.md',
            os.path.join(os.path.dirname(__file__), '..', 'product.md'),
            '/var/task/product.md'
        ]
        for path in paths_to_try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
        return "Knowledge base loaded."
    except Exception as e:
        return f"Error: {str(e)}"

# Simplified Kiro response generator
def get_kiro_response(user_query, context, user_area=None):
    query_lower = user_query.lower()
    
    # Location-aware prefix for responses
    location_prefix = ""
    if user_area:
        location_prefix = f"📍 Since you're near **{user_area}**, here's my advice:\n\n"

    # TRAFFIC & ROUTE QUERIES
    if any(word in query_lower for word in ["sitabuldi", "traffic", "jam", "route", "how to get", "commute"]):
        if "sitabuldi" in query_lower and ("6" in query_lower or "evening" in query_lower or "5" in query_lower):
            return location_prefix + """🔥 **Sitabuldi at evening peak? Bhau, you're braver than me!**

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
            return location_prefix + """**Dharampeth route – Good news, this is solid! ✅**

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

        else:
            return location_prefix + """🚗 **Traffic Update for Nagpur**

**Current Status:** Moderate traffic across the city

**Hot Spots Right Now:**
- Sitabuldi Junction: Heavy (as always!)
- Ramdaspeth: Moderate
- Wardha Road: Clear
- Ring Road: Smooth

**Pro Tips:**
- Avoid Sitabuldi during 5-7 PM
- Use Ring Road for longer distances
- Metro is fastest for Airport ↔ City travel

Ask me about specific routes for detailed advice! ✅"""

    # METRO QUERIES
    if any(word in query_lower for word in ["metro", "subway", "underground"]):
        return location_prefix + """🚇 **Nagpur Metro – The Real Game Changer!**

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
    if any(word in query_lower for word in ["fare", "cost", "price", "kitna lagega", "auto"]):
        return location_prefix + """💰 **Auto Fare Guide – Know Before You Go!**

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
        return location_prefix + """🛡️ **Safety First – Your Security Matters!**

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

    # MONSOON QUERIES
    if any(word in query_lower for word in ["rain", "monsoon", "flood", "waterlog"]):
        return location_prefix + """🌧️ **Monsoon Travel Guide – Stay Safe & Dry!**

**Danger Zones (AVOID in heavy rain):**
- Wardha Road near Medical College - floods first
- Itwari low-lying areas
- Zero Mile underpass

**Safe Routes:**
- Ring Road (elevated, good drainage)
- NH44 (highway standard)
- Metro (obviously!)

**Monsoon Tips:**
- Check weather before leaving
- Keep extra time buffer (roads get slow)
- Avoid autos in heavy rain (they'll refuse anyway)
- Use Ola/Uber with rain surge (painful but safe)

**If Stuck:**
- Find a chai shop, wait it out
- Don't try to cross flooded roads
- Keep emergency numbers handy

**Real Talk:** Nagpur monsoon is unpredictable. Better late than stuck! 🌧️✅"""

    # DEFAULT RESPONSE
    location_tip = ""
    if user_area:
        location_tip = f"\n\n📍 **Your Location**: You're near {user_area}. Try asking:\n- 'How is traffic from {user_area} right now?'\n- 'Best route from {user_area} to Sitabuldi'"
    
    clean_query = user_query.replace('[User is near ', '').split(']')[-1].strip() if '[User is near' in user_query else user_query
    
    return f"""🚕 **Nagpur Daily Commuter Guide**

I understand you're asking about: "{clean_query}"

**I can help you with:**
- 🚗 **Traffic & Routes**: "How to get from Dharampeth to Sitabuldi at 6 PM?"
- 💰 **Auto Fares**: "What's the fare from Sitabuldi to Ramdaspeth?"
- 🚇 **Metro Info**: "Tell me about Nagpur Metro"
- 🛡️ **Safety**: "Is it safe to travel alone at night?"
- 🌧️ **Monsoon**: "Is Wardha Road safe in rain?"

**Popular Queries:**
- "Traffic update for Sitabuldi"
- "Auto fare guide"
- "Metro timings"
- "Night travel safety tips"{location_tip}

Try one of these, or ask something specific about Nagpur commuting! ✅"""


# HTML template for the web interface
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚕 Nagpur Daily Commuter Guide</title>
    <style>
        * { box-sizing: border-box; }
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
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-top: 20px;
        }
        h1 {
            color: #d32f2f;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-size: 14px;
        }
        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            margin: 20px 0;
            padding: 10px;
            background: #f9f9f9;
            border-radius: 10px;
        }
        .message {
            margin: 10px 0;
            padding: 12px 15px;
            border-radius: 10px;
            line-height: 1.6;
            font-size: 14px;
        }
        .user-message {
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            margin-left: 15%;
        }
        .kiro-message {
            background-color: #fff9e6;
            border-left: 4px solid #ff9800;
            margin-right: 15%;
        }
        .input-container {
            display: flex;
            gap: 10px;
            margin: 15px 0;
        }
        #user-input {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            outline: none;
        }
        #user-input:focus {
            border-color: #667eea;
        }
        #send-btn {
            padding: 12px 24px;
            background: #d32f2f;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        #send-btn:hover {
            background: #b71c1c;
        }
        #send-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        .location-banner {
            background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
            color: white;
            padding: 12px 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }
        .location-banner button {
            background: white;
            color: #2E7D32;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        .sample-queries {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        .sample-queries h3 {
            margin: 0 0 10px 0;
            color: #666;
            font-size: 14px;
        }
        .query-btn {
            background: #2196f3;
            color: white;
            border: none;
            padding: 8px 12px;
            margin: 4px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 13px;
        }
        .query-btn:hover {
            background: #1976d2;
        }
        .nearby-suggestions {
            background: #e8f5e9;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #4CAF50;
            display: none;
        }
        .status {
            text-align: center;
            color: #666;
            font-size: 13px;
            margin-top: 10px;
        }
        @media (max-width: 600px) {
            .container { padding: 15px; }
            h1 { font-size: 1.5em; }
            .message { margin-left: 0 !important; margin-right: 0 !important; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚕 Nagpur Daily Commuter Guide</h1>
        <p class="subtitle">AI-powered assistant for navigating Nagpur's traffic | Powered by Kiro</p>

        <div class="location-banner">
            <div>
                <span id="location-icon">📍</span>
                <span id="location-text">Enable location for personalized suggestions</span>
            </div>
            <button id="location-btn">Enable Location</button>
        </div>

        <div class="nearby-suggestions" id="nearby-suggestions">
            <div id="suggestions-content"></div>
        </div>

        <div class="chat-container" id="chat-container">
            <div class="message kiro-message">
                <strong>🚕 Kiro:</strong><br>
                Namaste! I'm your Nagpur commuting buddy. Ask me about traffic, fares, safety, or metro routes. Click "Enable Location" above for personalized tips!
            </div>
        </div>

        <div class="input-container">
            <input type="text" id="user-input" placeholder="Ask about Nagpur traffic, fares, safety...">
            <button id="send-btn">Send</button>
        </div>

        <div class="sample-queries">
            <h3>💡 Quick queries (click to try):</h3>
            <button class="query-btn" data-query="How to get from Dharampeth to Sitabuldi at 6 PM?">Dharampeth → Sitabuldi</button>
            <button class="query-btn" data-query="What is the auto fare from Sitabuldi to Ramdaspeth?">Auto Fares</button>
            <button class="query-btn" data-query="Tell me about Nagpur Metro">Metro Info</button>
            <button class="query-btn" data-query="Is it safe to travel alone at night?">Night Safety</button>
            <button class="query-btn" data-query="Traffic update for Sitabuldi">Traffic Update</button>
        </div>

        <div class="status" id="status">Ready to help! 🚗</div>
    </div>

    <script>
        // State variables
        var userLocation = null;
        var userArea = null;

        var nagpurAreas = [
            { name: 'Sitabuldi', lat: 21.1458, lng: 79.0882, nearby: ['Zero Mile', 'Ramdaspeth'] },
            { name: 'Dharampeth', lat: 21.1395, lng: 79.0756, nearby: ['Seminary Hills', 'Congress Nagar'] },
            { name: 'Ramdaspeth', lat: 21.1377, lng: 79.0919, nearby: ['Sitabuldi', 'Sadar'] },
            { name: 'Civil Lines', lat: 21.1591, lng: 79.0765, nearby: ['Railway Station', 'VCA Ground'] },
            { name: 'Wardha Road', lat: 21.1167, lng: 79.1083, nearby: ['Medical College', 'Ajni'] },
            { name: 'Itwari', lat: 21.1551, lng: 79.0918, nearby: ['Gandhibagh', 'Cotton Market'] },
            { name: 'Ambazari', lat: 21.1285, lng: 79.0502, nearby: ['VNIT', 'Ambazari Lake'] },
            { name: 'Airport Area', lat: 21.0922, lng: 79.0472, nearby: ['Khapri', 'Wardha Road'] }
        ];

        // DOM Elements
        var chatContainer = document.getElementById('chat-container');
        var userInput = document.getElementById('user-input');
        var sendBtn = document.getElementById('send-btn');
        var statusEl = document.getElementById('status');
        var locationBtn = document.getElementById('location-btn');
        var locationText = document.getElementById('location-text');
        var locationIcon = document.getElementById('location-icon');
        var nearbySuggestions = document.getElementById('nearby-suggestions');
        var suggestionsContent = document.getElementById('suggestions-content');

        // Add message to chat
        function addMessage(text, className, sender) {
            var div = document.createElement('div');
            div.className = 'message ' + className;
            var formattedText = text.replace(/\\n/g, '<br>').replace(/\n/g, '<br>');
            formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            div.innerHTML = '<strong>' + sender + ':</strong><br>' + formattedText;
            chatContainer.appendChild(div);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Send message function
        function sendMessage() {
            var message = userInput.value.trim();
            if (!message) return;

            sendBtn.disabled = true;
            sendBtn.innerHTML = '...';
            statusEl.innerHTML = '🤔 Thinking...';

            addMessage(message, 'user-message', 'You');
            userInput.value = '';

            var requestBody = { 
                message: message,
                area: userArea ? userArea.name : null
            };

            fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(requestBody)
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                var responseText = data.response || data.error || 'Got a response!';
                addMessage(responseText, 'kiro-message', '🚕 Kiro');
            })
            .catch(function(error) {
                console.error('Fetch error:', error);
                addMessage('Connection error. Please try again.', 'kiro-message', '🚕 Kiro');
            })
            .finally(function() {
                sendBtn.disabled = false;
                sendBtn.innerHTML = 'Send';
                statusEl.innerHTML = 'Ready to help! 🚗';
            });
        }

        // Find nearest area
        function findNearestArea(lat, lng) {
            var nearest = nagpurAreas[0];
            var minDist = Infinity;
            for (var i = 0; i < nagpurAreas.length; i++) {
                var area = nagpurAreas[i];
                var dist = Math.sqrt(Math.pow(lat - area.lat, 2) + Math.pow(lng - area.lng, 2));
                if (dist < minDist) { 
                    minDist = dist; 
                    nearest = area; 
                }
            }
            return nearest;
        }

        // Show nearby suggestions
        function showNearbySuggestions(area) {
            suggestionsContent.innerHTML = '<strong>📍 ' + area.name + '</strong> - Nearby: ' + area.nearby.join(', ');
            nearbySuggestions.style.display = 'block';
        }

        // Get location function
        function getLocation() {
            locationBtn.innerHTML = 'Detecting...';
            locationBtn.disabled = true;

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    function(pos) {
                        userLocation = { lat: pos.coords.latitude, lng: pos.coords.longitude };
                        userArea = findNearestArea(userLocation.lat, userLocation.lng);
                        
                        locationIcon.innerHTML = '✅';
                        locationText.innerHTML = 'Near <strong>' + userArea.name + '</strong>';
                        locationBtn.innerHTML = 'Update';
                        locationBtn.disabled = false;
                        
                        showNearbySuggestions(userArea);
                        addMessage('Great! You are near <strong>' + userArea.name + '</strong>. I can now give personalized route suggestions!', 'kiro-message', '🚕 Kiro');
                    },
                    function(err) {
                        console.error('Geolocation error:', err);
                        locationIcon.innerHTML = '❌';
                        locationText.innerHTML = 'Location denied - enter area manually';
                        locationBtn.innerHTML = 'Try Again';
                        locationBtn.disabled = false;
                    },
                    { enableHighAccuracy: true, timeout: 10000 }
                );
            } else {
                locationText.innerHTML = 'Geolocation not supported';
                locationBtn.style.display = 'none';
            }
        }

        // Event Listeners - using addEventListener for better compatibility
        sendBtn.addEventListener('click', function() {
            sendMessage();
        });

        userInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        locationBtn.addEventListener('click', function() {
            getLocation();
        });

        // Query buttons - using event delegation
        document.querySelector('.sample-queries').addEventListener('click', function(e) {
            if (e.target.classList.contains('query-btn')) {
                var query = e.target.getAttribute('data-query');
                if (query) {
                    userInput.value = query;
                    sendMessage();
                }
            }
        });

        console.log('Nagpur Commuter Guide loaded successfully!');
    </script>
</body>
</html>"""


@app.route('/')
def home():
    return HTML_TEMPLATE


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        user_area = data.get('area', None)
        
        context = load_product_context()
        enhanced_query = user_message
        if user_area:
            enhanced_query = f"[User is near {user_area}] {user_message}"
        
        response = get_kiro_response(enhanced_query, context, user_area)
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


# For Vercel serverless deployment
if __name__ == '__main__':
    app.run(debug=True)
