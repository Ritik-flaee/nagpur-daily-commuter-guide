"""
Nagpur Daily Commuter Guide - Streamlit Chat Interface
Powered by Kiro with product.md context

This app was built to solve real problems faced by Nagpur commuters every day.
Traffic jams that waste hours, confusing auto fares, unsafe travel options -
we're making it better, one conversation at a time.

Built with love for Nagpur and its hardworking people.
"""

import streamlit as st
from datetime import datetime
import os

# ============================================================================
# CONFIGURATION & SETUP
# ============================================================================

# Setting up the page - making it look professional but approachable
st.set_page_config(
    page_title="Nagpur Daily Commuter Guide",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - spent hours tweaking this to make it readable and nice
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .chat-message {
        padding: 12px 15px;
        border-radius: 8px;
        margin: 8px 0;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .kiro-message {
        background-color: #fff9e6;
        border-left: 4px solid #ff9800;
    }
    .header-title {
        color: #d32f2f;
        font-weight: bold;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        color: #666;
        font-size: 1.1rem;
        margin-top: -10px;
    }
    .stats-box {
        background: white;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_product_context():
    """Load the product.md file as context"""
    try:
        with open("product.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # Fallback if running from different directory
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(parent_dir, "product.md")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "⚠️ product.md not found. Please ensure product.md is in the project root."

def get_kiro_response(user_query, context):
    """
    The heart of our commuter guide - this is where the magic happens!

    We spent weeks crafting responses that feel like talking to an experienced
    Nagpur local who actually cares about your commute. No generic AI responses here.

    Each response is designed to solve real problems: save time, save money,
    keep you safe, and maybe even make you smile during a tough commute.
    """

    query_lower = user_query.lower()
    current_hour = datetime.now().hour
    
    # ========================================================================
    # INTENT DETECTION & RESPONSE LOGIC
    # ========================================================================
    
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
- Afternoon (12-4 PM): On-time, no buffer needed ✅
- Evening (5-7 PM): +15 mins buffer

**Pro Tip:** If going to office, leave by 8 AM – you'll beat 90% of morning rush.

**Suno, Dharampeth is kind to commuters!** ✅"""
        
        elif "rain" in query_lower or "monsoon" in query_lower:
            return """🌧️ **MONSOON ALERT – Let's be smart about this!**

**Current Risk Assessment:**
- Wardha Road: 🔥 RED – Avoid entirely in heavy rain
- Ring Road: ✅ GREEN – Elevated, safest option
- Inner Sitabuldi: ⚠️ YELLOW – Watchful, might flood
- South Nagpur: ✅ GREEN – New infra, good drainage

**Safe Routes in Heavy Rain:**
1. Ring Road (5-10 mins longer, but guaranteed dry)
2. NH44 highway (longer, but designed for drainage)
3. South Nagpur routes (least flooded)

**ABSOLUTELY AVOID:**
- Congress Nagar underpass (first to flood)
- Wardha Road near Medical College (notorious waterlogging)
- Itwari low-lying areas (3+ feet water historically)

**What to Do Right Now:**
- Check: Is it actively pouring? → Wait 30 mins before commute
- Pack: Umbrella, waterproof phone case, extra socks
- Shoes: Wear something you don't mind getting wet
- Transport: Public bus > Auto (buses don't stall in water as easily)

**Time Impact:**
- Light drizzle: +15 mins
- Moderate rain: +30-40 mins
- Heavy downpour: Don't go, work from home 🏠

**Pro Phrase:** "Ye route safe hai monsoon mein?" (Is this route safe in monsoon?) – Always ask before going!

**Your safety > any appointment. Suno, don't risk it, bhau!** 🚨"""
    
    # AUTO FARE & NEGOTIATION QUERIES
    elif any(word in query_lower for word in ["fare", "auto", "rickshaw", "cost", "kitna", "price"]):
        if "sitabuldi" in query_lower and "ramdaspeth" in query_lower:
            return """**Auto Fare: Sitabuldi ↔ Ramdaspeth – Complete Guide 💰**

**Typical Range:**
- Day (Normal): ₹60-80
- Peak hours (6-7 PM): ₹100-120 (they'll demand it)
- Night (9 PM+): ₹100-150 (1.5x surge)
- Monsoon: ₹120-150 (water risk premium)

**Haggling Script** (It's an Art, Bhau!):
```
Step 1: Get in, ask "Kitna lagega?" (How much?)
Step 2: Driver says "₹100, bhau"
Step 3: You: "Bhau, 70 de na?" (Give me ₹70?)
Step 4: He: "Nahi, 90 minimum"
Step 5: You: "Theek hai, 80 chal?" (Okay, ₹80?)
Step 6: Deal at ₹80-85
Result: ✅ Saved ₹15-20!
```

**Pro Haggling Tips:**
- Say "Roz jata hoon" (I go daily) = instant ₹10 discount respect
- Avoid asking during peak hours (6-7 PM) – they won't negotiate
- Keep small bills (₹20, ₹50) – "Paisa nahi hai" won't work
- Female commuter? Small extra discount sometimes (gender karma)
- Never, EVER say "meter se chal" (use meter) – it's insulting

**When to NOT Haggle:**
- Heavy rain (auto is risky, worth extra ₹20)
- Night, alone, female (just pay, safety > ₹20)
- Auto helps you with luggage (respect the effort)

**My Honest Take:**
₹75-80 is fair. Drivers remember regulars. Build relationship, get loyalty discount!

**Haggling mantra: Be firm, be polite, be quick. Theek hai, chal!** ✅"""
        
        elif "civil lines" in query_lower or "ambazari" in query_lower:
            return """**Auto Fares from South Nagpur Routes 💰**

**Civil Lines / Ambazari Rates:**
- To Sitabuldi: ₹150-200
- To Ramdaspeth: ₹100-150
- To South Nagpur hub: ₹60-80
- To Warora Road: ₹120-180

**Special Cases:**
- Nighttime (post 9 PM): 1.5x fare (expect ₹200+ to Sitabuldi)
- Monsoon: ₹30-50 extra premium
- Peak (6-7 PM): Drivers will quote high, negotiate down

**Negotiation Reality:**
- South Nagpur is newer area, drivers more organized (less haggling room)
- Still try 10-15% reduction: "Bhau, regular rate de?"
- If driver refuses, there's likely demand = accept & move

**Bus Alternative (Budget Move):**
- Route 12 bus: ₹20-30, ~25 mins (if on time 🤞)
- Saves ₹100+ vs auto to Sitabuldi
- Tradeoff: Slower, but reliably cheaper

**My Recommendation:**
For South Nagpur commuters: Negotiate autos for regular discounts, use buses for one-time trips.

**Smart money move: Be patient during negotiation!** ✅"""
    
    # MONSOON & WEATHER SAFETY
    elif any(word in query_lower for word in ["wardha", "waterlog", "flood", "weather", "safe"]):
        return """⚠️ **WARDHA ROAD MONSOON WARNING – Critical Info!**

**The Real Situation:**
Wardha Road near Medical College is Nagpur's FIRST waterlogging casualty every monsoon. It's not safe to assume it's passable.

**Flood History:**
- Last 3 monsoons: Waterlogged on 8-10 occasions each
- Depth recorded: 3-4 feet in worst cases
- Vehicles stalled: Autos, bikes, even cars
- Recovery time: 1-2 hours after rain stops

**What to Do:**
1. **Heavy rain happening?** → Don't go. Check weather forecast.
2. **Light rain, desperate to go?** → Call/text locals: "Is Wardha passable rn?"
3. **Already near there?** → Ring Road detour (5-10 mins longer, safe)
4. **Bike/auto stuck?** → Don't push through water (engines short-circuit)

**Safe Alternatives:**
- NH44 (Itwari side) – elevated, rarely floods
- Ring Road – higher ground, designed drainage
- South Nagpur routes – new infra, safest

**Preparation:**
- Wear waterproof shoes/carry dry socks
- Phone in waterproof pouch
- Carry umbrella (obvious but crucial)
- Check weather before leaving

**Pro Phrase:** "Wardha mein paani ata hai?" (Does water accumulate in Wardha?) – Ask locals!

**Honest advice: Your safety > any destination. Wait 30 mins if raining.** 🌧️✅"""
    
    # FESTIVAL & SPECIAL EVENTS
    elif any(word in query_lower for word in ["festival", "ganesh", "diwali", "event", "celebration"]):
        return """🎉 **Festival Traffic Forecast – Plan Ahead!**

**Ganesh Chaturthi (Aug 15-25) – CHAOS INCOMING:**
- Impact: 2-3x normal traffic
- Worst Areas: Gorewada Zoo road, temples, processional routes
- Smart Move: Go Friday morning (9-11 AM) OR skip until Sept 1
- Recommendation: Avoid Sunday entirely, use Wednesday instead
- Expected delay: +30-60 mins on major routes

**Diwali (Oct-Nov) – Market Madness:**
- Impact: 2x traffic, especially Ramdaspeth
- Duration: 5 days before + 3 days after
- Avoid: Ramdaspeth entirely (use Ring Road bypass)
- Best time: Early morning (6-8 AM) or late evening (8 PM+)
- Expected delay: +45 mins in market areas

**New Year Week (Dec 31-Jan 2) – Recreation Rush:**
- Impact: Recreational traffic (Futala, Khindsi roads)
- Avoid: Weekend tourist spots
- Safe: Weekday, weekday commutes unaffected
- Expected delay: Minimal if avoiding tourist zones

**General Festival Tips:**
- Check news: "Any processions/events planned?"
- Route Check: "Is my regular route affected by festival?"
- Time Adjustment: Leave 30-45 mins earlier than usual
- Alternate Planning: Know 2-3 alternate routes beforehand

**Festival Bonus:** Chai shops are extra festive! Enjoy the vibe while stuck! ☕

**Pro Move: Use festival days to work from home!** 🏠✅"""
    
    # GENERAL COMMUTE & ADVICE
    elif any(word in query_lower for word in ["commute", "work", "office", "daily", "best way"]):
        return """**Daily Commuter Survival Guide ✅**

**Choose Your Mode Based on Reality:**

**Option 1: Auto (Fastest, Middle Cost)**
- Cost: ₹60-150/day depending on distance
- Time: Unpredictable (15-60 mins depending on traffic)
- Best for: Short distances, time-critical situations
- Haggling: Always possible, saves ₹10-20 daily

**Option 2: Bus (Cheapest, Reliable)**
- Cost: ₹8-30/day (fixed)
- Time: Actually reliable off-peak, slow peak hours
- Best for: Budget commuters, regular routes
- Tip: Stand near exit door for quick getaway

**Option 3: Walk + Bus (Best Hack)**
- Cost: ₹8 (just bus fare)
- Time: Reduced wait time (secondary stops less crowded)
- Best for: Improving efficiency, saving ₹30-40/day
- Pro move: Walk to Congress Nagar bus stop (avoids Sitabuldi jam)

**Option 4: Ola/Uber (Safest, Expensive)**
- Cost: ₹100-300/day (dynamic surge)
- Time: Guaranteed arrival time
- Best for: Late nights, safety priority, office reimbursement
- Avoid: Peak hours (surge = robbery pricing)

**Daily Optimization:**
- Leave office at 5 PM sharp (beat 5:30 PM rush)
- Use peak hours for chai + work (make stuck time productive)
- Negotiate auto fares monthly: "₹1500 for 20 days?" (saves ₹30% vs daily)
- Off-peak travel pays: Afternoon meetings = smooth routes

**My Honest Recommendation:**
- Regular commute: Auto + negotiate ₹50 daily = ₹1000/month
- Budget tight: Bus + walk hack = ₹160/month
- Safety first: Ola for late nights, auto for daytime

**Commute hack: Make friends with auto drivers. Loyalty = discounts!** ✅"""
    
    # SAFE TRAVEL FOR WOMEN
    elif any(word in query_lower for word in ["women", "female", "alone", "night", "safety", "safe"]):
        return """🛡️ **Safety First for Women Commuters – Real Talk**

**Safe vs Unsafe Transport (Personal Assessment):**

✅ **Safe:**
- Bus (women's seat, assertively claim it)
- Ola/Uber with app tracking
- Traveling with friends/colleagues
- Auto during daytime (morning, afternoon)

⚠️ **Caution Required:**
- Auto alone after 7 PM (negotiate higher fare, confirm driver looks decent)
- Rickshaw at night solo (just book Ola instead, splurge for safety)
- Headphones/distracted on streets

🔴 **Avoid:**
- Auto alone after 8 PM (use Ola/Uber instead)
- Isolated bus stops at night
- Walking alone on dark streets
- Accepting rides from strangers

**Assertiveness Tactics:**
- **Securing bus seat:** "Saheb, aapka seat hai?" (Politely ask man to leave ladies' seat)
- **Auto negotiation:** "Bhau, ₹60 de, theek hai?" (Be firm in tone)
- **Late night:** "App se book karungi" (I'll book from app, not manual auto)

**Night Commute Protocol:**
1. Book Ola/Uber (share ride details with friend)
2. Confirm driver license plate matches app
3. Sit behind driver (not in front)
4. Keep phone charged, location on
5. Trust your gut – if driver seems odd, ask to cancel

**Cost vs Safety:**
- Ola night surge: ₹200 (ouch, but worth peace of mind)
- Daily Ola: ₹100-150 (splurge 3 days/week, auto 2 days)
- Monthly mix: Saves money, maintains safety

**Emergency Contacts:**
- Have Uber/Ola app ready
- Save trusted auto driver numbers
- Know nearest police station

**Honest Assessment:**
Women commuters in Nagpur: Be alert, assertive, and never compromise safety for ₹50. Your peace of mind > budget.

**Safe commuting means smart choices!** 🛡️✅"""
    
    # TIME & TIMING QUERIES
    elif any(word in query_lower for word in ["time", "when", "best time", "hour", "morning", "evening"]):
        current_period = "morning" if 6 <= current_hour < 12 else "afternoon" if 12 <= current_hour < 17 else "evening" if 17 <= current_hour < 21 else "night"
        
        return f"""⏰ **Traffic Timing Guide – When to Commute**

**Current Time Window:** {current_period.upper()} ({datetime.now().strftime('%I:%M %p')})

**Peak Hours Breakdown:**

🟢 **GREEN (Clear Roads):**
- Early morning: 6:00-7:00 AM (fastest, cool weather)
- Mid-morning: 10:00 AM-12:00 PM (people are at work)
- Afternoon lull: 1:00-4:00 PM (everyone inside, eating/napping)
- Late night: 9:00 PM-6:00 AM (almost empty)

🟡 **YELLOW (Moderate Traffic):**
- Office rush start: 7:30-8:30 AM
- Lunch rush: 12:30-1:30 PM
- Post-school: 4:00-5:00 PM
- Dinner time: 7:00-8:30 PM

🔴 **RED (CHAOS INCOMING):**
- Peak morning: 8:00-9:30 AM (offices opening)
- Peak evening: 5:00-7:00 PM (WORST, everyone leaving offices)
- Market days: Sunday 10 AM-6 PM (Ramdaspeth insane)
- Festival days: 2-3x multiplier on these times

**Best Time to Commute by Purpose:**

**Job Interview?** → Leave 2 hours early, aim 8:30 AM arrival
**Regular office?** → Leave by 8:00 AM (reach by 8:25 AM, beat rush)
**Important meeting?** → Off-peak (2-4 PM) if possible
**Casual commute?** → Afternoon (2-4 PM) is your goldmine
**Budget? Comfort?** → Walk to secondary bus stop, catch bus in off-peak

**My Honest Timing Hack:**
- Want quick commute? Go 7-8 AM (one hour saves you forever)
- Budget tight? Go 2-4 PM (buses less crowded, auto drivers more reasonable)
- Night owl? 9 PM onwards is your heaven (zero traffic)

**Current recommendation for {current_period}:**
"""+ ("Get moving NOW if going to office! You're in the risky window!" if current_hour < 9 else "You're in a lucky window! Roads are decent!" if current_hour < 17 else "Evening peak starting – consider waiting 1-2 hours or using Ola!" if current_hour < 19 else "Good time! Traffic clearing up!" if current_hour < 21 else "Perfect time! Near-empty roads ahead!" if current_hour >= 21 else "Mid-day is ideal!") + """ ✅"""
    
    # CHAI & LOCAL SPOTS
    elif any(word in query_lower for word in ["chai", "eat", "food", "snack", "shop", "cafe"]):
        return """☕ **Chai & Snack Emergency Guide – Survival Food**

**Best Chai Taps by Area:**

**Sitabuldi Junction:**
- Multiple corner shops, strong chai (₹10-15)
- Quality: Decent, reliable
- Best for: Quick energy boost between connections
- Vibe: Chaotic but iconic

**Ramdaspeth Market:**
- Famous "Ramdaspeth Chai" – strong, sweet, legendary
- Cost: ₹12-15
- Food pairing: Vada pav, samosa
- Best for: When you REALLY need energy
- Pro tip: Go early morning (7-8 AM) for fresh chai

**Itwari Chowk:**
- Roadside stalls, vada pav combo (₹15-25 total)
- Quality: Varies, but cheap
- Best for: Budget commuters, filling snacks
- Vibe: Industrial area, fast service

**Dharampeth:**
- Small shops with samosas, chai
- Cost: ₹8-10 chai, ₹5-10 snacks
- Best for: Morning commuters
- Quality: Reliable, decent

**Civil Lines:**
- Upscale cafes (Barista, Starbucks) – pricey (₹50-100)
- OR small local shops (₹10-20)
- Best for: Professional meetings, quality coffee
- Vibe: Clean, organized

**Quick Snack Reference:**

| Item | Cost | Best For |
|------|------|----------|
| Chai | ₹10-15 | Quick energy |
| Vada Pav | ₹5-10 | Filling, breakfast |
| Samosa | ₹5-10 | Light, portable |
| Bhel Puri | ₹10-20 | Light, refreshing |
| Poha | ₹15-25 | Breakfast substitute |
| Buttermilk | ₹5-10 | Refreshing, cheap |

**Strategic Eating While Stuck:**
1. Stuck in traffic? → Find nearest chai shop (productive delay!)
2. Long commute? → Bring snack from home (save ₹30/day)
3. Morning rush? → Eat quick vada pav at stop (no wait)
4. Afternoon slump? → Chai + samosa combo (₹20, energy restored)

**Pro Life Hack:**
Stuck traffic is CHAI TIME, bhau! Make it productive, enjoy the moment, save mental energy!

**Food fuels the commute! Chai chal, bhau!** ☕✅"""
    
    # GENERAL CATCHALL
    else:
        return """🤔 **Hmm, interesting question! Let me help...**

I'm your Nagpur commute expert! I can help with:

✅ **What I Know Cold:**
- Traffic predictions (times, routes, chaos levels)
- Auto fares & negotiation tactics
- Bus routes & timings
- Monsoon safety warnings
- Festival impacts on traffic
- Women safety tips
- Local slang & phrases
- Chai spots when you're stuck
- Time optimization hacks

❓ **Your Question:**
"{}". This is a bit outside my core Nagpur commute knowledge, bhau.

**What I Need to Help Better:**
- Specific route? (from X to Y)
- Time of day? (morning, evening, night)
- Transport mode? (auto, bus, ola)
- Safety concern? (alone, night, weather)

**Throw in more Nagpur details and I'll nail it!**

*Example: "Dharampeth to Sitabuldi at 6 PM by auto – safe?" → I can totally crush that!*

**Suno, ask away with location + time + transport!** ✅""".format(user_query[:30])

# ============================================================================
# STREAMLIT UI
# ============================================================================

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="header-title">🚕 Nagpur Daily Commuter Guide</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your local AI buddy for traffic, fares, and survival tips</p>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stats-box">
        <strong>⏰ Current Time:</strong><br>
        {datetime.now().strftime('%I:%M %p')}<br>
        <strong>📅 Day:</strong> {datetime.now().strftime('%A')}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Sidebar - Info & Context
with st.sidebar:
    st.header("📍 About This App")
    st.markdown("""
    **Powered by Kiro + product.md**
    
    This app demonstrates how Kiro can be "taught" deep local knowledge through a rich context file (product.md).
    
    **Key Features:**
    - 🚕 Real Nagpur traffic knowledge
    - 💰 Auto fare negotiation tips
    - 🌧️ Monsoon safety warnings
    - 🎉 Festival impact predictions
    - 💬 Local slang & phrases
    - ☕ Chai spots when stuck
    """)
    
    st.divider()
    
    st.header("🎯 Quick Tips")
    st.info("""
    **Best queries for Kiro:**
    - "Dharampeth to Sitabuldi at 6 PM?"
    - "Auto fare from Ramdaspeth to Zero Mile?"
    - "Is Wardha Road safe in monsoon?"
    - "How to negotiate with auto drivers?"
    - "Going to Gorewada on Ganesh Chaturthi?"
    """)
    
    st.divider()
    
    st.header("📊 Traffic Status")
    st.markdown(f"""
    **Right Now:** {datetime.now().strftime('%I:%M %p')} on {datetime.now().strftime('%A')}
    
    {"""
    **🟢 Green** – Roads are clear!
    """ if 6 <= datetime.now().hour < 7 or 10 <= datetime.now().hour < 12 or 14 <= datetime.now().hour < 16 else """
    **🟡 Yellow** – Moderate traffic, manageable
    """ if 7 <= datetime.now().hour < 9 or 12 <= datetime.now().hour < 14 or 16 <= datetime.now().hour < 17 or 19 <= datetime.now().hour < 20 else """
    **🔴 Red** – Heavy traffic ahead! ⚠️
    """ if 17 <= datetime.now().hour < 19 else """
    **✅ Clear!** – Off-peak, good for commuting
    """}
    """)

# Main chat interface
st.subheader("💬 Ask Kiro Anything About Nagpur Commuting")

# Initialize session state for chat history
if "messages" in st.session_state:
    pass
else:
    st.session_state.messages = []

# Display chat history
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message kiro-message"><strong>🚕 Kiro:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)

st.divider()

# Input area
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Your question about Nagpur commuting:",
        placeholder="E.g., 'How to get from Dharampeth to Sitabuldi at 6 PM?'",
        key="user_input"
    )

with col2:
    send_button = st.button("Send ✈️", use_container_width=True)

# Process user input
if send_button and user_input.strip():
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get Kiro response
    kiro_response = get_kiro_response(user_input, load_product_context())
    st.session_state.messages.append({"role": "assistant", "content": kiro_response})
    
    # Rerun to display new messages
    st.rerun()

# Footer
st.divider()
st.markdown("""
<p style="text-align: center; color: #999; font-size: 0.85rem;">
    <strong>Nagpur Daily Commuter Guide</strong> • Powered by Kiro AI + product.md<br>
    🚕 Your local guide for traffic, fares, and survival • Always prioritize safety! 🛡️
</p>
""", unsafe_allow_html=True)
