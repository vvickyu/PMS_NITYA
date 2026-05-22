import streamlit as st
from datetime import date

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Nitya VFX — Project Manager",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS  (cinematic dark / gold theme)
# ─────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=JetBrains+Mono:wght@300;400;500;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet"/>

<style>
/* ── ROOT VARS ── */
:root {
  --gold:       #C9A84C;
  --gold-bright:#E8C96A;
  --gold-dim:   #7A6230;
  --gold-pale:  rgba(201,168,76,0.08);
  --ink:        #080A0E;
  --surface:    #0E1118;
  --surface2:   #141720;
  --border:     rgba(201,168,76,0.18);
  --border2:    rgba(255,255,255,0.07);
  --text:       #F0EDE4;
  --text-mid:   #9A9486;
  --text-dim:   #5C5849;
  --red:        #E05252;
  --green:      #52B788;
  --amber:      #E8A838;
}

/* ── GLOBAL RESETS ── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background: var(--ink) !important;
  color: var(--text) !important;
  font-family: 'Outfit', sans-serif !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 0.5px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-mid) !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 26px !important;
  font-weight: 600 !important;
  color: var(--gold) !important;
  letter-spacing: 0.04em;
  margin-bottom: 2px;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 9px !important;
  color: var(--text-dim) !important;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

/* ── SIDEBAR RADIO (nav) ── */
[data-testid="stSidebar"] .stRadio > label {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 10px !important;
  color: var(--text-dim) !important;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-bottom: 4px;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  font-family: 'Outfit', sans-serif !important;
  font-size: 13px !important;
  color: var(--text-mid) !important;
  padding: 8px 0 !important;
  border-left: 2px solid transparent;
  padding-left: 8px !important;
  transition: color 0.15s;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  color: var(--gold) !important;
  border-left-color: var(--gold) !important;
  background: var(--gold-pale);
  border-radius: 0 4px 4px 0;
}

/* ── MAIN CONTENT AREA ── */
[data-testid="stMainBlockContainer"] {
  background: var(--ink) !important;
  padding: 2rem 2.5rem !important;
}

/* ── HEADINGS ── */
h1, h2, h3 {
  font-family: 'Cormorant Garamond', serif !important;
  color: var(--text) !important;
}

/* ── INPUTS ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
  background: var(--surface) !important;
  border: 0.5px solid var(--border) !important;
  color: var(--text) !important;
  font-family: 'Outfit', sans-serif !important;
  border-radius: 0 !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 1px var(--gold) !important;
}
.stTextInput label, .stTextArea label, .stSlider label,
.stSelectbox label {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 10px !important;
  color: var(--gold) !important;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

/* ── SLIDER ── */
.stSlider [data-baseweb="slider"] div[data-testid="stThumbValue"] {
  background: var(--gold) !important;
  color: var(--ink) !important;
  font-family: 'JetBrains Mono', monospace !important;
}
.stSlider [role="slider"] { background: var(--gold) !important; }

/* ── BUTTONS ── */
.stButton > button {
  background: var(--gold) !important;
  color: var(--ink) !important;
  border: none !important;
  border-radius: 0 !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  padding: 10px 24px !important;
  transition: background 0.2s !important;
}
.stButton > button:hover {
  background: var(--gold-bright) !important;
  color: var(--ink) !important;
}

/* ── SELECTBOX ── */
.stSelectbox > div > div {
  background: var(--surface) !important;
  border: 0.5px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 0 !important;
}

/* ── SUCCESS / INFO / WARNING ── */
.stAlert { border-radius: 0 !important; }
[data-baseweb="notification"] {
  background: var(--surface2) !important;
  border-left: 3px solid var(--gold) !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 12px !important;
}

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; border-width: 0.5px !important; }

/* ── METRIC ── */
[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 0.5px solid var(--border) !important;
  padding: 20px 24px !important;
}
[data-testid="stMetricLabel"] {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 9px !important;
  color: var(--text-dim) !important;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
[data-testid="stMetricValue"] {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 36px !important;
  color: var(--gold) !important;
  font-weight: 600 !important;
}

/* ── DATAFRAME / TABLE ── */
[data-testid="stDataFrame"] { border: 0.5px solid var(--border) !important; }
.dvn-scroller { background: var(--surface) !important; }

/* ── EXPANDER ── */
.streamlit-expanderHeader {
  background: var(--surface2) !important;
  border: 0.5px solid var(--border) !important;
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 16px !important;
  color: var(--text) !important;
  border-radius: 0 !important;
}
.streamlit-expanderContent {
  background: var(--surface) !important;
  border: 0.5px solid var(--border) !important;
  border-top: none !important;
}

/* ── CUSTOM CARD BLOCKS ── */
.nvfx-card {
  background: var(--surface);
  border: 0.5px solid rgba(255,255,255,0.07);
  padding: 20px 22px;
  margin-bottom: 10px;
  position: relative;
  transition: border-color 0.2s;
}
.nvfx-card:hover { border-color: var(--border); }
.nvfx-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1.5px;
  background: var(--gold);
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.3s;
}
.nvfx-card:hover::before { transform: scaleX(1); }

.card-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 20px; font-weight: 600;
  color: var(--text); margin-bottom: 4px;
}
.card-desc { font-size: 13px; color: var(--text-mid); font-weight: 300; margin-bottom: 10px; }

.pill {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px; padding: 3px 10px;
  border: 0.5px solid; letter-spacing: 0.06em;
  margin-right: 4px; margin-top: 4px;
}
.pill-amber { border-color: #E8A838; color: #E8A838; background: rgba(232,168,56,0.08); }
.pill-green { border-color: #52B788; color: #52B788; background: rgba(82,183,136,0.08); }
.pill-red   { border-color: #E05252; color: #E05252; background: rgba(224,82,82,0.08); }
.pill-dim   { border-color: #7A6230; color: #7A6230; }
.pill-gold  { border-color: #C9A84C; color: #C9A84C; background: rgba(201,168,76,0.08); }

.artist-card {
  background: var(--surface);
  border: 0.5px solid rgba(255,255,255,0.07);
  padding: 16px 20px;
  display: flex; align-items: center; gap: 16px;
  margin-bottom: 8px;
}
.avatar {
  width: 44px; height: 44px;
  border: 0.5px solid var(--gold);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Cormorant Garamond', serif;
  font-size: 17px; font-weight: 600; color: var(--gold);
  flex-shrink: 0; background: var(--gold-pale);
}
.artist-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 19px; font-weight: 600; color: var(--text);
}
.artist-role { font-size: 12px; color: var(--text-mid); font-weight: 300; }
.artist-email {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px; color: var(--text-dim); margin-top: 2px;
}

.hist-item {
  display: flex; gap: 14px;
  padding: 10px 0;
  border-bottom: 0.5px solid rgba(255,255,255,0.06);
}
.hist-date {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px; color: var(--gold-dim);
  flex-shrink: 0; margin-top: 2px; min-width: 70px;
}
.hist-note { font-size: 12px; color: var(--text-mid); font-weight: 300; }

.page-header {
  border-bottom: 0.5px solid rgba(201,168,76,0.18);
  padding-bottom: 16px; margin-bottom: 24px;
}
.page-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 36px; font-weight: 600;
  color: var(--text); line-height: 1;
}
.page-sub {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px; color: var(--text-dim);
  letter-spacing: 0.08em; margin-top: 4px;
}

.prio-bar { display: flex; gap: 3px; }
.pb { width: 16px; height: 4px; }
.pb-on  { background: var(--gold); }
.pb-off { background: var(--surface2); border: 0.5px solid rgba(255,255,255,0.06); }

.section-divider {
  border: none; border-top: 0.5px solid rgba(201,168,76,0.15);
  margin: 32px 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SAMPLE DATA  (in-memory; replace with DB)
# ─────────────────────────────────────────────
MAX_HISTORY_ITEMS = 15

if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "id": "alpha",
            "name": "Alpha Feature Film",
            "description": "Wide-release VFX — 240 shots across 3 sequences. Delivery Q3.",
            "artists": ["Jamie Lin", "Priya Mehta", "Rohan Das"],
        },
        {
            "id": "beta",
            "name": "Beta Episodic",
            "description": "8-episode series. Compositing and creature FX pipeline.",
            "artists": ["Carlos R.", "Ananya K."],
        },
        {
            "id": "gamma",
            "name": "Gamma Commercial",
            "description": "30-second spot. Product viz + environment extension.",
            "artists": ["Priya Mehta"],
        },
    ]

if "shots" not in st.session_state:
    st.session_state.shots = [
        {"id": "sh010", "code": "SH_010", "name": "Hero Explosion",    "project": "alpha", "status": "In Progress", "priority": 4, "artist": "Jamie Lin",  "frames": "1001–1120", "folder": "/projects/alpha/sh_010", "notes": "Check lens flare comp on frame 1080. Director wants extra motion blur on debris elements.", "history": [{"date": "2026-05-22", "note": "Lens flare comp updated per supervisor feedback."},{"date": "2026-05-21", "note": "Motion blur pass applied to debris layer."},{"date": "2026-05-20", "note": "Grading pass aligned to sequence LUT v3."},{"date": "2026-05-19", "note": "Initial comp delivery to internal review."}]},
        {"id": "sh020", "code": "SH_020", "name": "City Skyline Ext.", "project": "alpha", "status": "Done",        "priority": 2, "artist": "Priya Mehta", "frames": "1200–1340", "folder": "/projects/alpha/sh_020", "notes": "", "history": []},
        {"id": "sh030", "code": "SH_030", "name": "Creature Attack",   "project": "alpha", "status": "Review",      "priority": 5, "artist": "Rohan Das",   "frames": "1400–1520", "folder": "/projects/alpha/sh_030", "notes": "Director review pending.", "history": []},
        {"id": "sh040", "code": "SH_040", "name": "Portal Open",       "project": "alpha", "status": "Hold",        "priority": 1, "artist": "Jamie Lin",  "frames": "1600–1680", "folder": "/projects/alpha/sh_040", "notes": "", "history": []},
        {"id": "sh050", "code": "SH_050", "name": "Rain Simulation",   "project": "alpha", "status": "In Progress", "priority": 3, "artist": "Ananya K.",  "frames": "1700–1820", "folder": "/projects/alpha/sh_050", "notes": "", "history": []},
        {"id": "sh060", "code": "SH_060", "name": "Final Wide",        "project": "alpha", "status": "Done",        "priority": 4, "artist": "Carlos R.",  "frames": "1900–2020", "folder": "/projects/alpha/sh_060", "notes": "", "history": []},
    ]

if "artists" not in st.session_state:
    st.session_state.artists = [
        {"id": "jl", "name": "Jamie Lin",  "initials": "JL", "role": "Senior Compositor",  "email": "jamie.lin@nityavfx.com",  "color": "#C9A84C"},
        {"id": "pm", "name": "Priya Mehta","initials": "PM", "role": "FX Artist",           "email": "priya.mehta@nityavfx.com","color": "#52B788"},
        {"id": "rd", "name": "Rohan Das",  "initials": "RD", "role": "Creature FX Lead",    "email": "rohan.das@nityavfx.com",  "color": "#E8A838"},
        {"id": "cr", "name": "Carlos R.",  "initials": "CR", "role": "Lighter / LookDev",   "email": "carlos.r@nityavfx.com",   "color": "#E05252"},
        {"id": "ak", "name": "Ananya K.",  "initials": "AK", "role": "FX / Simulation",     "email": "ananya.k@nityavfx.com",   "color": "#9C88E0"},
    ]

if "current_shot_id" not in st.session_state:
    st.session_state.current_shot_id = "sh010"

if "current_project_id" not in st.session_state:
    st.session_state.current_project_id = "alpha"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
STATUS_PILL = {
    "In Progress": '<span class="pill pill-amber">IN PROGRESS</span>',
    "Done":        '<span class="pill pill-green">DONE</span>',
    "Review":      '<span class="pill pill-red">REVIEW</span>',
    "Hold":        '<span class="pill pill-dim">HOLD</span>',
}

def prio_html(p: int) -> str:
    segs = "".join(
        f'<div class="pb pb-on"></div>' if i < p else '<div class="pb pb-off"></div>'
        for i in range(5)
    )
    return f'<div class="prio-bar">{segs}</div>'

def get_shot(shot_id):
    return next((s for s in st.session_state.shots if s["id"] == shot_id), None)

def get_project(proj_id):
    return next((p for p in st.session_state.projects if p["id"] == proj_id), None)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("# Nitya VFX\n\nProject Manager v1.0")
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["▦  Projects", "◫  Shots", "≡  Shot Detail", "◎  Artists"],
        label_visibility="visible",
    )
    st.markdown("---")
    st.markdown(
        "<p style='font-family:JetBrains Mono,monospace;font-size:9px;"
        "color:#5C5849;letter-spacing:0.08em'>session: nitya_prod_01</p>",
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# PAGE: PROJECTS
# ─────────────────────────────────────────────
def page_projects():
    st.markdown("""
    <div class="page-header">
      <div class="page-title">Projects</div>
      <div class="page-sub">3 active productions</div>
    </div>""", unsafe_allow_html=True)

    # Stats row
    cols = st.columns(4)
    stats = [
        ("3", "Active Projects"),
        ("6", "Shots Tracked"),
        ("5", "Artists"),
        ("2", "Done"),
    ]
    for col, (num, label) in zip(cols, stats):
        col.metric(label, num)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Project cards
    col1, col2 = st.columns(2)
    for i, proj in enumerate(st.session_state.projects):
        target_col = col1 if i % 2 == 0 else col2
        artist_pills = "".join(
            f'<span class="pill pill-gold">{a}</span>'
            for a in proj["artists"]
        )
        with target_col:
            st.markdown(f"""
            <div class="nvfx-card">
              <div class="card-title">{proj['name']}</div>
              <div class="card-desc">{proj['description']}</div>
              {artist_pills}
            </div>""", unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Add new project
    with st.expander("＋  Add New Project"):
        with st.form("new_project_form"):
            new_name = st.text_input("Project Name")
            new_desc = st.text_area("Description", height=80)
            if st.form_submit_button("Create Project"):
                if new_name.strip():
                    st.session_state.projects.append({
                        "id": new_name.lower().replace(" ", "_"),
                        "name": new_name.strip(),
                        "description": new_desc.strip(),
                        "artists": [],
                    })
                    st.success(f"Project '{new_name}' created ✓")
                    st.rerun()
                else:
                    st.error("Project name cannot be empty.")

# ─────────────────────────────────────────────
# PAGE: SHOTS
# ─────────────────────────────────────────────
def page_shots():
    proj = get_project(st.session_state.current_project_id)
    proj_name = proj["name"] if proj else "—"

    st.markdown(f"""
    <div class="page-header">
      <div class="page-title">Shots</div>
      <div class="page-sub">{proj_name} · {len(st.session_state.shots)} shots</div>
    </div>""", unsafe_allow_html=True)

    # Filter bar
    filter_col1, filter_col2 = st.columns([2, 1])
    with filter_col1:
        status_filter = st.selectbox(
            "Filter by status",
            ["All", "In Progress", "Done", "Review", "Hold"],
            label_visibility="visible",
        )
    with filter_col2:
        project_filter = st.selectbox(
            "Project",
            [p["name"] for p in st.session_state.projects],
        )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    shots = st.session_state.shots
    if status_filter != "All":
        shots = [s for s in shots if s["status"] == status_filter]

    # Table header
    hcols = st.columns([2, 1.4, 1.2, 1.2, 1.2, 1])
    headers = ["Shot", "Status", "Priority", "Artist", "Frames", "Action"]
    for col, h in zip(hcols, headers):
        col.markdown(
            f"<p style='font-family:JetBrains Mono,monospace;font-size:9px;"
            f"color:#5C5849;letter-spacing:0.1em;text-transform:uppercase;"
            f"margin-bottom:6px'>{h}</p>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);border-width:0.5px;margin:0 0 4px'>",
                unsafe_allow_html=True)

    for shot in shots:
        rcols = st.columns([2, 1.4, 1.2, 1.2, 1.2, 1])
        with rcols[0]:
            st.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;font-size:10px;"
                f"color:#C9A84C'>{shot['code']}</span><br>"
                f"<span style='font-family:Cormorant Garamond,serif;font-size:16px;"
                f"font-weight:600;color:#F0EDE4'>{shot['name']}</span>",
                unsafe_allow_html=True,
            )
        with rcols[1]:
            st.markdown(STATUS_PILL.get(shot["status"], shot["status"]),
                        unsafe_allow_html=True)
        with rcols[2]:
            st.markdown(prio_html(shot["priority"]), unsafe_allow_html=True)
        with rcols[3]:
            st.markdown(
                f"<span style='font-size:12px;color:#9A9486'>{shot['artist']}</span>",
                unsafe_allow_html=True,
            )
        with rcols[4]:
            st.markdown(
                f"<span style='font-family:JetBrains Mono,monospace;font-size:10px;"
                f"color:#5C5849'>{shot['frames']}</span>",
                unsafe_allow_html=True,
            )
        with rcols[5]:
            if st.button("Open", key=f"open_{shot['id']}"):
                st.session_state.current_shot_id = shot["id"]
                st.success(f"Opened {shot['code']} — go to Shot Detail")

        st.markdown(
            "<hr style='border-color:rgba(255,255,255,0.05);border-width:0.5px;margin:4px 0'>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Add new shot
    with st.expander("＋  Add New Shot"):
        with st.form("new_shot_form"):
            fc1, fc2 = st.columns(2)
            new_code   = fc1.text_input("Shot Code", placeholder="SH_070")
            new_sname  = fc2.text_input("Shot Name", placeholder="Underwater sequence")
            new_frames = fc1.text_input("Frames", placeholder="2100–2200")
            new_artist = fc2.text_input("Artist", placeholder="Jamie Lin")
            new_status = st.selectbox("Status", ["In Progress", "Hold", "Review", "Done"])
            new_prio   = st.slider("Priority", 1, 5, 3)
            new_notes  = st.text_area("Notes", height=70)
            if st.form_submit_button("Add Shot"):
                if new_code.strip() and new_sname.strip():
                    st.session_state.shots.append({
                        "id": new_code.lower().replace("_", ""),
                        "code": new_code.upper().strip(),
                        "name": new_sname.strip(),
                        "project": st.session_state.current_project_id,
                        "status": new_status,
                        "priority": new_prio,
                        "artist": new_artist.strip(),
                        "frames": new_frames.strip(),
                        "folder": "",
                        "notes": new_notes.strip(),
                        "history": [],
                    })
                    st.success(f"Shot {new_code} added ✓")
                    st.rerun()
                else:
                    st.error("Shot code and name are required.")

# ─────────────────────────────────────────────
# PAGE: SHOT DETAIL
# ─────────────────────────────────────────────
def page_shot_detail():
    shot = get_shot(st.session_state.current_shot_id)

    if not shot:
        st.error("No shot selected. Go to Shots and click Open on a shot.")
        return

    st.markdown(f"""
    <div class="page-header">
      <div class="page-title">{shot['code']} — {shot['name']}</div>
      <div class="page-sub">Alpha Feature Film · frames {shot['frames']}</div>
    </div>""", unsafe_allow_html=True)

    # Edit form
    with st.form("update_shot_form"):
        c1, c2 = st.columns(2)
        new_status  = c1.text_input("Status",      value=shot["status"])
        new_folder  = c2.text_input("Folder Link", value=shot["folder"])
        new_artist  = c1.text_input("Artist",      value=shot["artist"])
        new_frames  = c2.text_input("Frames",      value=shot["frames"])
        new_prio    = st.slider("Priority (1–5)", 1, 5, shot["priority"])
        new_notes   = st.text_area("Notes", value=shot["notes"], height=100)
        new_history = st.text_input("New History Entry",
                                    placeholder="Describe what changed…")

        if st.form_submit_button("Save Changes"):
            shot["status"]  = new_status
            shot["folder"]  = new_folder
            shot["artist"]  = new_artist
            shot["frames"]  = new_frames
            shot["priority"] = new_prio
            shot["notes"]   = new_notes
            if new_history.strip():
                shot["history"].insert(0, {
                    "date": str(date.today()),
                    "note": new_history.strip(),
                })
                shot["history"] = shot["history"][:MAX_HISTORY_ITEMS]
            st.success(f"{shot['code']} saved ✓")
            st.rerun()

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # History
    st.markdown(
        "<p style='font-family:JetBrains Mono,monospace;font-size:9px;"
        "color:#5C5849;letter-spacing:0.1em;text-transform:uppercase;"
        "margin-bottom:12px'>History — last 15 entries</p>",
        unsafe_allow_html=True,
    )

    if shot["history"]:
        for item in shot["history"][:MAX_HISTORY_ITEMS]:
            st.markdown(f"""
            <div class="hist-item">
              <div class="hist-date">{item['date']}</div>
              <div class="hist-note">{item['note']}</div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown(
            "<p style='color:#5C5849;font-size:13px;font-style:italic'>"
            "No history entries yet.</p>",
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────
# PAGE: ARTISTS
# ─────────────────────────────────────────────
def page_artists():
    proj = get_project(st.session_state.current_project_id)
    proj_name = proj["name"] if proj else "—"

    st.markdown(f"""
    <div class="page-header">
      <div class="page-title">Artists</div>
      <div class="page-sub">{proj_name} · {len(st.session_state.artists)} members</div>
    </div>""", unsafe_allow_html=True)

    # Artist cards
    for artist in st.session_state.artists:
        col_card, col_edit = st.columns([6, 1])
        with col_card:
            st.markdown(f"""
            <div class="nvfx-card" style="display:flex;align-items:center;gap:16px;padding:14px 20px">
              <div class="avatar" style="border-color:{artist['color']};color:{artist['color']};
                background:rgba(0,0,0,0.3)">{artist['initials']}</div>
              <div>
                <div class="artist-name">{artist['name']}</div>
                <div class="artist-role">{artist['role']}</div>
                <div class="artist-email">{artist['email']}</div>
              </div>
            </div>""", unsafe_allow_html=True)
        with col_edit:
            edit_key = f"edit_{artist['id']}"
            if edit_key not in st.session_state:
                st.session_state[edit_key] = False
            st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
            if st.button("Edit", key=f"btn_{artist['id']}"):
                st.session_state[edit_key] = not st.session_state[edit_key]

        # Inline edit form
        if st.session_state.get(f"edit_{artist['id']}"):
            with st.form(f"edit_artist_{artist['id']}"):
                ea1, ea2, ea3 = st.columns(3)
                upd_name  = ea1.text_input("Name",  value=artist["name"])
                upd_role  = ea2.text_input("Role",  value=artist["role"])
                upd_email = ea3.text_input("Email", value=artist["email"])
                if st.form_submit_button("Save Artist"):
                    artist["name"]  = upd_name.strip()
                    artist["role"]  = upd_role.strip()
                    artist["email"] = upd_email.strip()
                    st.session_state[f"edit_{artist['id']}"] = False
                    st.success(f"{artist['name']} updated ✓")
                    st.rerun()

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Add new artist
    with st.expander("＋  Add New Artist"):
        with st.form("new_artist_form"):
            na1, na2, na3 = st.columns(3)
            na_name  = na1.text_input("Name")
            na_role  = na2.text_input("Role")
            na_email = na3.text_input("Email")
            if st.form_submit_button("Add Artist"):
                if na_name.strip():
                    initials = "".join(w[0].upper() for w in na_name.strip().split()[:2])
                    st.session_state.artists.append({
                        "id":       na_name.lower().replace(" ", "_"),
                        "name":     na_name.strip(),
                        "initials": initials,
                        "role":     na_role.strip(),
                        "email":    na_email.strip(),
                        "color":    "#C9A84C",
                    })
                    st.success(f"Artist '{na_name}' added ✓")
                    st.rerun()
                else:
                    st.error("Name is required.")

# ─────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────
if "Projects" in page:
    page_projects()
elif "Shots" in page:
    page_shots()
elif "Shot Detail" in page:
    page_shot_detail()
elif "Artists" in page:
    page_artists()
