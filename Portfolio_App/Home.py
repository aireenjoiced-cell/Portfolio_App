import streamlit as st

st.set_page_config(
    page_title="Aireen Joice Dulatre | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --ink:    #0d0d0d;
    --cream:  #f5f0e8;
    --accent: #e84d0e;
    --mid:    #6b6b6b;
    --card:   #ffffff;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream);
    color: var(--ink);
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1100px; margin: auto; }

h1, h2, h3 { font-family: 'Syne', sans-serif; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: var(--ink);
    padding-top: 2.5rem;
}
section[data-testid="stSidebar"] * { color: var(--cream) !important; }
section[data-testid="stSidebar"] .stRadio label {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    letter-spacing: .05em;
}

/* ── Hero ── */
.hero {
    display: flex;
    flex-direction: column;
    gap: .4rem;
    padding: 3.5rem 0 2.5rem;
    border-bottom: 2px solid var(--ink);
    margin-bottom: 3rem;
}
.hero-tag {
    font-size: .85rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--accent);
    font-family: 'Syne', sans-serif;
    font-weight: 600;
}
.hero h1 {
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 800;
    line-height: 1.05;
    margin: 0;
}
.hero-sub {
    font-size: 1.15rem;
    color: var(--mid);
    max-width: 560px;
    margin-top: .6rem;
    line-height: 1.6;
}

.hero-accent { color: var(--accent); }

/* ── Stat pills ── */
.stat-row { display: flex; gap: 1.2rem; flex-wrap: wrap; margin-top: 2rem; }
.stat-pill {
    background: var(--ink);
    color: var(--cream);
    padding: .55rem 1.3rem;
    border-radius: 100px;
    font-family: 'Syne', sans-serif;
    font-size: .9rem;
    font-weight: 600;
}
.stat-pill span { color: var(--accent); margin-right: .4rem; }

/* ── Section header ── */
.sec-title {
    font-size: 1.7rem;
    font-weight: 700;
    font-family: 'Syne', sans-serif;
    border-left: 5px solid var(--accent);
    padding-left: .9rem;
    margin-bottom: 1.5rem;
}

/* ── Skill cards ── */
.skill-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px,1fr)); gap: 1rem; margin-bottom: 3rem; }
.skill-card {
    background: var(--card);
    border: 1.5px solid #e0dcd4;
    border-radius: 12px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: transform .2s, box-shadow .2s;
}
.skill-card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,.08); }
.skill-icon { font-size: 2rem; margin-bottom: .5rem; }
.skill-name { font-family: 'Syne', sans-serif; font-size: .9rem; font-weight: 600; }
.skill-level { font-size: .75rem; color: var(--mid); margin-top: .2rem; }

/* ── Timeline ── */
.timeline { position: relative; padding-left: 1.8rem; margin-bottom: 3rem; }
.timeline::before {
    content: '';
    position: absolute;
    left: 0; top: 6px; bottom: 0;
    width: 2px;
    background: var(--ink);
}


</style>
""", unsafe_allow_html=True)


# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">Welcome</div>
  <h1>Hi, I'm <span class="hero-accent">Aireen Joice Dulatre</span> <br>I build things that matter.</h1>
  <p class="hero-sub">
   A BS Computer Science student passionate about building modern web and mobile applications,
    data-driven systems, and solving real-world problems.
  </p>
  <div class="stat-row">
    <div class="stat-pill"><span>3yr</span>BSCS Student</div>
    <div class="stat-pill"><span>6</span>Projects </div>
    <div class="stat-pill"><span>1yr</span>Python</div>
   
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

