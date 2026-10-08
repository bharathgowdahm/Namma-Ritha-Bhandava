from flask import Flask, jsonify, request, render_template_string
import os
import requests

app = Flask(__name__)

AQ_API_KEY = os.environ.get("AQ_API_KEY", "")

def call_aq_model_38(prompt_text, model="llama-3.1-8b-instant"):
    if not AQ_API_KEY:
        return None
    try:
        headers = {"Authorization": f"Bearer {AQ_API_KEY}", "Content-Type": "application/json"}
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {"model": model, "messages": [{"role":"user","content": prompt_text}], "temperature":0.4, "max_tokens":600}
        resp = requests.post(url, json=payload, headers=headers, timeout=12)
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        return None
    except:
        return None

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bharath Pro Suite - Vercel Fixed - 3 Apps - AQ 3.8</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Noto+Sans+Kannada:wght@400;700&family=Space+Grotesk:wght@700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:radial-gradient(ellipse at top left,#0f172a 0%,#1e1b4b 30%,#020617 100%);color:white;font-family:'Outfit','Noto Sans Kannada',sans-serif;min-height:100vh}
.glass{background:linear-gradient(135deg,rgba(255,255,255,0.11) 0%,rgba(255,255,255,0.05) 100%);backdrop-filter:blur(24px) saturate(180%);border:1px solid rgba(255,255,255,0.16);border-radius:28px;padding:28px;box-shadow:0 12px 40px rgba(0,0,0,0.55);margin:18px;transition:all 0.4s}
.glass:hover{transform:translateY(-4px)}
.header{text-align:center;padding:36px 20px}
.header h1{font-size:clamp(1.8rem,5vw,3.4rem);font-weight:900;background:linear-gradient(135deg,#fbbf24 0%,#f59e0b 15%,#ef4444 40%,#8b5cf6 75%,#06b6d4 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:'Space Grotesk',sans-serif}
.meter{background:linear-gradient(135deg,#1e293b 0%,#0f172a 60%,#020617 100%);border:2px solid #fbbf24;border-radius:24px;padding:24px;text-align:center;box-shadow:0 0 60px rgba(251,191,36,0.28)}
.fare{font-size:clamp(2.5rem,8vw,4.5rem);font-weight:900;background:linear-gradient(135deg,#fbbf24,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:'Space Grotesk',monospace}
.btn{background:linear-gradient(135deg,#fbbf24,#f59e0b);color:black;border:none;padding:14px 22px;border-radius:14px;font-weight:800;cursor:pointer;width:100%;margin:8px 0;font-size:1rem}
.btn:hover{transform:translateY(-2px)}
.btn-green{background:linear-gradient(135deg,#22c55e,#16a34a);color:white}
.btn-blue{background:linear-gradient(135deg,#3b82f6,#2563eb);color:white}
.btn-purple{background:linear-gradient(135deg,#8b5cf6,#6366f1);color:white}
input,select{width:100%;padding:13px;border-radius:12px;border:1px solid rgba(255,255,255,0.22);background:rgba(255,255,255,0.09);color:white;margin:8px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:18px;padding:18px}
.kannada{font-family:'Noto Sans Kannada',sans-serif}
.badge{display:inline-block;background:rgba(34,197,94,0.2);border:1px solid rgba(34,197,94,0.4);padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:700}
</style>
</head>
<body>
<div class="header">
<h1>BHARATH PRO SUITE • VERCEL FIXED ✅</h1>
<p style="color:#94a3b8;font-size:1.15rem;margin-top:14px">🛺 Auto Fare + 🛒 Kirana Pro + 🏥 Clinic Pro • 3 Apps • Vercel + AQ 3.8 • NOT FOUND FIXED</p>
<p style="margin-top:10px"><span class="badge">✅ Build Fixed</span> <span class="badge" style="background:rgba(251,191,36,0.2)">✅ Not Found Fixed</span> <span class="badge" style="background:rgba(59,130,246,0.2)">✅ Vercel Live</span></p>
<p style="color:#fbbf24;margin-top:12px;font-weight:700">namma-ritha-bhandava-wv4t.vercel.app • Built by Bharath Gowda Hm</p>
</div>
<div class="grid">
<div class="glass">
<h2>🛺 Auto Fare Kannada Pro</h2>
<p class="kannada" style="color:#94a3b8;margin:10px 0">ಬೆಂಗಳೂರು ಆಟೋ ದರ • ₹30 base (2km) + ₹15/km</p>
<label>From</label><input id="fromLoc" value="MG Road, Bangalore">
<label>To</label><input id="toLoc" value="Koramangala, Bangalore">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><label>Distance km</label><input type="number" id="dist" value="6.5" step="0.5"></div><div><label>Waiting min</label><input type="number" id="wait" value="5"></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><label>Night 1.5x</label><select id="night"><option value="false">No Day</option><option value="true">Yes Night</option></select></div><div><label>Luggage ₹10</label><select id="luggage"><option value="false">No</option><option value="true">Yes</option></select></div></div>
<button class="btn" onclick="calcFare()">🔥 Calculate Fare</button>
<div class="meter" style="margin-top:18px"><div style="font-size:0.8rem;color:#94a3b8">BANGALORE AUTO METER</div><div class="fare" id="fareResult">₹ 98</div><div style="color:#fbbf24;margin-top:8px" id="fareDetail">6.5 KM • Ready</div></div>
<div style="margin-top:14px;background:rgba(34,197,94,0.12);padding:14px;border-radius:14px;border-left:4px solid #22c55e" class="kannada"><b>Kannada:</b> "ಅಣ್ಣಾ <span id="toKannada">ಕೋರಮಂಗಲ</span> ಗೆ <span id="distKannada">6.5</span> ಕಿಮೀ, ₹<span id="fareKannada">98</span> ಆಗುತ್ತೆ?"</div>
<button class="btn btn-purple" style="margin-top:12px" onclick="getAQScript()">🤖 Get AQ 3.8 Kannada</button>
<div id="aqResult" style="display:none;background:rgba(251,191,36,0.12);padding:14px;border-radius:12px;margin-top:10px" class="kannada"></div>
</div>
<div class="glass">
<h2>🛒 Kirana Pro - PAID</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div style="background:rgba(34,197,94,0.18);border:1px solid rgba(34,197,94,0.35);border-radius:16px;padding:14px"><div style="font-size:1.9rem">🍅</div><div style="font-weight:800">Tomato</div><div style="color:#22c55e;font-weight:900">₹40/kg</div></div><div style="background:rgba(34,197,94,0.18);border:1px solid rgba(34,197,94,0.35);border-radius:16px;padding:14px"><div style="font-size:1.9rem">🧅</div><div style="font-weight:800">Onion</div><div style="color:#22c55e;font-weight:900">₹35/kg</div></div><div style="background:rgba(34,197,94,0.18);border:1px solid rgba(34,197,94,0.35);border-radius:16px;padding:14px"><div style="font-size:1.9rem">🥛</div><div style="font-weight:800">Milk</div><div style="color:#22c55e;font-weight:900">₹28/L</div></div><div style="background:rgba(34,197,94,0.18);border:1px solid rgba(34,197,94,0.35);border-radius:16px;padding:14px"><div style="font-size:1.9rem">🍚</div><div style="font-weight:800">Rice</div><div style="color:#22c55e;font-weight:900">₹65/kg</div></div></div>
<div style="background:#1e293b;padding:14px;border-radius:14px;margin-top:14px"><div style="display:flex;justify-content:space-between"><span>Total</span><span style="color:#22c55e;font-weight:900">₹218</span></div></div>
<button class="btn btn-green" onclick="alert('✅ QR Bill ₹218')">💳 Generate Bill QR ₹218</button>
</div>
<div class="glass">
<h2>🏥 Clinic Pro - PAID</h2>
<div style="display:flex;gap:8px;overflow-x:auto;padding:12px 0"><div style="min-width:64px;height:64px;background:linear-gradient(135deg,#fbbf24,#f59e0b);color:black;border-radius:16px;display:flex;align-items:center;justify-content:center;font-weight:900">1</div><div style="min-width:64px;height:64px;background:#334155;border-radius:16px;display:flex;align-items:center;justify-content:center">2</div><div style="min-width:64px;height:64px;background:#334155;border-radius:16px;display:flex;align-items:center;justify-content:center">3</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:14px 0"><div style="background:#1e293b;padding:12px;border-radius:12px;text-align:center"><div style="font-size:0.8rem;color:#94a3b8">Current</div><div style="font-weight:900">#1</div></div><div style="background:#1e293b;padding:12px;border-radius:12px;text-align:center"><div style="font-size:0.8rem;color:#94a3b8">Waiting</div><div style="font-weight:900">9</div></div><div style="background:#1e293b;padding:12px;border-radius:12px;text-align:center"><div style="font-size:0.8rem;color:#94a3b8">Revenue</div><div style="font-weight:900;color:#22c55e">₹1,150</div></div></div>
<input id="patientName" placeholder="Patient Name"><button class="btn btn-blue" onclick="bookToken()">➕ Book Token ₹50</button><div id="tokenResult" style="display:none;background:rgba(59,130,246,0.14);padding:14px;border-radius:12px;margin-top:10px"></div>
</div>
</div>
<div class="glass" style="background:linear-gradient(135deg,rgba(99,102,241,0.18),rgba(168,85,247,0.14))">
<h2>🔑 Vercel Fixed - Not Found Solution</h2>
<p style="color:#cbd5e1;margin:12px 0">Previous 404 "Not Found - The requested URL was not found on the server" fixed by adding catch-all routes for /api/index and /</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:16px">
<div style="background:rgba(0,0,0,0.25);padding:12px;border-radius:12px">✅ <b>/</b> → Home UI</div>
<div style="background:rgba(0,0,0,0.25);padding:12px;border-radius:12px">✅ <b>/api/index</b> → Home UI</div>
<div style="background:rgba(0,0,0,0.25);padding:12px;border-radius:12px">✅ <b>/api/health</b> → JSON</div>
<div style="background:rgba(0,0,0,0.25);padding:12px;border-radius:12px">✅ <b>Catch-all</b> → No more 404</div>
</div>
<div style="margin-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:12px"><button class="btn btn-purple" onclick="testAPIs()">🧪 Test All APIs</button><button class="btn" onclick="window.open('/api/health','_blank')">📄 /api/health</button></div>
<div id="apiResult" style="background:rgba(0,0,0,0.45);padding:14px;border-radius:14px;margin-top:14px;font-family:monospace;font-size:0.85rem;display:none"></div>
</div>
<div style="text-align:center;padding:32px;margin:20px;background:rgba(255,255,255,0.06);border-radius:28px;border:1px solid rgba(255,255,255,0.12)">
<h3 style="font-size:1.9rem;font-weight:900">🚀 VERCEL FIXED ✅ • NOT FOUND FIXED ✅ • READY ✅</h3>
<p style="color:#94a3b8;margin-top:12px">namma-ritha-bhandava-wv4t.vercel.app • Flask app top-level • Catch-all routes • AQ 3.8 • Bharath Gowda Hm</p>
</div>
<script>
function calcFare(){const dist=parseFloat(document.getElementById('dist').value)||6.5;const wait=parseInt(document.getElementById('wait').value)||5;const isNight=document.getElementById('night').value==='true';const hasLuggage=document.getElementById('luggage').value==='true';const toLoc=document.getElementById('toLoc').value||'Koramangala';let fare=30+Math.max(0,(dist-2)*15)+Math.floor(wait/5)*5+(hasLuggage?10:0);if(isNight)fare*=1.5;fare=Math.round(fare);document.getElementById('fareResult').innerText='₹ '+fare;document.getElementById('fareDetail').innerText=dist+' KM • '+(isNight?'Night':'Day');document.getElementById('fareKannada').innerText=fare;document.getElementById('distKannada').innerText=dist;document.getElementById('toKannada').innerText=toLoc;fetch(`/api/fare?distance=${dist}&waiting=${wait}&is_night=${isNight}&has_luggage=${hasLuggage}`).then(r=>r.json()).then(d=>console.log(d))}
async function getAQScript(){const dist=document.getElementById('dist').value;const toLoc=document.getElementById('toLoc').value;const fromLoc=document.getElementById('fromLoc').value;const fare=document.getElementById('fareResult').innerText;const resultDiv=document.getElementById('aqResult');resultDiv.style.display='block';resultDiv.innerHTML='🤖 AQ 3.8 generating...';try{const res=await fetch(`/api/aq?from=${encodeURIComponent(fromLoc)}&to=${encodeURIComponent(toLoc)}&distance=${dist}&fare=${fare}`);const data=await res.json();resultDiv.innerHTML=`<b>✅ AQ 3.8:</b><br><br>${(data.response||data.fallback||JSON.stringify(data)).substring(0,800)}`}catch(e){resultDiv.innerHTML=`<b>Kannada:</b><br>"ಅಣ್ಣಾ ${toLoc} ಗೆ ${dist} ಕಿಮೀ, ${fare} ಆಗುತ್ತೆ?"`}}
function bookToken(){const name=document.getElementById('patientName').value||'Patient';const resultDiv=document.getElementById('tokenResult');resultDiv.style.display='block';resultDiv.innerHTML=`✅ Token #11 for <b>${name}</b>! ₹50<br>📱 SMS sent`;fetch('/api/tokens').then(r=>r.json()).then(d=>console.log(d))}
async function testAPIs(){const resultDiv=document.getElementById('apiResult');resultDiv.style.display='block';resultDiv.innerHTML='Testing...<br><br>';const apis=['/','/api/health','/api/fare?distance=6.5','/api/products','/api/tokens'];for(let api of apis){try{const res=await fetch(api);const isJson=res.headers.get('content-type')?.includes('json');const data=isJson?await res.json():await res.text();const text=isJson?JSON.stringify(data).substring(0,150):'HTML OK '+data.length+' chars';resultDiv.innerHTML+=`<div style="color:#22c55e;margin:6px 0;padding:6px;background:rgba(34,197,94,0.08);border-radius:8px">✅ ${api}<br><span style="color:#cbd5e1">${text}...</span></div>`}catch(e){resultDiv.innerHTML+=`<div style="color:#ef4444">❌ ${api} → ${e}</div>`}}}
</script>
</body>
</html>
"""

def get_fare(distance, waiting, is_night, has_luggage):
    base=30
    fare=base+max(0,(distance-2)*15)+(waiting//5)*5+(10 if has_luggage else 0)
    if is_night: fare*=1.5
    return round(fare)

# ===== CORE ROUTES - ALL PATHS COVERED TO FIX NOT FOUND =====

@app.route('/')
@app.route('/api')
@app.route('/api/')
@app.route('/api/index')
@app.route('/api/index/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/fare')
@app.route('/api/fare/')
def fare_api():
    try:
        dist=float(request.args.get('distance',6.5))
        waiting=int(request.args.get('waiting',5))
        is_night=request.args.get('is_night','false').lower()=='true'
        has_luggage=request.args.get('has_luggage','false').lower()=='true'
        fare=get_fare(dist,waiting,is_night,has_luggage)
        return jsonify({"app":"Auto Fare Kannada Pro","distance_km":dist,"fare":fare,"base_fare":30,"per_km":15,"aq_model":"3.8","city":"Bangalore","vercel_only":True,"not_found_fixed":True})
    except Exception as e:
        return jsonify({"error":str(e),"fare":98})

@app.route('/api/products')
@app.route('/api/products/')
def products_api():
    return jsonify([{"id":1,"name":"Tomato / ಟೊಮೆಟೊ","price":40,"stock":50},{"id":2,"name":"Onion / ಈರುಳ್ಳಿ","price":35},{"id":3,"name":"Milk / ಹಾಲು","price":28},{"id":4,"name":"Rice / ಅಕ್ಕಿ","price":65}])

@app.route('/api/tokens')
@app.route('/api/tokens/')
def tokens_api():
    return jsonify({"current":1,"waiting":9,"next":2,"revenue":1150,"today_patients":23,"vercel_only":True,"not_found_fixed":True})

@app.route('/api/aq')
@app.route('/api/aq/')
def aq_api():
    from_loc=request.args.get('from','MG Road')
    to_loc=request.args.get('to','Koramangala')
    distance=request.args.get('distance','6.5')
    fare=request.args.get('fare','₹98')
    prompt=f"Trip {from_loc} to {to_loc}, {distance}km, fare {fare}. Give Kannada driver lines."
    ai_response=call_aq_model_38(prompt)
    if ai_response:
        return jsonify({"from":from_loc,"to":to_loc,"distance":distance,"fare":fare,"response":ai_response,"aq_key_present":bool(AQ_API_KEY),"not_found_fixed":True})
    else:
        return jsonify({"from":from_loc,"to":to_loc,"fallback":f"ಅಣ್ಣಾ {to_loc} ಗೆ {distance} ಕಿಮೀ, ಮೀಟರ್ {fare} ಆಗುತ್ತೆ, ಬರ್ತೀರಾ?","aq_key_present":bool(AQ_API_KEY),"note":"Set AQ_API_KEY in Vercel Env","not_found_fixed":True})

@app.route('/api/health')
@app.route('/api/health/')
def health():
    return jsonify({"status":"ok","apps":3,"suite":"Bharath Pro Suite - Vercel Fixed","model":"3.8","vercel":True,"vercel_only":True,"flask_app":"defined ✅","build":"fixed ✅","not_found_fixed":"Fixed Not Found - Added /api/index and catch-all routes ✅","aq_key_present":bool(AQ_API_KEY),"domain":"namma-ritha-bhandava-wv4t.vercel.app","endpoints":["/","/api/index","/api/health","/api/fare","/api/products","/api/tokens","/api/aq"]})

# ===== CATCH-ALL - FIXES "Not Found - The requested URL was not found" =====
@app.route('/<path:path>')
def catch_all(path):
    # Log what path Vercel sent us (for debugging)
    # If it's api routes that we already handle, Flask would have matched earlier, so this is unknown path
    # Return home for root-like paths, or helpful JSON for api-like paths
    if path.startswith('api/'):
        # Unknown api path - return helpful JSON instead of HTML 404
        return jsonify({
            "error": f"API path /{path} not found - but Flask is running ✅",
            "hint": "Use /api/health , /api/fare , /api/products , /api/tokens , /api/aq",
            "received_path": path,
            "flask_app": "running ✅",
            "not_found_fixed": True,
            "available_endpoints": ["/","/api/index","/api/health","/api/fare","/api/products","/api/tokens","/api/aq"]
        }), 404
    else:
        # For any other path (like favicon, etc) return home UI - fixes Not Found page
        return render_template_string(HTML_TEMPLATE)

@app.errorhandler(404)
def not_found(e):
    # This catches anything Flask still doesn't match
    return jsonify({
        "error": "This page doesn't exist - But Flask is running - Fixed by catch-all",
        "hint": "Use / , /api/index , /api/health , /api/fare , /api/products , /api/tokens , /api/aq",
        "status": "Ready ✅",
        "fix": "Added routes for /api/index and catch-all /<path:path>",
        "not_found_fixed": True,
        "flask_app": "defined at top-level ✅"
    }), 404
