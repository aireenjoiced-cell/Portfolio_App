import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()
img_base64 = get_base64_image("Portfolio_App/pages/joice.jpg")  # change to your file path
st.set_page_config(page_title="About | Aireen Joice Dulatre", page_icon="👤", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
:root { --ink:#0d0d0d; --cream:#f5f0e8; --accent:#e84d0e; --mid:#6b6b6b; --card:#ffffff; }
html,body,[class*="css"]{ font-family:'DM Sans',sans-serif; background:var(--cream); color:var(--ink); }
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 3rem 4rem;max-width:1100px;margin:auto;}
h1,h2,h3{font-family:'Syne',sans-serif;}
section[data-testid="stSidebar"]{background-color:var(--ink);padding-top:2.5rem;}
section[data-testid="stSidebar"] *{color:var(--cream)!important;}

.page-header{padding:2.5rem 0 1.5rem;border-bottom:2px solid var(--ink);margin-bottom:2.5rem;}
.page-tag{font-size:.8rem;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-family:'Syne',sans-serif;font-weight:600;}
.page-header h1{font-size:3rem;font-weight:800;margin:.3rem 0 0;}



.about-grid{display:grid;grid-template-columns:4fr 5fr;gap:2rem;align-items:start;margin-bottom:3rem;width:100%;}
@media(max-width:768px){.about-grid{grid-template-columns:1fr;}}
.avatar-box{background:var(--ink);border-radius:20px;padding:2rem;text-align:center;color:var(--cream);}
.avatar-emoji{font-size:6rem;display:block;margin-bottom:1rem;}
.avatar-name{font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:700;}
.avatar-role{color:#aaa;font-size:.95rem;margin-top:.3rem;}
.avatar-location{margin-top:.8rem;font-size:.85rem;color:#888;}
.badge-row{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.2rem;}
.badge{background:#1e1e1e;padding:.3rem .8rem;border-radius:100px;font-size:.8rem;color:#ddd;}

.bio-section h2{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;border-left:5px solid var(--accent);padding-left:.8rem;margin-bottom:1rem;}
.bio-section p{line-height:1.7;color:green;font-size:1rem;}

.val-grid{display:grid;
  grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1rem; margin-bottom:3rem;
}

/* Flip Card Container */
.flip-card{
  perspective:1000px;
}

/* Inner wrapper */
.flip-inner{position:relative;width:100%;height:150px;text-align:center;transition:transform 0.6s;transform-style:preserve-3d;
  cursor:pointer;
}

/* Flip on click */

.flip-card:hover .flip-inner{transform:rotateY(180deg);}

.click-text{margin-top: 0.5rem;font-size: 0.8rem;color: #e84d0e;font-weight: 600;opacity: 0.8;transition: 0.3s;}

/* Front & Back */
.flip-front, .flip-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;border:1.5px solid #e0dcd4;border-radius:14px;padding:1.4rem 1.2rem;background:var(--card);
}

/* Back side */
.flip-back{transform:rotateY(180deg);}
.avatar-img{width:150px;height:150px;border-radius:100%;object-fit:cover;margin-bottom:0.8rem;border:3px solid #e84d0e;}
            

/* Your existing styles */
.val-icon{font-size:1.8rem;margin-bottom:.6rem;}
.val-title{font-family:'Syne',sans-serif;font-size:.95rem;font-weight:700;margin-bottom:.3rem;color:black;}
.val-desc{font-size:.85rem;color:black;line-height:1.5;}
.edu-item{display:flex;gap:1.2rem;align-items:flex-start;padding:1.2rem 0;border-bottom:1px solid #e0dcd4;}
.edu-item:last-child{border-bottom:none;}
.edu-icon{font-size:2rem;flex-shrink:0;}
.edu-degree{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;}
.edu-school{font-size:.9rem;color:var(--mid);}
.edu-year{font-size:.8rem;color:var(--accent);font-weight:600;margin-top:.2rem;}

.interest-row{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:.5rem;}
.interest-chip{background:var(--ink);color:var(--cream);padding:.45rem 1rem;border-radius:100px;font-size:.85rem;font-family:'Syne',sans-serif;font-weight:600;}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="page-header">
  <div class="page-tag">Who I Am</div>
  <h1>About Me</h1>
</div>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="about-grid">
 <div class="avatar-box">
  <img src="data:Portfolio_App/pages/joice.jpg;base64,{img_base64}" class="avatar-img"/>
  <div class="avatar-name">Aireen Joice Dulatre</div>
  <div class="avatar-role">Computer Science Student</div>
  <div class="avatar-location">📍 Tagpu, Mandaon, Masbate, Philippines</div>
  <div class="badge-row">
    <span class="badge">Python</span>
    <span class="badge">Html</span>
    <span class="badge">Css</span>
    <span class="badge">C++</span>
  </div>
</div>
  <div class="bio-section">
    <h2>My Story</h2>
    <p>
       I started my college journey without any knowledge about computers, and I often felt lost in my major subjects. However, whenever we had activities, I was able to understand things better, especially when writing small Python scripts to automate homework tasks.
    <p>
      Over the past two years of studying Computer Science, I have grown a lot. Now, I can create my own website or portfolio, and I’ve quickly fallen in love with the idea that code can solve real-world problems.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div style="font-family:\'Syne\',sans-serif;font-size:1.5rem;font-weight:700;border-left:5px solid #e84d0e;padding-left:.8rem;margin-bottom:1.2rem;">My Values</div>', unsafe_allow_html=True)

st.markdown("""
<div class="val-grid">

  <div class="flip-card">
    <div class="flip-inner">
      <div class="flip-front">
        <div class="val-icon">🔬</div>
        <div class="val-title">Curiosity First</div>
        <p class="click-text">Click me</p>
      </div>
      <div class="flip-back">
        <div class="val-desc">I dive deep before I build. Understanding the "why" leads to better solutions.</div>
      </div>
    </div>
  </div>

  <div class="flip-card">
    <div class="flip-inner">
      <div class="flip-front">
        <div class="val-icon">🤝"</div>
        <div class="val-title">Empathy in Code</div>
        <p class="click-text">Click me</p>
      </div>
      <div class="flip-back">
        <div class="val-desc">Good software is written for humans. I design with the end user in mind, always.</div>
      </div>
    </div>
  </div>

  <div class="flip-card">
    <div class="flip-inner">
      <div class="flip-front">
        <div class="val-icon">⚡</div>
        <div class="val-title">Ship & Iterate</div>
        <p class="click-text">Click me</p>
      </div>
      <div class="flip-back">
        <div class="val-desc">Perfect is the enemy of good. I ship early, gather feedback, and improve fast.</div>
      </div>
    </div>
  </div>

  <div class="flip-card">
    <div class="flip-inner">
      <div class="flip-front">
        <div class="val-icon">📚</div>
        <div class="val-title">Never Stop Learning</div>
        <p class="click-text">Click me</p>
      </div>
      <div class="flip-back">
        <div class="val-desc">The tech landscape changes daily. I dedicate time every week to learning something new.</div>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)



st.markdown('<div style="font-family:\'Syne\',sans-serif;font-size:1.5rem;font-weight:700;border-left:5px solid #e84d0e;padding-left:.8rem;margin-bottom:1rem;">Education</div>', unsafe_allow_html=True)
st.markdown("""
<div>
  <div class="edu-item">
    <div class="edu-icon">🎓</div>
    <div>
      <div class="edu-degree">B.S. Computer Science</div>
      <div class="edu-school">Dr. Emelio B. Estipona Memorial State College of Agriculture and Technology</div>
      <div class="edu-year">2023 – present </div>
    </div>
  </div>
  
""", unsafe_allow_html=True)

st.markdown('<div style="font-family:\'Syne\',sans-serif;font-size:1.5rem;font-weight:700;border-left:5px solid #e84d0e;padding-left:.8rem;margin:.5rem 0 .8rem;">Interests & Hobbies</div>', unsafe_allow_html=True)
st.markdown("""
<div class="interest-row">
  <span class="interest-chip">🧗 Drawing</span>
  <span class="interest-chip">📷 Photography</span>
  <span class="interest-chip">☕ Badminton</span>
  <span class="interest-chip">🌏 Travel</span>
  <span class="interest-chip">📖 Sci-Fi Novels</span>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ──────────────────────────────────────────────────
st.markdown("""
<br><br>
<center style="color:gray; font-size:0.9rem;">
© 2026 Aireen Joice Dulatre • Portfolio 🚀
</center>
""", unsafe_allow_html=True)
