#!/usr/bin/env python3
"""
Simple Test Script for Nagpur Daily Commuter Guide
Tests the core Kiro response logic without Streamlit dependencies
"""

import os
import sys
from datetime import datetime

# Add the app directory to path so we can import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_product_context():
    """Load the product.md context file"""
    try:
        with open('../product.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("❌ product.md not found. Make sure you're running from the app directory.")
        return None

def get_kiro_response(user_query, context):
    """
    Simplified version of the Kiro response generator for testing
    """
    query_lower = user_query.lower()
    current_hour = datetime.now().hour

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

**Pro Move:** Work from a cafe in Sitabuldi till 7 PM, then leave when traffic clears. Most productive time = stuck time! ☕

**Jaldi chal, bhau!** ✅"""

        elif "dharampeth" in query_lower:
            return """**Dharampeth route – Good news, this is solid! ✅**

**Traffic Profile:**
- Status: Moderate, usually manageable
- Peak jam: 7-9 AM (office commute), 5-7 PM (return rush)
- Normal time: 15-20 mins to most places
- Chaos level: Yellow ⚠️ (not Red 🔥)

**Best Routes from Dharampeth:**
- To Sitabuldi: Via Warora Road (20 mins) OR Ring Road detour (25 mins, clearer)
- To South Nagpur: Direct is best, ~20 mins
- To Ramdaspeth: Via Congress Nagar, ~15 mins

**Transport Options:**
- Auto: ₹60-100 (negotiate for ₹50 if regular)
- Bus: Route 4 ideal, ₹8-12, reliable timing
- Walking: 15-minute walk to Congress Nagar bus stop = avoid crowded platforms

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
- "How to get from Dharampeth to Sitabuldi at 6 PM?"
- "What's the auto fare from Sitabuldi to Ramdaspeth?"
- "Is Wardha Road safe in monsoon?"
- "Tell me about Nagpur Metro"

Try one of these, or ask something specific about Nagpur commuting! ✅"""

def test_responses():
    """Test the core response logic with sample queries"""
    print("🧪 Testing Nagpur Daily Commuter Guide")
    print("=" * 50)

    # Load context
    context = load_product_context()
    if not context:
        return

    print("✅ product.md loaded successfully")
    print(f"📄 Context length: {len(context)} characters")
    print()

    # Test queries
    test_queries = [
        "How do I get from Dharampeth to Sitabuldi at 6 PM?",
        "What's the auto fare from Sitabuldi to Ramdaspeth?",
        "Tell me about Nagpur Metro",
        "Is it safe to travel alone at night?",
        "What's the traffic like in monsoon?",
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"🧪 Test {i}: {query}")
        print("-" * 40)
        response = get_kiro_response(query, context)
        print(response[:300] + "..." if len(response) > 300 else response)
        print()
        print("✅ Response generated successfully")
        print("=" * 50)
        print()

def interactive_test():
    """Interactive testing mode"""
    print("🎯 Interactive Testing Mode")
    print("Type 'quit' to exit")
    print("-" * 30)

    context = load_product_context()
    if not context:
        return

    while True:
        query = input("❓ Your question: ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            break

        if query:
            response = get_kiro_response(query, context)
            print("\n🚕 Kiro Response:")
            print("-" * 20)
            print(response)
            print("\n" + "=" * 50 + "\n")
        else:
            print("Please enter a question!")

if __name__ == "__main__":
    print("Nagpur Daily Commuter Guide - Test Suite")
    print("=" * 50)

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_test()
    else:
        test_responses()
        print("💡 For interactive testing, run: python test_app.py --interactive")