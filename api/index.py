from flask import Flask, request, jsonify, Response
import os
import json
from datetime import datetime

app = Flask(__name__)

def load_product_context():
    try:
        paths_to_try = ['product.md', '../product.md', os.path.join(os.path.dirname(__file__), '..', 'product.md')]
        for path in paths_to_try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
        return "Knowledge base loaded."
    except Exception as e:
        return f"Error: {str(e)}"

# Interactive response generator - returns structured JSON for rich UI
def get_kiro_response(user_query, context, user_area=None):
    query_lower = user_query.lower()
    
    # TRAFFIC & ROUTE QUERIES
    if any(word in query_lower for word in ["sitabuldi", "traffic", "jam", "route", "how to get", "commute"]):
        if "sitabuldi" in query_lower and ("6" in query_lower or "evening" in query_lower or "5" in query_lower):
            return {
                "type": "traffic",
                "title": "🔥 Sitabuldi Evening Traffic",
                "subtitle": "Bhau, you're braver than me!",
                "location": user_area,
                "severity": "high",
                "cards": [
                    {"icon": "⏱️", "title": "Time Estimate", "items": [
                        {"label": "Normal", "value": "20-25 mins", "status": "good"},
                        {"label": "Peak (5-7 PM)", "value": "45-90 mins", "status": "bad"},
                        {"label": "Root cause", "value": "Office rush + bus convergence", "status": "info"}
                    ]},
                    {"icon": "🚀", "title": "Escape Plans", "items": [
                        {"label": "Plan A (Best)", "value": "Leave at 5 PM sharp", "status": "good"},
                        {"label": "Plan B (Smart)", "value": "Route 1 bus - ₹8", "status": "info"},
                        {"label": "Plan C (Rich)", "value": "Ola/Uber ₹70-100", "status": "warning"}
                    ]},
                    {"icon": "☕", "title": "If Already Stuck", "items": [
                        {"label": "Chai spot", "value": "Near Sitabuldi railway station - ₹10", "status": "info"},
                        {"label": "Wait time", "value": "Traffic clears by 7 PM", "status": "info"},
                        {"label": "Pro tip", "value": "Work from cafe till 7 PM", "status": "good"}
                    ]}
                ],
                "quickActions": [
                    {"text": "🚇 Check Metro", "query": "metro from sitabuldi"},
                    {"text": "💰 Auto Fare", "query": "auto fare sitabuldi"},
                    {"text": "🛡️ Safety Tips", "query": "night safety"}
                ]
            }
        elif "dharampeth" in query_lower:
            return {
                "type": "traffic",
                "title": "✅ Dharampeth Route",
                "subtitle": "Good news - this area is solid!",
                "location": user_area,
                "severity": "medium",
                "cards": [
                    {"icon": "🚦", "title": "Traffic Profile", "items": [
                        {"label": "Status", "value": "Moderate", "status": "warning"},
                        {"label": "Peak jam", "value": "7-9 AM, 5-7 PM", "status": "warning"},
                        {"label": "Normal time", "value": "15-20 mins", "status": "good"}
                    ]},
                    {"icon": "🗺️", "title": "Best Routes", "items": [
                        {"label": "To Sitabuldi", "value": "Via Warora Road (20 mins)", "status": "good"},
                        {"label": "Alternate", "value": "Ring Road (25 mins, clearer)", "status": "info"},
                        {"label": "To Ramdaspeth", "value": "Via Congress Nagar (15 mins)", "status": "good"}
                    ]},
                    {"icon": "🚕", "title": "Transport Options", "items": [
                        {"label": "Auto", "value": "₹60-100 (negotiate ₹50)", "status": "info"},
                        {"label": "Bus", "value": "Route 4 - ₹8-12", "status": "good"},
                        {"label": "Walk", "value": "15 min to Congress Nagar stop", "status": "info"}
                    ]}
                ],
                "quickActions": [
                    {"text": "🚇 Metro Options", "query": "metro"},
                    {"text": "💰 Fare Guide", "query": "auto fare dharampeth"}
                ]
            }
        else:
            return {
                "type": "traffic",
                "title": "🚗 Nagpur Traffic Update",
                "subtitle": "Current city-wide status",
                "location": user_area,
                "severity": "medium",
                "cards": [
                    {"icon": "🔴", "title": "Hot Spots", "items": [
                        {"label": "Sitabuldi Junction", "value": "Heavy", "status": "bad"},
                        {"label": "Ramdaspeth", "value": "Moderate", "status": "warning"},
                        {"label": "Itwari", "value": "Heavy", "status": "bad"}
                    ]},
                    {"icon": "🟢", "title": "Clear Routes", "items": [
                        {"label": "Wardha Road", "value": "Clear", "status": "good"},
                        {"label": "Ring Road", "value": "Smooth", "status": "good"},
                        {"label": "South Nagpur", "value": "Light", "status": "good"}
                    ]},
                    {"icon": "💡", "title": "Pro Tips", "items": [
                        {"label": "Avoid", "value": "Sitabuldi 5-7 PM", "status": "warning"},
                        {"label": "Use", "value": "Ring Road for long distances", "status": "good"},
                        {"label": "Best", "value": "Metro for Airport ↔ City", "status": "good"}
                    ]}
                ],
                "quickActions": [
                    {"text": "🚇 Metro Info", "query": "metro"},
                    {"text": "🔍 Specific Route", "query": "dharampeth to sitabuldi"}
                ]
            }

    # METRO QUERIES
    if any(word in query_lower for word in ["metro", "subway", "underground"]):
        return {
            "type": "metro",
            "title": "🚇 Nagpur Metro",
            "subtitle": "Running since 2019 - The Game Changer!",
            "location": user_area,
            "severity": "info",
            "cards": [
                {"icon": "🔵", "title": "Aqua Line", "items": [
                    {"label": "Route", "value": "Sitabuldi ↔ Airport", "status": "info"},
                    {"label": "Stations", "value": "15 stations, 13.8 km", "status": "info"},
                    {"label": "Time saved", "value": "25 mins vs 90 mins by road!", "status": "good"}
                ]},
                {"icon": "🟠", "title": "Orange Line", "items": [
                    {"label": "Route", "value": "Khapri ↔ Automotive Square", "status": "info"},
                    {"label": "Stations", "value": "11 stations, 9.6 km", "status": "info"},
                    {"label": "Best for", "value": "Industrial areas", "status": "info"}
                ]},
                {"icon": "💰", "title": "Fares & Tips", "items": [
                    {"label": "Smart Card", "value": "₹50 (saves ₹2/trip)", "status": "good"},
                    {"label": "Frequency", "value": "Every 3-5 mins peak", "status": "good"},
                    {"label": "Hours", "value": "6 AM - 11 PM daily", "status": "info"}
                ]},
                {"icon": "🌍", "title": "Impact on Nagpur", "items": [
                    {"label": "Traffic", "value": "30% less autos on roads", "status": "good"},
                    {"label": "Environment", "value": "50,000+ cars off daily", "status": "good"},
                    {"label": "Safety", "value": "Women-only coaches available", "status": "good"}
                ]}
            ],
            "quickActions": [
                {"text": "🚗 Traffic Update", "query": "traffic"},
                {"text": "💰 Auto Fares", "query": "auto fare"},
                {"text": "🛡️ Safety", "query": "safety tips"}
            ]
        }

    # FARE QUERIES
    if any(word in query_lower for word in ["fare", "cost", "price", "kitna lagega", "auto"]):
        return {
            "type": "fare",
            "title": "💰 Auto Fare Guide",
            "subtitle": "Know before you go, bhau!",
            "location": user_area,
            "severity": "info",
            "cards": [
                {"icon": "📍", "title": "Zone 1 (Central)", "items": [
                    {"label": "Sitabuldi/Ramdaspeth", "value": "₹30-50", "status": "good"},
                    {"label": "Short hop", "value": "₹40-60", "status": "good"},
                    {"label": "No meter", "value": "Negotiate always!", "status": "warning"}
                ]},
                {"icon": "🏙️", "title": "Zone 2 (Mid-Distance)", "items": [
                    {"label": "Dharampeth→Civil Lines", "value": "₹80-120", "status": "info"},
                    {"label": "Ramdaspeth→Ambazari", "value": "₹100-150", "status": "info"},
                    {"label": "Sitabuldi→South", "value": "₹120-180", "status": "info"}
                ]},
                {"icon": "🛣️", "title": "Zone 3 (Long Distance)", "items": [
                    {"label": "Zero Mile→Gorewada", "value": "₹150-250", "status": "warning"},
                    {"label": "Sitabuldi→Wardha Rd", "value": "₹200-300", "status": "warning"},
                    {"label": "Night (9PM+)", "value": "1.5x fare", "status": "bad"}
                ]},
                {"icon": "🗣️", "title": "Haggling Script", "items": [
                    {"label": "Step 1", "value": "\"Kitna lagega bhau?\"", "status": "info"},
                    {"label": "Step 2", "value": "Counter at 60-70% of quote", "status": "info"},
                    {"label": "Step 3", "value": "\"Theek hai, chal!\"", "status": "good"}
                ]}
            ],
            "quickActions": [
                {"text": "🚇 Try Metro", "query": "metro"},
                {"text": "🚌 Bus Routes", "query": "bus"},
                {"text": "🚗 Traffic", "query": "traffic"}
            ]
        }

    # SAFETY QUERIES
    if any(word in query_lower for word in ["safe", "safety", "alone", "night", "woman", "female"]):
        return {
            "type": "safety",
            "title": "🛡️ Safety Guide",
            "subtitle": "Your security matters most!",
            "location": user_area,
            "severity": "warning",
            "cards": [
                {"icon": "👩", "title": "For Women/Evening", "items": [
                    {"label": "Best option", "value": "Ola/Uber (tracked)", "status": "good"},
                    {"label": "Metro", "value": "Women-only coaches", "status": "good"},
                    {"label": "Avoid", "value": "Sharing autos at night", "status": "bad"}
                ]},
                {"icon": "📋", "title": "General Rules", "items": [
                    {"label": "Fare", "value": "Confirm BEFORE entering", "status": "warning"},
                    {"label": "Phone", "value": "Keep charged, share location", "status": "info"},
                    {"label": "Trust", "value": "Your instincts!", "status": "good"}
                ]},
                {"icon": "📞", "title": "Emergency Numbers", "items": [
                    {"label": "Police", "value": "100", "status": "bad"},
                    {"label": "Women Helpline", "value": "181", "status": "bad"},
                    {"label": "Ambulance", "value": "108", "status": "bad"}
                ]}
            ],
            "quickActions": [
                {"text": "🚇 Safe Metro", "query": "metro"},
                {"text": "🚗 Traffic Now", "query": "traffic"},
                {"text": "💰 Fare Guide", "query": "auto fare"}
            ]
        }

    # MONSOON QUERIES
    if any(word in query_lower for word in ["rain", "monsoon", "flood", "waterlog"]):
        return {
            "type": "monsoon",
            "title": "🌧️ Monsoon Guide",
            "subtitle": "Stay safe & dry!",
            "location": user_area,
            "severity": "warning",
            "cards": [
                {"icon": "⚠️", "title": "Danger Zones", "items": [
                    {"label": "Wardha Road", "value": "Floods first!", "status": "bad"},
                    {"label": "Itwari", "value": "Low-lying areas", "status": "bad"},
                    {"label": "Zero Mile", "value": "Underpass floods", "status": "bad"}
                ]},
                {"icon": "✅", "title": "Safe Routes", "items": [
                    {"label": "Ring Road", "value": "Elevated, good drainage", "status": "good"},
                    {"label": "NH44", "value": "Highway standard", "status": "good"},
                    {"label": "Metro", "value": "Obviously!", "status": "good"}
                ]},
                {"icon": "💡", "title": "Survival Tips", "items": [
                    {"label": "Buffer", "value": "Add 30-40 mins", "status": "warning"},
                    {"label": "If stuck", "value": "Find chai shop, wait", "status": "info"},
                    {"label": "Never", "value": "Cross flooded roads!", "status": "bad"}
                ]}
            ],
            "quickActions": [
                {"text": "🚇 Metro (Safe)", "query": "metro"},
                {"text": "🚗 Traffic", "query": "traffic"},
                {"text": "🛡️ Safety", "query": "safety"}
            ]
        }

    # DEFAULT RESPONSE
    return {
        "type": "welcome",
        "title": "🚕 Nagpur Commuter Guide",
        "subtitle": "Your local travel buddy!",
        "location": user_area,
        "severity": "info",
        "cards": [
            {"icon": "🎯", "title": "I Can Help With", "items": [
                {"label": "Traffic", "value": "Real-time route advice", "status": "info"},
                {"label": "Auto Fares", "value": "Zone-wise pricing", "status": "info"},
                {"label": "Metro", "value": "Lines, timings, fares", "status": "info"},
                {"label": "Safety", "value": "Night travel tips", "status": "info"}
            ]}
        ],
        "quickActions": [
            {"text": "🚗 Traffic Update", "query": "traffic update sitabuldi"},
            {"text": "💰 Auto Fares", "query": "auto fare guide"},
            {"text": "🚇 Metro Info", "query": "tell me about metro"},
            {"text": "🛡️ Safety Tips", "query": "night safety tips"},
            {"text": "🌧️ Monsoon Guide", "query": "monsoon travel tips"}
        ]
    }


# Interactive HTML template
HTML_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚕 Nagpur Commuter Guide</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #fff;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            padding: 20px 0;
            margin-bottom: 20px;
        }
        header h1 {
            font-size: 2.5em;
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        header p {
            color: #a0a0a0;
            margin-top: 5px;
        }
        .location-bar {
            background: linear-gradient(135deg, #00b894, #00cec9);
            padding: 12px 20px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .location-bar button {
            background: rgba(255,255,255,0.2);
            border: 2px solid white;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .location-bar button:hover {
            background: white;
            color: #00b894;
        }
        .chat-area {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 20px;
            min-height: 400px;
            max-height: 600px;
            overflow-y: auto;
        }
        .message {
            margin-bottom: 20px;
            animation: fadeIn 0.3s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user-msg {
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 12px 18px;
            border-radius: 18px 18px 4px 18px;
            margin-left: 20%;
            display: inline-block;
            max-width: 80%;
            float: right;
            clear: both;
        }
        .bot-msg {
            clear: both;
            padding-top: 10px;
        }
        .response-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
        }
        .response-header .icon {
            font-size: 2em;
        }
        .response-header h2 {
            font-size: 1.4em;
            color: #feca57;
        }
        .response-header p {
            color: #a0a0a0;
            font-size: 0.9em;
        }
        .severity-high { border-left: 4px solid #ff6b6b; padding-left: 15px; }
        .severity-medium { border-left: 4px solid #feca57; padding-left: 15px; }
        .severity-info { border-left: 4px solid #54a0ff; padding-left: 15px; }
        .severity-warning { border-left: 4px solid #ff9f43; padding-left: 15px; }
        
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }
        .card {
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }
        .card-header {
            background: rgba(255,255,255,0.1);
            padding: 12px 15px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
        }
        .card-header .card-icon {
            font-size: 1.3em;
        }
        .card-content {
            padding: 12px 15px;
        }
        .card-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            align-items: center;
        }
        .card-item:last-child {
            border-bottom: none;
        }
        .card-item .label {
            color: #a0a0a0;
            font-size: 0.9em;
        }
        .card-item .value {
            font-weight: 500;
            text-align: right;
            max-width: 60%;
        }
        .status-good { color: #00b894; }
        .status-warning { color: #feca57; }
        .status-bad { color: #ff6b6b; }
        .status-info { color: #54a0ff; }
        
        .quick-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        .quick-action {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border: none;
            color: white;
            padding: 10px 18px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 0.9em;
            transition: all 0.3s;
            font-weight: 500;
        }
        .quick-action:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        
        .input-area {
            display: flex;
            gap: 10px;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 16px;
        }
        #user-input {
            flex: 1;
            background: rgba(255,255,255,0.1);
            border: 2px solid rgba(255,255,255,0.2);
            border-radius: 12px;
            padding: 15px;
            color: white;
            font-size: 16px;
            outline: none;
        }
        #user-input::placeholder {
            color: rgba(255,255,255,0.5);
        }
        #user-input:focus {
            border-color: #667eea;
        }
        #send-btn {
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            border: none;
            color: white;
            padding: 15px 30px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
        }
        #send-btn:hover {
            transform: scale(1.05);
        }
        #send-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        
        .sample-queries {
            margin-top: 20px;
            text-align: center;
        }
        .sample-queries h3 {
            color: #a0a0a0;
            font-size: 0.9em;
            margin-bottom: 10px;
        }
        .sample-btn {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            padding: 8px 15px;
            margin: 5px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.85em;
            transition: all 0.3s;
        }
        .sample-btn:hover {
            background: rgba(255,255,255,0.2);
            border-color: #667eea;
        }
        
        .welcome-msg {
            text-align: center;
            padding: 40px;
            color: #a0a0a0;
        }
        .welcome-msg h2 {
            color: #feca57;
            margin-bottom: 10px;
        }
        
        @media (max-width: 600px) {
            header h1 { font-size: 1.8em; }
            .cards-grid { grid-template-columns: 1fr; }
            .user-msg { margin-left: 10%; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚕 Nagpur Commuter Guide</h1>
            <p>AI-powered local travel assistant | Powered by Kiro</p>
        </header>

        <div class="location-bar">
            <div>
                <span id="loc-icon">📍</span>
                <span id="loc-text">Enable location for personalized tips</span>
            </div>
            <button id="loc-btn">Enable Location</button>
        </div>

        <div class="chat-area" id="chat-area">
            <div class="welcome-msg">
                <h2>Namaste! 🙏</h2>
                <p>Ask me about Nagpur traffic, auto fares, metro, or safety tips.</p>
                <p style="margin-top:10px;">Try clicking one of the buttons below!</p>
            </div>
        </div>

        <div class="input-area">
            <input type="text" id="user-input" placeholder="Ask about traffic, fares, metro, safety...">
            <button id="send-btn">Send 🚀</button>
        </div>

        <div class="sample-queries">
            <h3>💡 Quick queries:</h3>
            <button class="sample-btn">🚗 Sitabuldi Traffic</button>
            <button class="sample-btn">💰 Auto Fares</button>
            <button class="sample-btn">🚇 Metro Info</button>
            <button class="sample-btn">🛡️ Night Safety</button>
            <button class="sample-btn">🌧️ Monsoon Tips</button>
        </div>
    </div>

    <script>
        (function() {
            var userArea = null;
            var chatArea = document.getElementById('chat-area');
            var userInput = document.getElementById('user-input');
            var sendBtn = document.getElementById('send-btn');
            var firstMessage = true;

            var sampleQueries = {
                '🚗 Sitabuldi Traffic': 'How is traffic at Sitabuldi at 6 PM?',
                '💰 Auto Fares': 'What is the auto fare guide?',
                '🚇 Metro Info': 'Tell me about Nagpur Metro',
                '🛡️ Night Safety': 'Is it safe to travel alone at night?',
                '🌧️ Monsoon Tips': 'Monsoon travel tips'
            };

            var nagpurAreas = [
                { name: 'Sitabuldi', lat: 21.1458, lng: 79.0882 },
                { name: 'Dharampeth', lat: 21.1395, lng: 79.0756 },
                { name: 'Ramdaspeth', lat: 21.1377, lng: 79.0919 },
                { name: 'Civil Lines', lat: 21.1591, lng: 79.0765 },
                { name: 'Wardha Road', lat: 21.1167, lng: 79.1083 }
            ];

            function findNearestArea(lat, lng) {
                var nearest = nagpurAreas[0];
                var minDist = Infinity;
                for (var i = 0; i < nagpurAreas.length; i++) {
                    var d = Math.sqrt(Math.pow(lat - nagpurAreas[i].lat, 2) + Math.pow(lng - nagpurAreas[i].lng, 2));
                    if (d < minDist) { minDist = d; nearest = nagpurAreas[i]; }
                }
                return nearest.name;
            }

            function renderResponse(data) {
                var html = '<div class="bot-msg">';
                html += '<div class="response-header severity-' + data.severity + '">';
                html += '<div><h2>' + data.title + '</h2>';
                html += '<p>' + data.subtitle + '</p>';
                if (data.location) html += '<p style="color:#00b894;">📍 Near ' + data.location + '</p>';
                html += '</div></div>';

                html += '<div class="cards-grid">';
                for (var i = 0; i < data.cards.length; i++) {
                    var card = data.cards[i];
                    html += '<div class="card">';
                    html += '<div class="card-header"><span class="card-icon">' + card.icon + '</span>' + card.title + '</div>';
                    html += '<div class="card-content">';
                    for (var j = 0; j < card.items.length; j++) {
                        var item = card.items[j];
                        html += '<div class="card-item">';
                        html += '<span class="label">' + item.label + '</span>';
                        html += '<span class="value status-' + item.status + '">' + item.value + '</span>';
                        html += '</div>';
                    }
                    html += '</div></div>';
                }
                html += '</div>';

                if (data.quickActions && data.quickActions.length > 0) {
                    html += '<div class="quick-actions">';
                    for (var k = 0; k < data.quickActions.length; k++) {
                        var action = data.quickActions[k];
                        html += '<button class="quick-action" data-query="' + action.query + '">' + action.text + '</button>';
                    }
                    html += '</div>';
                }
                html += '</div>';
                return html;
            }

            function addUserMessage(text) {
                if (firstMessage) {
                    chatArea.innerHTML = '';
                    firstMessage = false;
                }
                var div = document.createElement('div');
                div.className = 'message';
                div.innerHTML = '<div class="user-msg">' + text + '</div>';
                chatArea.appendChild(div);
                chatArea.scrollTop = chatArea.scrollHeight;
            }

            function addBotMessage(data) {
                var div = document.createElement('div');
                div.className = 'message';
                div.innerHTML = renderResponse(data);
                chatArea.appendChild(div);
                chatArea.scrollTop = chatArea.scrollHeight;

                // Attach quick action handlers
                var btns = div.querySelectorAll('.quick-action');
                for (var i = 0; i < btns.length; i++) {
                    btns[i].onclick = function() {
                        userInput.value = this.getAttribute('data-query');
                        sendMessage();
                    };
                }
            }

            function sendMessage() {
                var msg = userInput.value.trim();
                if (!msg) return;

                sendBtn.disabled = true;
                sendBtn.textContent = '...';
                addUserMessage(msg);
                userInput.value = '';

                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/api/chat', true);
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.onreadystatechange = function() {
                    if (xhr.readyState === 4) {
                        sendBtn.disabled = false;
                        sendBtn.textContent = 'Send 🚀';
                        if (xhr.status === 200) {
                            try {
                                var resp = JSON.parse(xhr.responseText);
                                addBotMessage(resp.response);
                            } catch(e) {
                                console.error(e);
                            }
                        }
                    }
                };
                xhr.send(JSON.stringify({ message: msg, area: userArea }));
            }

            // Event listeners
            sendBtn.onclick = sendMessage;
            userInput.onkeypress = function(e) {
                if (e.key === 'Enter') sendMessage();
            };

            document.getElementById('loc-btn').onclick = function() {
                var btn = this;
                btn.textContent = 'Detecting...';
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(pos) {
                        userArea = findNearestArea(pos.coords.latitude, pos.coords.longitude);
                        document.getElementById('loc-icon').textContent = '✅';
                        document.getElementById('loc-text').innerHTML = 'Near <strong>' + userArea + '</strong>';
                        btn.textContent = 'Update';
                    }, function() {
                        document.getElementById('loc-icon').textContent = '❌';
                        document.getElementById('loc-text').textContent = 'Location denied';
                        btn.textContent = 'Try Again';
                    });
                }
            };

            var sampleBtns = document.querySelectorAll('.sample-btn');
            for (var i = 0; i < sampleBtns.length; i++) {
                sampleBtns[i].onclick = function() {
                    var query = sampleQueries[this.textContent];
                    if (query) {
                        userInput.value = query;
                        sendMessage();
                    }
                };
            }
        })();
    </script>
</body>
</html>'''


@app.route('/')
def home():
    return Response(HTML_PAGE, mimetype='text/html')


@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        resp = Response()
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return resp
    
    try:
        data = request.get_json() or {}
        user_message = data.get('message', '')
        user_area = data.get('area', None)
        
        context = load_product_context()
        response_data = get_kiro_response(user_message, context, user_area)
        
        resp = jsonify({'response': response_data})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        resp = jsonify({'error': str(e)})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp, 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
