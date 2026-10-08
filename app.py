from flask import Flask, jsonify, request, render_template_string
import os
import requests
from datetime import datetime

app = Flask(__name__)
AQ_API_KEY = os.environ.get("AQ_API_KEY", "")

TOKENS = [
    {"id":1,"name":"Ramesh Gowda","phone":"9876543210","age":45,"symptom":"Fever","status":"current","time":"09:15 AM","fee":50},
    {"id":2,"name":"Lakshmi","phone":"9876543211","age":32,"symptom":"Cough","status":"waiting","time":"09:18 AM","fee":50},
    {"id":3,"name":"Suresh","phone":"9876543212","age":28,"symptom":"Headache","status":"waiting","time":"09:22 AM","fee":50},
]
CURRENT_TOKEN = 1

def call_aq_clinic(prompt_text):
    if not AQ_API_KEY:
        return None
    try:
        headers = {"Authorization": f"Bearer {AQ_API_KEY}", "Content-Type": "application/json"}
        url = "https://api.groq.com/openai/v1/chat/completions"
        payload = {"model":"llama-3.1-8b-instant","messages":[{"role":"user","content":prompt_text}],"temperature":0.3,"max_tokens":250}
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        return None
    except:
        return None

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Namma Clinic Pro - Token Queue - Vercel</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Noto+Sans+Kannada:wght@400;700&family=Space+Grotesk:wght@700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:radial-gradient(ellipse at top left,#0f172a 0%,#1e293b 20%,#020617 100%);color:white;font-family:'Outfit','Noto Sans Kannada',sans-serif;min-height:100vh}
.glass{background:linear-gradient(135deg,rgba(255,255,255,0.10) 0%,rgba(255,255,255,0.04) 100%);backdrop-filter:blur(28px) saturate(180%);border:1px solid rgba(255,255,255,0.14);border-radius:26px;padding:26px;box-shadow:0 12px 40px rgba(0,0,0,0.6);margin:16px;transition:all 0.4s}
.glass:hover{transform:translateY(-3px)}
.header{text-align:center;padding:32px 20px}
.header h1{font-size:clamp(2rem,5vw,3.6rem);font-weight:900;background:linear-gradient(135deg,#38bdf8 0%,#3b82f6 25%,#8b5cf6 60%,#06b6d4 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:'Space Grotesk',sans-serif;line-height:1.05}
.token-big{background:linear-gradient(135deg,#1e293b 0%,#0f172a 70%,#020617 100%);border:2px solid #38bdf8;border-radius:22px;padding:22px;text-align:center;box-shadow:0 0 70px rgba(56,189,248,0.25)}
.token-number{font-size:clamp(3rem,9vw,5rem);font-weight:900;background:linear-gradient(135deg,#38bdf8,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:'Space Grotesk',monospace}
.btn{background:linear-gradient(135deg,#3b82f6,#2563eb);color:white;border:none;padding:13px 20px;border-radius:14px;font-weight:800;cursor:pointer;width:100%;margin:7px 0;font-size:0.95rem}
.btn:hover{transform:translateY(-2px)}
.btn-green{background:linear-gradient(135deg,#22c55e,#16a34a)}
.btn-gold{background:linear-gradient(135deg,#fbbf24,#f59e0b);color:black}
.btn-purple{background:linear-gradient(135deg,#8b5cf6,#6366f1)}
.btn-red{background:linear-gradient(135deg,#ef4444,#dc2626)}
input,select,textarea{width:100%;padding:12px 14px;border-radius:12px;border:1px solid rgba(255,255,255,0.20);background:rgba(255,255,255,0.08);color:white;margin:6px 0;font-size:0.95rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px;padding:16px}
.kannada{font-family:'Noto Sans Kannada',sans-serif}
.badge{display:inline-block;background:rgba(34,197,94,0.18);border:1px solid rgba(34,197,94,0.35);padding:5px 14px;border-radius:20px;font-size:0.8rem;font-weight:800;margin:4px}
.badge-blue{background:rgba(59,130,246,0.18);border-color:rgba(59,130,246,0.35)}
.badge-gold{background:rgba(251,191,36,0.18);border-color:rgba(251,191,36,0.35)}
.queue-item{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:14px;margin:8px 0}
.queue-item.current{border-color:#38bdf8;background:linear-gradient(135deg,rgba(56,189,248,0.18),rgba(59,130,246,0.12))}
.dot{width:14px;height:14px;border-radius:50%}
.dot-current{background:#38bdf8;box-shadow:0 0 12px #38bdf8;animation:pulse 2s infinite}
.dot-waiting{background:#fbbf24}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(56,189,248,0.7)}50%{box-shadow:0 0 0 10px rgba(56,189,248,0)}100%{box-shadow:0 0 0 0 rgba(56,189,248,0)}}
.stat{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:12px 0}
.stat-box{background:#1e293b;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:12px;text-align:center}
</style>
</head>
<body>
<div class="header">
<h1>NAMMA CLINIC PRO • TOKEN QUEUE</h1>
<p>🏥 Clinic Token Management • Doctor Dashboard • High Graphics • Vercel + AQ 3.8</p>
<p style="margin-top:10px"><span class="badge">✅ Clinic Pro Only</span> <span class="badge badge-blue">✅ Vercel Ready</span> <span class="badge badge-gold">✅ Not Found Fixed</span></p>
<p style="color:#38bdf8;margin-top:10px;font-weight:700">Built by Bharath Gowda Hm | PAID ₹10k-15k/clinic + ₹500/month</p>
</div>
<div class="grid">
<div class="glass">
<h2>🎫 Live Token Board</h2>
<div class="token-big" style="margin-top:14px">
<div style="font-size:0.8rem;color:#94a3b8;font-weight:700">CURRENT TOKEN • NOW SERVING</div>
<div class="token-number" id="currentTokenDisplay">#1</div>
<div style="color:#38bdf8;margin-top:8px;font-weight:700" id="currentPatientDisplay">Ramesh Gowda • Fever • 09:15 AM</div>
<div style="color:#94a3b8;font-size:0.85rem;margin-top:6px" id="currentPhone">📱 9876543210 • Fee ₹50</div>
</div>
<div class="stat">
<div class="stat-box"><div style="font-size:0.75rem;color:#94a3b8">WAITING</div><div style="font-weight:900;font-size:1.4rem" id="waitingCount">9</div></div>
<div class="stat-box"><div style="font-size:0.75rem;color:#94a3b8">TODAY</div><div style="font-weight:900;font-size:1.4rem" id="todayCount">23</div></div>
<div class="stat-box"><div style="font-size:0.75rem;color:#94a3b8">REVENUE</div><div style="font-weight:900;font-size:1.4rem;color:#22c55e" id="revenueDisplay">₹1,150</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px">
<button class="btn btn-green" onclick="callNext()">⏭️ Call Next</button>
<button class="btn btn-gold" onclick="markDone()">✅ Done</button>
</div>
<button class="btn btn-red" onclick="resetQueue()" style="margin-top:8px">🔄 Reset Day</button>
<div id="actionResult" style="display:none;background:rgba(56,189,248,0.12);padding:12px;border-radius:12px;margin-top:12px;border-left:4px solid #38bdf8;font-size:0.9rem"></div>
</div>
<div class="glass">
<h2>➕ Book Token • ಹೊಸ ಟೋಕನ್</h2>
<p class="kannada" style="color:#94a3b8;margin:8px 0;font-size:0.9rem">ರೋಗಿ ವಿವರ • Patient Details • AQ 3.8</p>
<input id="pName" placeholder="Patient Name / ರೋಗಿ ಹೆಸರು">
<input id="pPhone" placeholder="Phone / ಫೋನ್">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<input id="pAge" type="number" placeholder="Age">
<select id="pGender"><option>Male</option><option>Female</option></select>
</div>
<textarea id="pSymptom" rows="2" placeholder="Symptoms / ಲಕ್ಷಣಗಳು"></textarea>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<select id="pType"><option>New Patient</option><option>Follow-up</option><option>Emergency</option></select>
<input id="pFee" type="number" value="50">
</div>
<button class="btn" onclick="bookToken()">➕ Book Token ₹50</button>
<div id="bookResult" style="display:none;margin-top:12px"></div>
<div id="aqSymptomResult" style="display:none;background:rgba(251,191,36,0.12);padding:12px;border-radius:12px;margin-top:10px;border-left:4px solid #fbbf24;font-size:0.9rem" class="kannada"></div>
</div>
<div class="glass">
<h2>📋 Queue List • ಸರತಿ ಪಟ್ಟಿ</h2>
<div id="queueList" style="max-height:380px;overflow-y:auto;margin-top:12px">Loading...</div>
<div style="margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:10px">
<button class="btn btn-purple" onclick="loadQueue()">🔄 Refresh</button>
<button class="btn" style="background:#334155" onclick="exportQueue()">📤 Export CSV</button>
</div>
</div>
</div>
<div class="glass" style="background:linear-gradient(135deg,rgba(56,189,248,0.15),rgba(59,130,246,0.12))">
<h2>🔑 Clinic Pro Only - Vercel Fixed</h2>
<p style="color:#cbd5e1;margin:10px 0">Only Clinic Pro Project • No Auto Fare • No Kirana • Focused • PAID ₹10k-15k</p>
<div style="margin-top:18px;display:grid;grid-template-columns:1fr 1fr;gap:12px">
<button class="btn btn-purple" onclick="testAPIs()">🧪 Test APIs</button>
<button class="btn" onclick="window.open('/api/health','_blank')">📄 /api/health</button>
</div>
<div id="apiResult" style="background:rgba(0,0,0,0.45);padding:14px;border-radius:14px;margin-top:14px;font-family:monospace;font-size:0.85rem;display:none;max-height:300px;overflow:auto"></div>
</div>
<script>
let tokens=[];let currentId=1;
async function loadQueue(){try{const res=await fetch('/api/tokens');const data=await res.json();tokens=data.queue||[];if(data.current)currentId=data.current;renderQueue();updateStats(data)}catch(e){tokens=[{id:1,name:"Ramesh Gowda",phone:"9876543210",age:45,symptom:"Fever",status:"current",time:"09:15 AM",fee:50},{id:2,name:"Lakshmi",phone:"9876543211",age:32,symptom:"Cough",status:"waiting",time:"09:18 AM",fee:50}];renderQueue()}}
function renderQueue(){const list=document.getElementById('queueList');if(tokens.length===0){list.innerHTML='<div style="text-align:center;color:#94a3b8;padding:20px">No tokens</div>';return}list.innerHTML=tokens.map(t=>`<div class="queue-item ${t.status==='current'?'current':''}"><div class="dot ${t.status==='current'?'dot-current':'dot-waiting'}"></div><div style="min-width:52px;height:52px;background:${t.status==='current'?'linear-gradient(135deg,#38bdf8,#3b82f6)':'#334155'};color:${t.status==='current'?'black':'white'};border-radius:14px;display:flex;align-items:center;justify-content:center;font-weight:900">#${t.id}</div><div style="flex:1"><div style="font-weight:800">${t.name}</div><div style="font-size:0.85rem;color:#94a3b8">${t.symptom} • ${t.time} • ${t.status}</div><div style="font-size:0.8rem;color:#94a3b8">📱 ${t.phone} • ₹${t.fee}</div></div></div>`).join('')}
function updateStats(data){document.getElementById('currentTokenDisplay').innerText='#'+(data.current||1);const curr=tokens.find(t=>t.id===data.current)||tokens[0];if(curr){document.getElementById('currentPatientDisplay').innerText=curr.name+' • '+curr.symptom+' • '+curr.time;document.getElementById('currentPhone').innerText='📱 '+curr.phone+' • Fee ₹'+curr.fee}document.getElementById('waitingCount').innerText=data.waiting||tokens.filter(t=>t.status==='waiting').length;document.getElementById('todayCount').innerText=data.today_patients||tokens.length;document.getElementById('revenueDisplay').innerText='₹'+(data.revenue||tokens.length*50)}
async function bookToken(){const name=document.getElementById('pName').value.trim();const phone=document.getElementById('pPhone').value.trim();const age=document.getElementById('pAge').value.trim();const symptom=document.getElementById('pSymptom').value.trim();const fee=document.getElementById('pFee').value||50;if(!name||!phone||!symptom){alert('Fill Name, Phone, Symptoms');return}const resultDiv=document.getElementById('bookResult');const aqDiv=document.getElementById('aqSymptomResult');resultDiv.style.display='block';resultDiv.innerHTML='<div style="background:rgba(59,130,246,0.12);padding:12px;border-radius:12px">⏳ Booking...</div>';try{const res=await fetch(`/api/tokens/book?name=${encodeURIComponent(name)}&phone=${encodeURIComponent(phone)}&age=${age}&symptom=${encodeURIComponent(symptom)}&fee=${fee}`);const data=await res.json();resultDiv.innerHTML=`<div style="background:rgba(34,197,94,0.12);padding:14px;border-radius:12px;border-left:4px solid #22c55e">✅ Token #${data.token_id||(tokens.length+1)} for ${name}!<br>📱 SMS to ${phone}<br>Waiting: ~${(data.waiting||tokens.length)*5} min</div>`;aqDiv.style.display='block';aqDiv.innerHTML='🤖 AQ 3.8 analyzing...';fetch(`/api/aq?symptom=${encodeURIComponent(symptom)}&name=${encodeURIComponent(name)}&age=${age}`).then(r=>r.json()).then(d=>{aqDiv.innerHTML=`<b>AQ 3.8:</b><br><br>${(d.response||d.fallback||'').substring(0,600)}`});loadQueue()}catch(e){const newId=tokens.length+1;tokens.push({id:newId,name,phone,age,symptom,status:'waiting',time:new Date().toLocaleTimeString(),fee});renderQueue();resultDiv.innerHTML=`<div style="background:rgba(34,197,94,0.12);padding:12px;border-radius:12px">✅ Token #${newId} Booked (Local)!</div>`}}
async function callNext(){const resultDiv=document.getElementById('actionResult');resultDiv.style.display='block';try{const res=await fetch('/api/tokens/next',{method:'POST'});const data=await res.json();resultDiv.innerHTML=`✅ Next: Token #${data.next||currentId+1} - ${data.name||'Next'}`;currentId=data.next||currentId+1;loadQueue()}catch(e){currentId++;document.getElementById('currentTokenDisplay').innerText='#'+currentId;resultDiv.innerHTML=`✅ Next: #${currentId} (Local)`}}
function markDone(){const resultDiv=document.getElementById('actionResult');resultDiv.style.display='block';resultDiv.innerHTML=`✅ Token #${currentId} Done • Next in 2 sec`;setTimeout(()=>{callNext()},1500)}
function resetQueue(){if(confirm('Reset queue?')){tokens=[];currentId=1;renderQueue();document.getElementById('actionResult').style.display='block';document.getElementById('actionResult').innerHTML='🔄 Queue reset'}}
function exportQueue(){const csv='ID,Name,Phone,Symptom,Status,Fee\n'+tokens.map(t=>`${t.id},${t.name},${t.phone},${t.symptom},${t.status},${t.fee}`).join('\n');const blob=new Blob([csv],{type:'text/csv'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='clinic-tokens.csv';a.click()}
async function testAPIs(){const resultDiv=document.getElementById('apiResult');resultDiv.style.display='block';resultDiv.innerHTML='Testing...<br><br>';const apis=['/','/api/health','/api/tokens','/api/aq?symptom=Fever'];for(let api of apis){try{const res=await fetch(api);const isJson=res.headers.get('content-type')?.includes('json');const data=isJson?await res.json():await res.text();const text=isJson?JSON.stringify(data).substring(0,150):'HTML OK';resultDiv.innerHTML+=`<div style="color:#22c55e;margin:6px 0;padding:6px;background:rgba(34,197,94,0.08);border-radius:8px">✅ ${api}<br>${text}...</div>`}catch(e){resultDiv.innerHTML+=`<div style="color:#ef4444">❌ ${api}</div>`}}}
window.onload=()=>{loadQueue()};
</script>
</body>
</html>
'''

def get_next_id():
    global TOKENS
    if not TOKENS:
        return 1
    return max(t["id"] for t in TOKENS) + 1

@app.route('/')
@app.route('/api')
@app.route('/api/')
@app.route('/api/index')
@app.route('/api/index/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/health')
@app.route('/api/health/')
def health():
    return jsonify({
        "status":"ok",
        "project":"Namma Clinic Pro - Token Queue Pro - ONLY Clinic Pro",
        "suite":"Clinic Pro Only - Day 6 - Vercel Only",
        "model":"3.8",
        "vercel":True,
        "clinic_only":True,
        "flask_app":"defined ✅",
        "not_found_fixed":"Fixed ✅",
        "aq_key_present":bool(AQ_API_KEY),
        "today_patients":len(TOKENS),
        "current":CURRENT_TOKEN,
        "waiting":len([t for t in TOKENS if t["status"]=="waiting"]),
        "revenue":sum(t["fee"] for t in TOKENS),
        "endpoints":["/","/api/index","/api/health","/api/tokens","/api/tokens/book","/api/tokens/next","/api/aq"],
        "price":"₹10k-15k per clinic + ₹500/month"
    })

@app.route('/api/tokens')
@app.route('/api/tokens/')
def tokens_api():
    global TOKENS, CURRENT_TOKEN
    waiting=len([t for t in TOKENS if t["status"]=="waiting"])
    return jsonify({"current":CURRENT_TOKEN,"waiting":waiting,"next":CURRENT_TOKEN+1,"revenue":sum(t["fee"] for t in TOKENS),"today_patients":len(TOKENS),"queue":TOKENS,"clinic_only":True})

@app.route('/api/tokens/book')
@app.route('/api/tokens/book/')
def book_token_api():
    global TOKENS, CURRENT_TOKEN
    name=request.args.get('name','Patient')
    phone=request.args.get('phone','9999999999')
    age=request.args.get('age','')
    symptom=request.args.get('symptom','General')
    fee=int(request.args.get('fee','50'))
    new_id=get_next_id()
    new_token={"id":new_id,"name":name,"phone":phone,"age":age,"symptom":symptom,"status":"waiting" if TOKENS else "current","time":datetime.now().strftime("%I:%M %p"),"fee":fee}
    TOKENS.append(new_token)
    if len(TOKENS)==1:
        CURRENT_TOKEN=new_id
    waiting=len([t for t in TOKENS if t["status"]=="waiting"])
    return jsonify({"success":True,"token_id":new_id,"id":new_id,"name":name,"waiting":waiting,"clinic_only":True})

@app.route('/api/tokens/next', methods=['GET','POST'])
@app.route('/api/tokens/next/', methods=['GET','POST'])
def next_token_api():
    global TOKENS, CURRENT_TOKEN
    for t in TOKENS:
        if t["id"]==CURRENT_TOKEN:
            t["status"]="done"
    waiting=[t for t in TOKENS if t["status"]=="waiting"]
    if waiting:
        nxt=waiting[0]
        nxt["status"]="current"
        CURRENT_TOKEN=nxt["id"]
        return jsonify({"success":True,"next":CURRENT_TOKEN,"name":nxt["name"],"current_token":nxt,"clinic_only":True})
    else:
        return jsonify({"success":True,"next":CURRENT_TOKEN,"message":"No more waiting","clinic_only":True})

@app.route('/api/aq')
@app.route('/api/aq/')
def aq_api():
    symptom=request.args.get('symptom','Fever')
    name=request.args.get('name','Patient')
    age=request.args.get('age','28')
    prompt=f"Clinic: Patient {name}, age {age}, symptom '{symptom}'. Give urgency, department, first question. Short."
    ai_response=call_aq_clinic(prompt)
    if ai_response:
        return jsonify({"symptom":symptom,"name":name,"response":ai_response,"aq_key_present":bool(AQ_API_KEY),"clinic_only":True})
    else:
        urgency="High" if any(x in symptom.lower() for x in ["chest pain","breath","unconscious","bleeding"]) else "Medium"
        return jsonify({"symptom":symptom,"fallback":f"{urgency} urgency - General Physician - Ask duration for {symptom}? Kannada: ಎಷ್ಟು ದಿನದಿಂದ {symptom}?","urgency":urgency,"department":"General Physician","aq_key_present":bool(AQ_API_KEY),"clinic_only":True})

@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('api/'):
        return jsonify({"error":f"API /{path} not found","hint":"Use /api/health , /api/tokens , /api/tokens/book , /api/aq","received_path":path,"clinic_only":True}),404
    else:
        return render_template_string(HTML_TEMPLATE)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Not Found - Clinic Pro Running","hint":"Use / , /api/index , /api/health , /api/tokens","clinic_only":True,"status":"Ready"}),404
