import streamlit as st
import re
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="Contact | Aireen Joice Dulatre", page_icon="✉️", layout="wide")

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

.contact-grid{display:grid;grid-template-columns:1fr 1.6fr;gap:3rem;align-items:start;}
@media(max-width:700px){.contact-grid{grid-template-columns:1fr;}}

.info-card{background:var(--ink);color:var(--cream);padding:2rem;border-radius:18px;}
.info-card h3{font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:700;margin-bottom:1.2rem;}
.contact-item{display:flex;gap:.9rem;align-items:flex-start;margin-bottom:1.2rem;}
.c-icon{font-size:1.4rem;flex-shrink:0;margin-top:.1rem;}
.c-label{font-size:.75rem;color:#888;font-family:'Syne',sans-serif;font-weight:600;letter-spacing:.1em;text-transform:uppercase;}
.c-value{font-size:.95rem;margin-top:.1rem;}
.c-value a{color:var(--cream);text-decoration:none;}

.avail-badge{display:inline-flex;align-items:center;gap:.5rem;background:#1a3a1a;color:#5de85d;padding:.5rem 1rem;border-radius:100px;font-size:.82rem;font-family:'Syne',sans-serif;font-weight:700;margin-top:1.5rem;}
.avail-dot{width:8px;height:8px;border-radius:50%;background:#5de85d;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.4;}}

.form-label{font-family:'Syne',sans-serif;font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.3rem;display:block;}

/* Streamlit input overrides */
.stTextInput input, .stTextArea textarea, .stSelectbox select{
    background:var(--card)!important;
    border:1.5px solid #ccc8be!important;
    border-radius:10px!important;
    font-family:'DM Sans',sans-serif!important;
    color:var(--ink)!important;
}
.stTextInput input:focus, .stTextArea textarea:focus{border-color:var(--accent)!important;}

div.stButton > button{
    background:var(--ink);
    color:var(--cream);
    font-family:'Syne',sans-serif;
    font-weight:700;
    font-size:.95rem;
    border:none;
    border-radius:100px;
    padding:.7rem 2rem;
    width:100%;
    transition:background .2s;
}
div.stButton > button:hover{background:var(--accent);}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
  <div class="page-tag">Say Hello</div>
  <h1>Contact Me</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="contact-grid">', unsafe_allow_html=True)
col_info, col_form = st.columns([1, 1.6])

with col_info:
    st.markdown("""
    <div class="info-card">
      <h3>Let's Connect</h3>
      <div class="contact-item">
        <div class="c-icon">📧</div>
        <div>
          <div class="c-label">Email</div>
          <div class="c-value"><a href="mailto:aireenjoiced@gmail.com">aireenjoiced@gmail.com</a></div>
        </div>
      </div>
      <div class="contact-item">
        <div class="c-icon">🐙</div>
        <div>
          <div class="c-label">GitHub</div>
          <div class="c-value"> <a href="https://github.com/aireenjoiced-cell" target="_blank">https://github.com/aireenjoiced-cell</a></div>
        </div>
      </div>
      <div class="contact-item">
      </div>
      <div class="contact-item">
        <div class="c-icon">🎯</div>
        <div>
          <div class="c-label">Facebook</div>
          <div class="c-value"> <a href="https://www.facebook.com/joice.not.aireen" target="_blank">
        https://www.facebook.com/joice.not.aireen
      </a></div>
        </div>
      </div>
      <div class="contact-item">
        <div class="c-icon">📍</div>
        <div>
          <div class="c-label">Location</div>
          <div class="c-value">Tagpu, Mandaon, Masbate, Philippines</div>
        </div>
      </div>
      <div class="avail-badge"><span class="avail-dot"></span>Available for Projects</div>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    st.markdown("#### Send a Message")
    st.markdown("Fill out the form below and I'll get back to you within 24 hours.")

    with st.form("contact_form", clear_on_submit=True):
        name     = st.text_input("Your Name *", placeholder="Juan dela Cruz")
        email    = st.text_input("Your Email *", placeholder="juan@example.com")
        subject  = st.selectbox("Subject *", [
            "— Select a topic —",
            "💼 Freelance / Project Inquiry",
            "🤝 Collaboration Opportunity",
            "💡 Open Source Contribution",
            "💬 Just Saying Hi",
            "🐛 Bug Report",
            "Other",
        ])
        message  = st.text_area("Message *", placeholder="Tell me about your project or idea...", height=160)
        agree    = st.checkbox("I agree to be contacted by email regarding my enquiry.")
        submitted = st.form_submit_button("Send Message 🚀")

        if submitted:
            errors = []
            if not name.strip():
                errors.append("Name is required.")
            if not email.strip() or not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
                errors.append("A valid email is required.")
            if subject == "— Select a topic —":
                errors.append("Please select a subject.")
            if not message.strip() or len(message.strip()) < 20:
                errors.append("Message must be at least 20 characters.")
            if not agree:
                errors.append("Please agree to be contacted.")

            if errors:
                for e in errors:
                    st.error(e)
            else:
                ts = datetime.now().strftime("%B %d, %Y at %I:%M %p")
                st.success(f"""
                ✅ **Message sent successfully!**

                Thank you **{name}** — I've received your message about *"{subject}"* and will reply to **{email}** within 24 hours.

                _(Submitted on {ts})_
                """)

st.markdown("</div>", unsafe_allow_html=True)

# ── FAQ ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("#### 🙋 Frequently Asked Questions")

faqs = [
    ("Are you available for freelance work?",
     "Yes! I'm open to freelance projects, especially in backend development, data engineering, and ML solutions. Feel free to reach out with your requirements."),
    ("What is your typical project timeline?",
     "It depends on scope. Small apps take 2–4 weeks; larger platforms 2–4 months. I always provide a detailed estimate after initial discussions."),
    ("Do you work with international clients?",
     "Absolutely. I've worked with clients across SEA, Australia, and the US. I'm flexible with time zones."),
    ("What technologies do you prefer?",
     "Python ecosystem for backend/data, React for frontend. I'm also comfortable picking up new stacks based on project needs."),
]

for q, a in faqs:
    with st.expander(f"**{q}**"):
        st.write(a)
# ── FOOTER ──────────────────────────────────────────────────
st.markdown("""
<br><br>
<center style="color:gray; font-size:0.9rem;">
© 2026 Aireen Joice Dulatre • Portfolio 🚀
</center>
""", unsafe_allow_html=True)
