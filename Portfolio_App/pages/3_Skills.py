import streamlit as st
import base64

st.set_page_config(page_title="Skills | Aireen Joice Dulatre", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
:root{--ink:#0d0d0d;--cream:#f5f0e8;--accent:#e84d0e;--mid:#6b6b6b;--card:#ffffff;}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--ink);}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 3rem 4rem;max-width:1100px;margin:auto;}
h1,h2,h3{font-family:'Syne',sans-serif;}
section[data-testid="stSidebar"]{background-color:var(--ink);padding-top:2.5rem;}
section[data-testid="stSidebar"] *{color:var(--cream)!important;}

.page-header{padding:2.5rem 0 1.5rem;border-bottom:2px solid var(--ink);margin-bottom:2.5rem;}
.page-tag{font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-family:'Syne',sans-serif;font-weight:600;}
.page-header h1{font-size:3rem;font-weight:800;margin:.3rem 0 0;}

.sec-title{font-size:1.4rem;font-weight:700;font-family:'Syne',sans-serif;border-left:5px solid var(--accent);padding-left:.8rem;margin-bottom:1.5rem;margin-top:2rem;}

.skill-bar-wrap{margin-bottom:1.1rem;}
.skill-bar-header{display:flex;justify-content:space-between;margin-bottom:.3rem;}
.skill-bar-name{font-family:'Syne',sans-serif;font-size:.95rem;font-weight:600;}
.skill-bar-pct{font-size:.85rem;color:var(--accent);font-weight:700;}
.skill-bar-bg{background:#e0dcd4;border-radius:100px;height:8px;overflow:hidden;}
.skill-bar-fill{height:100%;border-radius:100px;background:var(--ink);transition:width 1s ease;}

.tool-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:.9rem;margin-bottom:2rem;}
.tool-chip{background:var(--card);border:1.5px solid #e0dcd4;border-radius:10px;padding:.85rem .7rem;text-align:center;font-family:'Syne',sans-serif;font-size:.82rem;font-weight:600;transition:transform .15s;color:var(--accent)}
.tool-chip:hover{transform:translateY(-3px);box-shadow:0 4px 16px rgba(0,0,0,.07);}
.tool-chip span{display:block;font-size:1.6rem;margin-bottom:.35rem; } 

.cert-card{background:var(--card);border:1.5px solid #e0dcd4;border-radius:14px;padding:1.2rem 1.4rem;display:flex;align-items:center;gap:1.2rem;margin-bottom:.9rem;}
.cert-icon{font-size:2.2rem;flex-shrink:0;}
.cert-name{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;}
.cert-issuer{font-size:.85rem;color:var(--accent);}
.cert-year{font-size:.8rem;color:var(--mid);font-weight:600;margin-top:.2rem;}

/* Override Streamlit slider accent */
.stSlider [data-baseweb="slider"] [role="slider"]{ background-color:var(--accent)!important; }
</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="page-header">
  <div class="page-tag">What I Know</div>
  <h1>Skills & Tools</h1>
</div>
""", unsafe_allow_html=True)

# ── Interactive skill finder ────────────────────────────────────────────────
st.markdown("### 🔍 Skill Explorer")
st.markdown("Use the slider to filter skills by proficiency level.")
min_level = st.slider("Minimum proficiency (%)", 0, 100, 60, step=5)

SKILLS = {
    "Languages & Frameworks": [
        ("Python",      95),
        ("JavaScript",  78),
        ("SQL",         85),
        ("HTML",  70),
        ("CSS",  70),
    ],
    "Data & ML": [
        ("Pandas / NumPy",   92),
        ("Scikit-learn",     85),
        ("Streamlit",        90),
    ],
    "Infrastructure & DevOps": [
        ("GitHub Actions",    82),
    ],
}

for cat, skills in SKILLS.items():
    visible = [(n, v) for n, v in skills if v >= min_level]
    if not visible:
        continue
    st.markdown(f'<div class="sec-title">{cat}</div>', unsafe_allow_html=True)
    for name, pct in visible:
        color = "#e84d0e" if pct >= 85 else "#13f186"
        st.markdown(f"""
        <div class="skill-bar-wrap">
          <div class="skill-bar-header">
            <span class="skill-bar-name">{name}</span>
            <span class="skill-bar-pct">{pct}%</span>
          </div>
          <div class="skill-bar-bg">
            <div class="skill-bar-fill" style="width:{pct}%;background:{color};"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)




    # ── FOOTER ──────────────────────────────────────────────────
st.markdown("""
<br><br>
<center style="color:gray; font-size:0.9rem;">
© 2026 Aireen Joice Dulatre • Portfolio 🚀
</center>
""", unsafe_allow_html=True)

