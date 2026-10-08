import streamlit as st
from datetime import datetime, time, date
import json
import requests
import random
import math

st.set_page_config(
    page_title="Bharath Pro Apps - 3 Professional Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== MASTER HIGH GRAPHICS PROFESSIONAL CSS =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;700&family=Outfit:wght@300;400;600;700;900&family=Space+Grotesk:wght@400;700&display=swap');

.stApp {
    background: radial-gradient(ellipse at top left, #0f172a 0%, #1e1b4b 25%, #020617 100%);
    color: white;
    font-family: 'Outfit', 'Noto Sans Kannada', sans-serif;
}

.glass-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.15), inset 0 -1px 0 rgba(0,0,0,0.2);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.6s;
}
.glass-card:hover::before {
    left: 100%;
}
.glass-card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 0 1px rgba(251,191,36,0.25), inset 0 1px 0 rgba(255,255,255,0.2);
    border-color: rgba(251,191,36,0.35);
}

.meter-display {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 50%, #020617 100%);
    border: 2px solid;
    border-image: linear-gradient(135deg, #fbbf24, #f59e0b, #ef4444) 1;
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 0 50px rgba(251,191,36,0.25), inset 0 2px 0 rgba(255,255,255,0.1), inset 0 -2px 10px rgba(0,0,0,0.5);
    position: relative;
}

.fare-amount {
    font-size: 4rem;
    font-weight: 900;
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 25%, #ef4444 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 40px rgba(251,191,36,0.6);
    letter-spacing: -0.03em;
    font-family: 'Space Grotesk', monospace;
    line-height: 1;
}

.kannada-text {
    font-family: 'Noto Sans Kannada', sans-serif;
}

.pulse-gold {
    animation: pulseGold 2.5s infinite;
}
@keyframes pulseGold {
    0% { box-shadow: 0 0 0 0 rgba(251,191,36,0.7), 0 0 50px rgba(251,191,36,0.3); }
    50% { box-shadow: 0 0 0 18px rgba(251,191,36,0), 0 0 60px rgba(251,191,36,0.4); }
    100% { box-shadow: 0 0 0 0 rgba(251,191,36,0), 0 0 50px rgba(251,191,36,0.3); }
}

.shimmer {
    position: relative;
    overflow: hidden;
}
.shimmer::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    animation: shimmerMove 3s infinite;
}
@keyframes shimmerMove {
    0% { left: -100%; }
    100% { left: 100%; }
}

.product-card {
    background: linear-gradient(135deg, rgba(34,197,94,0.15) 0%, rgba(16,185,129,0.08) 100%);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 20px;
    padding: 18px;
    transition: all 0.3s ease;
}
.product-card:hover {
    background: linear-gradient(135deg, rgba(34,197,94,0.25) 0%, rgba(16,185,129,0.15) 100%);
    transform: scale(1.02);
    border-color: rgba(34,197,94,0.5);
}

.token-queue {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 12px 0;
}
.token-item {
    min-width: 70px;
    height: 70px;
    background: linear-gradient(135deg, #334155, #1e293b);
    border: 2px solid #475569;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1.2rem;
    transition: all 0.3s;
}
.token-item.active {
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: black;
    border-color: #fbbf24;
    box-shadow: 0 0 20px rgba(251,191,36,0.6);
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# Language
lang = st.sidebar.selectbox("Language / ಭಾಷೆ", ["ಕನ್ನಡ", "English", "Kanglish"], key="lang")
def t(en, kn): 
    if lang=="ಕನ್ನಡ": return kn
    elif lang=="Kanglish": return f"{kn} / {en}"
    return en

# ===== AQ API SYSTEM - MODEL 3.8 COMPATIBLE + VERCEL =====
st.sidebar.markdown("## 🚀 Bharath Pro Suite - Day 6")
st.sidebar.success("👤 Free User | 3 Professional Apps")
st.sidebar.caption("High Graphics • High Simulation • Vercel + AQ 3.8")

app_choice = st.sidebar.selectbox(
    "🎯 Choose Professional App",
    ["🛺 Auto Fare Kannada Pro", "🛒 Namma Kirana Pro - Paid Store", "🏥 Namma Clinic Pro - Token System"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {t('🔑 AQ API System - Model 3.8', '🔑 AQ API - ಮಾಡೆಲ್ 3.8')}")

DEFAULT_AQ_KEY = ""
api_key = st.sidebar.text_input(
    "AQ API Key (Model 3.8)",
    type="password",
    value=DEFAULT_AQ_KEY,
    placeholder="AQ.Ab8RN6IcvDo76Tq-SbIz5UXl24ufjjHujo4o3WPtHe",
    help="Supports AQ.Ab8... + gsk_... Model 3.8"
)
if not api_key:
    try:
        if "AQ_API_KEY" in st.secrets:
            api_key = st.secrets["AQ_API_KEY"]
            st.sidebar.success("✅ AQ Loaded")
    except:
        pass

model_name = st.sidebar.selectbox("AI Model", ["llama-3.1-8b-instant (Model 3.8)", "llama-3.1-70b-versatile (3.8 Pro)", "gemma2-9b-it (3.8 Lite)"], index=0)
actual_model = model_name.split(" ")[0]

if api_key:
    st.sidebar.success(f"✅ AQ Ready: {api_key[:6]}... | {actual_model} | Vercel ✅")
else:
    st.sidebar.warning("No AQ Key - Local Pro Mode")

def call_aq_model_38(prompt_text, api_key, model):
    if not api_key:
        return None
    try:
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "X-AQ-Model": "3.8", "X-AQ-Key-Format": "AQ.Ab8"}
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {"model": model, "messages": [{"role":"user","content": prompt_text}], "temperature": 0.4, "max_tokens": 700}
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        else:
            return None
    except:
        return None

# ===== HEADER =====
st.markdown(f"""
<div style="text-align:center; padding: 24px 0 8px 0;">
<h1 style="font-size: 3.2rem; font-weight:900; margin:0; background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 20%, #ef4444 50%, #8b5cf6 80%, #06b6d4 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:-0.03em; font-family:'Space Grotesk', sans-serif;">
BHARATH PRO SUITE • 3 APPS
</h1>
<p class="kannada-text" style="font-size:1.25rem; color:#94a3b8; margin-top:10px; font-weight:300;">
{app_choice} • Professional • High Simulation • High Graphics • Vercel + AQ Model 3.8 • Built by Bharath Gowda
</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# APP 1: AUTO FARE KANNADA PRO - PROFESSIONAL
# ============================================================================
if app_choice == "🛺 Auto Fare Kannada Pro":
    def calc_fare(dist, wait, night, luggage):
        fare = 30 + max(0, (dist-2)*15) + (wait//5)*5 + (10 if luggage else 0)
        return round(fare * (1.5 if night else 1))
    
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### {t('📍 Trip Simulation', '📍 ಪ್ರಯಾಣ ಸಿಮ್ಯುಲೇಶನ್')} - Professional")
        c1,c2 = st.columns(2)
        from_loc = c1.text_input(t("From", "ಇಂದ"), value="MG Road")
        to_loc = c2.text_input(t("To", "ಗೆ"), value="Koramangala")
        c1,c2,c3 = st.columns(3)
        distance = c1.slider("Distance km", 0.5, 30.0, 6.5, 0.5)
        waiting = c2.slider("Waiting min", 0, 60, 5, 5)
        luggage = c3.checkbox("Luggage ₹10")
        c1,c2 = st.columns(2)
        is_night = c1.checkbox("Night 1.5x (10PM-5AM)")
        traffic = c2.select_slider("Traffic", options=["Low","Medium","High","Peak"], value="Medium")
        fare = calc_fare(distance, waiting, is_night, luggage)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card" style="margin-top:20px;">', unsafe_allow_html=True)
        st.markdown(f"### 🔥 {t('Live Meter Simulation', 'ಲೈವ್ ಮೀಟರ್ ಸಿಮ್ಯುಲೇಶನ್')}")
        st.markdown(f"""
        <div style="height: 120px; background: linear-gradient(90deg, #1e293b 0%, #334155 50%, #1e293b 100%); border-radius: 60px; position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); margin: 20px 0;">
            <div style="position:absolute; top:50%; left:0; right:0; height:4px; background: repeating-linear-gradient(90deg, #fbbf24 0px, #fbbf24 20px, transparent 20px, transparent 40px); transform: translateY(-50%); opacity:0.6;"></div>
            <div style="position:absolute; top:50%; left:15%; transform: translateY(-50%); font-size: 48px; filter: drop-shadow(0 0 20px rgba(251,191,36,0.8)); animation: autoMove 4s infinite alternate;">🛺</div>
            <div style="position:absolute; right:10%; top:50%; transform: translateY(-50%); font-size: 24px;">🏁 {to_loc}</div>
        </div>
        <style>@keyframes autoMove {{ 0% {{ left:15%; }} 100% {{ left:70%; }} }}</style>
        """, unsafe_allow_html=True)
        
        c1,c2,c3 = st.columns([2,1,1])
        with c1:
            st.markdown(f"""
            <div class="meter-display pulse-gold">
                <div style="font-size:0.85rem; color:#94a3b8; letter-spacing:0.25em; font-weight:600;">BANGALORE AUTO METER • OFFICIAL 2024</div>
                <div class="fare-amount">₹ {fare}</div>
                <div style="color:#fbbf24; font-size:0.95rem; margin-top:8px; font-weight:600;">{distance} KM • {traffic} • {t('Meter', 'ಮೀಟರ್')}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.metric("Per KM", f"₹ {fare/distance:.1f}" if distance else "₹0")
            st.metric("Waiting", f"₹ {(waiting//5)*5}")
        with c3:
            st.metric("Base", "₹30/2km")
            st.metric("Night", "1.5x" if is_night else "1x")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### 🗣️ {t('Kannada Negotiation AI', 'ಕನ್ನಡ ಮಾತುಕತೆ AI')} (AQ 3.8)")
        if st.button(t("🤖 Get Kannada Script", "🤖 ಕನ್ನಡ ಸ್ಕ್ರಿಪ್ಟ್"), type="primary", use_container_width=True):
            prompt = f"Bangalore auto {from_loc} to {to_loc} {distance}km fare ₹{fare} night={is_night} traffic={traffic}. Give 3 short Kannada driver-friendly lines + 1 firm polite line. JSON kannada, english, tip"
            ai = call_aq_model_38(prompt, api_key, actual_model)
            if ai:
                st.success("✅ AQ 3.8 Response")
                st.markdown(f'<div class="kannada-text" style="background: rgba(251,191,36,0.12); padding: 16px; border-radius: 14px; border-left: 4px solid #fbbf24;">{ai[:600]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="kannada-text" style="background: rgba(34,197,94,0.12); padding: 16px; border-radius: 14px; border-left: 4px solid #22c55e;">
                <b>Professional Kannada:</b><br>
                "ಅಣ್ಣಾ {to_loc} ಗೆ {distance} ಕಿಮೀ, ಮೀಟರ್ ₹{fare} ಆಗುತ್ತೆ"<br>
                "ಮೀಟರ್ ಹಾಕಿ, ₹{fare+10} ಕೊಡ್ತೀನಿ"<br>
                <small>Tip: Meter + Smile + Exact change</small>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"#### 💸 {t('Breakdown', 'ವಿವರ')}")
        for k,v in {f"Base 2km":"₹30", f"Extra {max(0,distance-2):.1f}km":"₹{max(0,(distance-2)*15):.0f}", f"Waiting":"₹{(waiting//5)*5}", "Luggage":f"₹{10 if luggage else 0}", "Total":f"₹{fare}"}.items():
            c1,c2 = st.columns([3,1])
            c1.write(k)
            c2.markdown(f"**{v}**")
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# APP 2: NAMMA KIRANA PRO - PAID STORE - HIGH SIMULATION
# ============================================================================
elif app_choice == "🛒 Namma Kirana Pro - Paid Store":
    if "cart" not in st.session_state:
        st.session_state.cart = []
    
    products = [
        {"name":"Tomato / ಟೊಮೆಟೊ","price":40,"stock":50,"unit":"kg","emoji":"🍅"},
        {"name":"Onion / ಈರುಳ್ಳಿ","price":35,"stock":30,"unit":"kg","emoji":"🧅"},
        {"name":"Milk / ಹಾಲು","price":28,"stock":20,"unit":"L","emoji":"🥛"},
        {"name":"Bread / ಬ್ರೆಡ್","price":35,"stock":15,"unit":"pcs","emoji":"🍞"},
        {"name":"Rice / ಅಕ್ಕಿ","price":65,"stock":100,"unit":"kg","emoji":"🍚"},
        {"name":"Oil / ಎಣ್ಣೆ","price":140,"stock":25,"unit":"L","emoji":"🫒"},
        {"name":"Sugar / ಸಕ್ಕರೆ","price":45,"stock":40,"unit":"kg","emoji":"🧂"},
        {"name":"Tea / ಟೀ","price":120,"stock":18,"unit":"kg","emoji":"🍵"},
    ]
    
    col1, col2 = st.columns([1.3, 1], gap="large")
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### 🛒 {t('Namma Kirana Pro - High Simulation Store', 'ನಮ್ಮ ಕಿರಾಣಿ ಪ್ರೊ - ಹೈ ಸಿಮ್ಯುಲೇಶನ್ ಅಂಗಡಿ')}")
        st.caption(t("Professional Mobile Store for Kirana Owners • Sell for ₹5k-10k per store", "ಕಿರಾಣಿ ಮಾಲೀಕರಿಗೆ ವೃತ್ತಿಪರ ಮೊಬೈಲ್ ಅಂಗಡಿ • ಪ್ರತಿ ಅಂಗಡಿಗೆ ₹5k-10k"))
        
        # Search + AQ AI
        c1,c2 = st.columns([2,1])
        search = c1.text_input(t("Search product", "ಉತ್ಪನ್ನ ಹುಡುಕಿ"), placeholder="Tomato, ಹಾಲು...")
        if c2.button(t("🤖 AQ Describe in Kannada", "🤖 AQ ಕನ್ನಡದಲ್ಲಿ ವಿವರಿಸಿ"), use_container_width=True):
            prompt = f"Describe {search or 'Tomato'} for kirana store in Kannada + English, 2 lines, price tip. JSON kn, en, tip"
            ai = call_aq_model_38(prompt, api_key, actual_model)
            if ai:
                st.info(ai[:400])
            else:
                st.info("🍅 ಟೊಮೆಟೊ - ತಾಜಾ, 1 ಕೆಜಿ ₹40, ಇಂದು ತಂದದ್ದು / Fresh tomato, 1kg ₹40")
        
        # Product grid - high graphics
        cols = st.columns(2)
        for i, p in enumerate(products):
            if search and search.lower() not in p['name'].lower():
                continue
            with cols[i%2]:
                st.markdown(f"""
                <div class="product-card shimmer" style="margin-bottom: 12px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size: 2rem;">{p['emoji']}</span>
                        <span style="background: rgba(34,197,94,0.3); padding: 4px 10px; border-radius: 20px; font-size:0.8rem;">Stock: {p['stock']}</span>
                    </div>
                    <div style="font-weight:700; margin: 8px 0; font-size:1.05rem;">{p['name']}</div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:1.3rem; font-weight:900; color:#22c55e;">₹{p['price']}/{p['unit']}</span>
                        <span style="color:#94a3b8; font-size:0.85rem;">{p['unit']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                c1,c2 = st.columns(2)
                if c1.button(f"➕ Add", key=f"add_{i}", use_container_width=True):
                    st.session_state.cart.append(p)
                    st.toast(f"Added {p['name']}")
                if c2.button(f"🔊 Voice", key=f"voice_{i}", use_container_width=True):
                    st.toast(f"🔊 {p['name']} - ₹{p['price']}")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### 🧾 {t('Live Bill Simulation', 'ಲೈವ್ ಬಿಲ್ ಸಿಮ್ಯುಲೇಶನ್')} - Professional")
        
        if not st.session_state.cart:
            st.info(t("Cart empty - Add products", "ಕಾರ್ಟ್ ಖಾಲಿ - ಉತ್ಪನ್ನ ಸೇರಿಸಿ"))
        else:
            total = sum([p['price'] for p in st.session_state.cart])
            st.markdown(f"""
            <div class="meter-display pulse-gold" style="border-color:#22c55e;">
                <div style="font-size:0.85rem; color:#94a3b8; letter-spacing:0.2em;">LIVE BILL • KIRANA PRO</div>
                <div class="fare-amount" style="background: linear-gradient(135deg, #22c55e, #16a34a); -webkit-background-clip:text;">₹ {total}</div>
                <div style="color:#22c55e; font-size:0.9rem;">{len(st.session_state.cart)} items • {t('Kannada Voice Ready', 'ಕನ್ನಡ ಧ್ವನಿ ಸಿದ್ಧ')}</div>
            </div>
            """, unsafe_allow_html=True)
            
            for idx, item in enumerate(st.session_state.cart):
                c1,c2,c3 = st.columns([1,2,1])
                c1.write(f"{item['emoji']}")
                c2.write(f"{item['name']} - ₹{item['price']}")
                if c3.button("❌", key=f"rem_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()
            
            st.markdown("---")
            st.markdown(f"**Total: ₹{total}** + Delivery ₹20 = **₹{total+20}**")
            
            c1,c2 = st.columns(2)
            if c1.button("💳 Pay via QR", type="primary", use_container_width=True):
                st.success(f"✅ QR Generated: ₹{total+20} - Share to customer")
                st.balloons()
            if c2.button("🔊 Kannada Voice Bill", use_container_width=True):
                st.info(f"🔊 ಒಟ್ಟು ₹{total+20}, {len(st.session_state.cart)} ವಸ್ತುಗಳು")
            
            if st.button("📤 WhatsApp Customer", use_container_width=True):
                st.success("WhatsApp bill sent!")
        
        st.markdown("---")
        st.markdown(f"### 🚀 {t('Sell This Store', 'ಈ ಅಂಗಡಿ ಮಾರಿ')} - ₹5k-10k")
        st.markdown("""
        - ✅ **For Kirana Owner:** Your name, your products, your QR
        - ✅ **High Graphics:** Glass cards + Shimmer + Pulse bill
        - ✅ **AQ API:** Describe any product in Kannada (Model 3.8)
        - ✅ **Vercel:** `api/products` ready
        - ✅ **Mobile:** PWA installable
        - 💰 **Charge:** ₹5k setup + ₹300/month
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# APP 3: NAMMA CLINIC PRO - TOKEN SYSTEM - HIGH SIMULATION
# ============================================================================
else:
    if "tokens" not in st.session_state:
        st.session_state.tokens = [{"id":i, "name":f"Patient {i}", "status":"waiting" if i>1 else "current"} for i in range(1, 11)]
    
    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### 🏥 {t('Namma Clinic Pro - Token System', 'ನಮ್ಮ ಕ್ಲಿನಿಕ್ ಪ್ರೊ - ಟೋಕನ್ ವ್ಯವಸ್ಥೆ')} - Professional")
        st.caption(t("Sell to clinics for ₹10k-15k • Live queue simulation", "ಕ್ಲಿನಿಕ್‌ಗಳಿಗೆ ₹10k-15k ಗೆ ಮಾರಿ • ಲೈವ್ ಕ್ಯೂ ಸಿಮ್ಯುಲೇಶನ್"))
        
        # Token simulation
        st.markdown(f"#### 🔥 {t('Live Token Queue', 'ಲೈವ್ ಟೋಕನ್ ಕ್ಯೂ')} - High Simulation")
        token_html = '<div class="token-queue">'
        for tok in st.session_state.tokens[:10]:
            active_class = "active" if tok['status']=="current" else ""
            token_html += f'<div class="token-item {active_class}">{tok["id"]}</div>'
        token_html += '</div>'
        st.markdown(token_html, unsafe_allow_html=True)
        
        c1,c2,c3 = st.columns(3)
        c1.metric(t("Current Token", "ಪ್ರಸ್ತುತ ಟೋಕನ್"), "#1", "Dr. seeing")
        c2.metric(t("Waiting", "ಕಾಯುವಿಕೆ"), "9", "15 min each")
        c3.metric(t("Next", "ಮುಂದಿನ"), "#2", "Ready")
        
        # Add token
        with st.form("add_token"):
            c1,c2 = st.columns(2)
            name = c1.text_input(t("Patient Name", "ರೋಗಿ ಹೆಸರು"), placeholder="Bharath Gowda")
            phone = c2.text_input(t("Phone", "ಫೋನ್"), placeholder="9876543210")
            c1,c2 = st.columns(2)
            reason = c1.selectbox(t("Reason", "ಕಾರಣ"), ["Fever / ಜ್ವರ", "Cold / ಶೀತ", "Diabetes / ಸಕ್ಕರೆ", "BP Check", "General"])
            lang_pref = c2.selectbox("Language", ["ಕನ್ನಡ", "English"])
            if st.form_submit_button(t("➕ Book Token ₹50", "➕ ಟೋಕನ್ ಬುಕ್ ಮಾಡಿ ₹50"), type="primary", use_container_width=True):
                new_id = len(st.session_state.tokens)+1
                st.session_state.tokens.append({"id":new_id, "name":name or f"Patient {new_id}", "status":"waiting", "reason":reason})
                st.success(f"✅ Token #{new_id} booked for {name} - {reason}")
                st.balloons()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f"### 🤖 {t('AQ Prescription AI', 'AQ ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ AI')} (Model 3.8)")
        
        med_input = st.text_input(t("Medicine / Prescription", "ಔಷಧಿ / ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್"), placeholder="Dolo 650, Telma 40...")
        if st.button(t("🔍 Explain in Kannada + English", "🔍 ಕನ್ನಡ + ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ವಿವರಿಸಿ"), type="primary", use_container_width=True) and med_input:
            with st.spinner(t("AQ Model 3.8 explaining...", "AQ ಮಾಡೆಲ್ 3.8 ವಿವರಿಸುತ್ತಿದೆ...")):
                prompt = f"Explain medicine {med_input} for Karnataka clinic patient in Kannada + English simple, dosage, after food, side effect. JSON kn, en, tip, side"
                ai = call_aq_model_38(prompt, api_key, actual_model)
                if ai:
                    st.success(f"✅ {med_input} - AQ 3.8")
                    st.markdown(f'<div class="kannada-text" style="background: rgba(59,130,246,0.12); padding: 16px; border-radius: 14px; border-left: 4px solid #3b82f6;">{ai[:700]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="kannada-text" style="background: rgba(59,130,246,0.12); padding: 16px; border-radius: 14px;">
                    <b>{med_input}:</b><br>
                    ಜ್ವರಕ್ಕೆ, ಬೆಳಿಗ್ಗೆ 1 ಮಾತ್ರೆ, ರಾತ್ರಿ 1 ಮಾತ್ರೆ, ಊಟದ ನಂತರ 3 ದಿನ<br>
                    <small>After food, 3 days</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"#### 📊 {t('Clinic Analytics', 'ಕ್ಲಿನಿಕ್ ವಿಶ್ಲೇಷಣೆ')}")
        c1,c2 = st.columns(2)
        c1.metric("Today Patients", "23", "+5")
        c2.metric("Revenue", "₹1,150", "₹50/token")
        
        # Chart simulation
        st.bar_chart({"Mon":20, "Tue":25, "Wed":18, "Thu":23, "Fri":30, "Sat":15})
        
        st.markdown(f"### 💰 {t('Sell This Clinic System', 'ಈ ಕ್ಲಿನಿಕ್ ವ್ಯವಸ್ಥೆ ಮಾರಿ')}")
        st.markdown("""
        - ✅ **For Clinic:** Token + Queue + Prescription AI
        - ✅ **High Simulation:** Live token queue + Pulse current token
        - ✅ **AQ API:** Explain any medicine in Kannada (3.8)
        - ✅ **Vercel:** `api/tokens` ready
        - ✅ **Paid:** ₹10k-15k per clinic + ₹500/month
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding: 28px; background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%); border-radius: 28px; border: 1px solid rgba(255,255,255,0.1);">
<h3 style="margin:0; font-size:1.9rem; font-weight:900; letter-spacing:-0.02em;">🚀 BHARATH PRO SUITE • 3 PROFESSIONAL APPS • DAY 6 • GITHUB STREAK</h3>
<p style="color:#94a3b8; margin: 12px 0 0 0; font-size:1.05rem;">🛺 Auto Fare + 🛒 Kirana Pro + 🏥 Clinic Pro • High Simulation • High Graphics • Glassmorphism • 60 FPS • Vercel + AQ Model 3.8 • Built by Bharath Gowda Hm</p>
<p style="color:#fbbf24; font-size:0.95rem; margin-top:14px; font-weight:600;">⚡ Most Powerful Ideas • Production Grade • Paid Ready • ₹5k-15k per client • Bangalore • Hassan • Devanahalli</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Vercel Deploy")
st.sidebar.code("vercel --prod", language="bash")
st.sidebar.caption("3 Apps in 1 • api/ folder • AQ_AB8... + gsk_... support")
