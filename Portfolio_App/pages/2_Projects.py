import streamlit as st

st.set_page_config(page_title="Projects | Aireen Joice Dulatre", page_icon="💼", layout="wide")


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

.proj-card{background:var(--card);border:1.5px solid #e0dcd4;border-radius:16px;padding:1.8rem;margin-bottom:1.5rem;transition:box-shadow .2s;}
.proj-card:hover{box-shadow:0 8px 32px rgba(0,0,0,.09);}
.proj-header{display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:.5rem;margin-bottom:.8rem;}
.proj-title{font-family:'Syne',sans-serif;font-size:1.25rem;font-weight:700;color: green;}
.proj-year{font-size:.8rem;color:var(--accent);font-family:'Syne',sans-serif;font-weight:700;letter-spacing:.08em;}
.proj-desc{font-size:.95rem;color:#333;line-height:1.65;margin-bottom:1rem;}
.tag-row{display:flex;flex-wrap:wrap;gap:.5rem;}
.tag{background:#f0ebe0;color:var(--ink);padding:.25rem .75rem;border-radius:100px;font-size:.78rem;font-family:'Syne',sans-serif;font-weight:600;}
.tag-highlight{background:var(--ink);color:var(--cream);}
.proj-links{margin-top:1rem;display:flex;gap:.8rem;}
.proj-link{display:inline-flex;align-items:center;gap:.3rem;font-size:.85rem;font-family:'Syne',sans-serif;font-weight:600;color:var(--ink);text-decoration:none;padding:.4rem .9rem;border:1.5px solid var(--ink);border-radius:100px;transition:background .2s,color .2s;}
.proj-link:hover{background:var(--ink);color:var(--cream);}
.featured-banner{background:var(--accent);color:#fff;font-size:.72rem;font-family:'Syne',sans-serif;font-weight:700;padding:.2rem .65rem;border-radius:100px;letter-spacing:.05em;}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="page-header">
  <div class="page-tag">What I've Built</div>
  <h1>Projects</h1>
</div>
""", unsafe_allow_html=True)

# ── Filter controls ──────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "Student Attendance Tracker",
        "year": "2026",
        "desc": "Used to record, monitor, and manage student attendance in schools or universities. To make attendance faster and easier and Reduce manual errors.",
        "tags": ["Python", ],
        "category": " Attendance ",
        "featured": True,
    },
    {
        "title": "Teachers Day Card Letter",
        "year": "2025",
        "desc": "This our last year activity to express our appreciation, gratitude, and respect for their hard work and dedication. ",
        "tags": ["Html","CSS"],
        "category": " Card",
        "featured": True,
        "github": "https://aireenjoiced-cell.github.io/Teacher-Day-Card/",
        "demo": None,
    },
    {
        "title": "Streamlit Basic Calculator",
        "year": "2026",
        "desc": "I create a basic calculator for our activty to perform mathematical computations quickly and accurately.Interactive Streamlit.",
        "tags": ["Streamlit", "Python"],
        "category": "Calculator",
        "featured": True,
        
    },
    {
        "title": "My porfolio Website",
        "year": "2024",
        "desc": "I create my website to describe my self. While exploring in canva AI",
        "tags": [ "Python"],
        "category": "Portfolio",
        "featured": True,
        "github":"https://aireenjoiced-cell.github.io/PERSONAL_WEBSITE/",
        
    },
    {
        "title": "TricAlert: Report and Complaint",
        "year": "2026",
        "desc": "This is my new project, creating our application for the commuters of Aroroy to easily report and complaint to the tricycle drivers.",
        "tags": ["Andriod Studio","Mysql"],
        "category": "TricAlert",
        "featured": True,
        
        
    },
    {
        "title": "Streamlit/Machine Learning",
        "year": "2026",
        "desc": "This my upcoming activity to fulfill one of our activity.",
        "tags": ["Python", "Streamlit"],
        "category": "Live Detection",
        "featured": True    
    },
]

all_cats = ["All"] + sorted(set(p["category"] for p in PROJECTS))
col_f, col_sort = st.columns([3, 1])
with col_f:
    cat_filter = st.selectbox("Filter by category", all_cats, label_visibility="collapsed")
with col_sort:
    featured_only = st.toggle("⭐ Featured only", value=False)

st.markdown("---")

filtered = PROJECTS
if cat_filter != "All":
    filtered = [p for p in filtered if p["category"] == cat_filter]
if featured_only:
    filtered = [p for p in filtered if p["featured"]]

st.markdown(f"<p style='color:var(--mid);font-size:.9rem;margin-bottom:1.5rem;'>Showing <strong>{len(filtered)}</strong> project(s)</p>", unsafe_allow_html=True)

for p in filtered:
    featured_html = '<span class="featured-banner">⭐ Featured</span>' if p["featured"] else ""
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    links = ""
    if p.get("github"):
        links += f'<a class="proj-link" href="{p["github"]}">⌥ GitHub</a>'
    if p.get("demo"):
        links += f'<a class="proj-link" href="{p["demo"]}">↗ Live Demo</a>'
    st.markdown(f"""
    <div class="proj-card">
      <div class="proj-header">
        <span class="proj-title">{p["title"]}</span>
        <span style="display:flex;gap:.5rem;align-items:center;">
          {featured_html}
          <span class="proj-year">{p["year"]}</span>
        </span>
      </div>
      <div style="margin-bottom:.7rem;">
        <span class="tag tag-highlight">{p["category"]}</span>
      </div>
      <p class="proj-desc">{p["desc"]}</p>
      <div class="tag-row">{tags_html}</div>
      <div class="proj-links">{links}</div>
    </div>
    """, unsafe_allow_html=True)


if not filtered:
    st.info("No projects match the selected filters. Try removing some filters!")



# ── FOOTER ──────────────────────────────────────────────────
st.markdown("""
<br><br>
<center style="color:gray; font-size:0.9rem;">
© 2026 Aireen Joice Dulatre • Portfolio 🚀
</center>
""", unsafe_allow_html=True)
