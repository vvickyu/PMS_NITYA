"""
app.py — Nitya VFX Project Manager
Run:  streamlit run app.py
"""

import streamlit as st
from db import Database, init_db

init_db()
db = Database()

st.set_page_config(
    page_title="Nitya VFX — Project Manager",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=JetBrains+Mono:wght@300;400;500;700&family=Outfit:wght@300;400;500;600&display=swap');

:root {
  --gold:#C9A84C; --gold-bright:#E8C96A; --gold-dim:#7A6230;
  --gold-pale:rgba(201,168,76,0.08);
  --ink:#080A0E; --surface:#0E1118; --surface2:#141720; --surface3:#1B1F2B;
  --border:rgba(201,168,76,0.18); --border2:rgba(255,255,255,0.07);
  --text:#F0EDE4; --text-mid:#9A9486; --text-dim:#5C5849;
  --red:#E05252; --green:#52B788; --amber:#E8A838;
}

/* ── Base ── */
html, body, .stApp { font-size: 17px !important; }
.stApp { background: var(--ink) !important; }
[data-testid="stAppViewContainer"] { background: var(--ink) !important; }
[data-testid="stHeader"] { background: var(--ink) !important; }
.block-container {
  padding-top: 2.5rem !important;
  padding-bottom: 3rem !important;
  max-width: 1200px !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 0.5px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-mid) !important; }
[data-testid="stSidebar"] label { font-size: 15px !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 16px !important; font-weight: 400 !important; }
[data-testid="stSidebar"] p { font-size: 15px !important; }

/* ── All text inputs & textareas ── */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
  background: var(--surface2) !important;
  border: 0.5px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 0 !important;
  font-family: 'Outfit', sans-serif !important;
  font-size: 16px !important;
  padding: 10px 14px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 1px var(--gold-pale) !important;
}
.stTextInput label,
.stTextArea label,
.stNumberInput label,
.stSelectbox label,
.stSlider label {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--gold) !important;
  font-weight: 500 !important;
  margin-bottom: 6px !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
  background: var(--surface2) !important;
  border: 0.5px solid var(--border) !important;
  border-radius: 0 !important;
  font-size: 16px !important;
  color: var(--text) !important;
  min-height: 46px !important;
}

/* ── Buttons ── */
.stButton > button {
  background: var(--gold) !important;
  color: #080A0E !important;
  border: none !important;
  border-radius: 0 !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  padding: 13px 28px !important;
  min-height: 46px !important;
  transition: background 0.2s !important;
}
.stButton > button:hover {
  background: var(--gold-bright) !important;
  color: #080A0E !important;
}
.stFormSubmitButton > button {
  font-size: 12px !important;
  padding: 12px 26px !important;
  min-height: 44px !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 0.5px solid var(--border2) !important;
  padding: 22px 24px !important;
  border-left: 2px solid var(--gold) !important;
}
[data-testid="stMetricValue"] {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 52px !important;
  color: var(--gold) !important;
  line-height: 1 !important;
}
[data-testid="stMetricLabel"] {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: var(--text-dim) !important;
}

/* ── Expanders ── */
[data-testid="stExpander"] {
  background: var(--surface) !important;
  border: 0.5px solid var(--border2) !important;
  border-radius: 0 !important;
  margin-bottom: 10px !important;
}
[data-testid="stExpander"]:hover { border-color: var(--border) !important; }
[data-testid="stExpander"] summary {
  font-family: 'Cormorant Garamond', serif !important;
  font-size: 20px !important;
  font-weight: 600 !important;
  padding: 18px 20px !important;
  color: var(--text) !important;
}
[data-testid="stExpanderDetails"] { padding: 8px 20px 20px !important; }
[data-testid="stExpanderToggleIcon"] { color: var(--gold) !important; }

/* ── Slider ── */
[data-testid="stSlider"] > div > div > div {
  background: var(--gold) !important;
}
.stSlider [data-testid="stTickBarMin"],
.stSlider [data-testid="stTickBarMax"] {
  font-size: 13px !important;
  color: var(--text-dim) !important;
}

/* ── Number input ── */
[data-testid="stNumberInput"] input {
  font-size: 16px !important;
}

/* ── Alerts ── */
[data-testid="stAlert"] { border-radius: 0 !important; font-size: 15px !important; }
.stSuccess { background: rgba(82,183,136,0.1) !important; border-color: var(--green) !important; }
.stWarning { background: rgba(232,168,56,0.1) !important; border-color: var(--amber) !important; }
.stError   { background: rgba(224,82,82,0.1)  !important; border-color: var(--red) !important; }

/* ── Dividers ── */
hr { border-color: var(--border) !important; margin: 28px 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--ink); }
::-webkit-scrollbar-thumb { background: var(--gold-dim); border-radius: 2px; }

/* ── Generic paragraph text ── */
p, li, div { line-height: 1.65; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# CONSTANTS & HELPERS
# ─────────────────────────────────────────────────────────────

STATUS_OPTIONS = ["Pending", "In Progress", "Review", "On Hold", "Done", "Cancelled"]
STATUS_COLORS  = {
    "In Progress": "#E8A838",
    "Done":        "#52B788",
    "Review":      "#E05252",
    "On Hold":     "#7A6230",
    "Pending":     "#5C5849",
    "Cancelled":   "#5C5849",
}
AVATAR_COLORS = ["#C9A84C", "#52B788", "#E8A838", "#E05252", "#9C88E0", "#4A90D9"]


def status_badge(status: str, size: str = "12px") -> str:
    c = STATUS_COLORS.get(status, "#5C5849")
    return (
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:{size};'
        f'padding:5px 14px;border:0.5px solid {c};color:{c};'
        f'background:{c}20;letter-spacing:0.08em;white-space:nowrap">'
        f'{status.upper()}</span>'
    )


def prio_bar(value: int, max_val: int = 5) -> str:
    segs = "".join(
        f'<div style="width:18px;height:6px;background:{"#C9A84C" if i<=value else "#1B1F2B"};'
        f'display:inline-block;margin-right:3px;border-radius:1px"></div>'
        for i in range(1, max_val + 1)
    )
    return f'<div style="display:flex;align-items:center;gap:2px;margin-top:2px">{segs}</div>'


def mono_label(text: str, size: str = "11px") -> str:
    return (
        f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:{size};'
        f'color:#C9A84C;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:10px">'
        f'{text}</div>'
    )


def section_header(tag: str, title: str, sub: str = "") -> None:
    sub_html = (
        f'<div style="font-family:\'Outfit\',sans-serif;font-size:17px;'
        f'color:#9A9486;font-weight:300;margin-top:8px;max-width:600px">{sub}</div>'
        if sub else ""
    )
    st.markdown(f"""
    <div style="margin-bottom:32px;padding-bottom:24px;
                border-bottom:0.5px solid rgba(201,168,76,0.15)">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;
                  color:#C9A84C;letter-spacing:0.22em;text-transform:uppercase;
                  display:flex;align-items:center;gap:12px;margin-bottom:10px">
        {tag}
        <span style="width:36px;height:0.5px;background:#C9A84C;display:inline-block"></span>
      </div>
      <div style="font-family:'Cormorant Garamond',serif;
                  font-size:clamp(32px,4vw,52px);font-weight:300;line-height:1.05">
        {title}
      </div>
      {sub_html}
    </div>
    """, unsafe_allow_html=True)


def card_box(content_html: str, border_color: str = "rgba(255,255,255,0.07)",
             pad: str = "22px 24px") -> None:
    st.markdown(
        f'<div style="background:#0E1118;border:0.5px solid {border_color};'
        f'padding:{pad};margin-bottom:12px">{content_html}</div>',
        unsafe_allow_html=True,
    )


def hist_row(date_str: str, entry: str) -> str:
    return (
        f'<div style="display:flex;gap:20px;padding:14px 0;'
        f'border-bottom:0.5px solid rgba(255,255,255,0.05)">'
        f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:11px;'
        f'color:#7A6230;flex-shrink:0;padding-top:2px;min-width:88px">{date_str}</div>'
        f'<div style="font-size:16px;color:#9A9486;font-weight:300;line-height:1.5">{entry}</div>'
        f'</div>'
    )


# ─────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("""
    <div style="padding:12px 0 22px">
      <div style="font-family:'Cormorant Garamond',serif;font-size:30px;
                  font-weight:600;color:#C9A84C;line-height:1">Nitya VFX</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:10px;
                  color:#5C5849;letter-spacing:0.16em;text-transform:uppercase;
                  margin-top:4px">Project Manager v1.0</div>
    </div>
    <hr style="border-color:rgba(201,168,76,0.18);margin:0 0 20px"/>
    """, unsafe_allow_html=True)

    projects = db.get_projects()
    if projects:
        proj_names = [p["name"] for p in projects]
        chosen_name = st.selectbox("Active Project", proj_names, key="proj_select")
        active_proj = next(p for p in projects if p["name"] == chosen_name)
        st.session_state["project_id"] = active_proj["id"]
    else:
        st.warning("No projects yet.")
        st.session_state["project_id"] = None

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:16px 0'/>",
                unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["▦  Projects", "◫  Shots", "≡  Shot Detail", "◎  Artists"],
        key="nav_page",
    )

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:16px 0'/>",
                unsafe_allow_html=True)

    pid = st.session_state.get("project_id")
    if pid:
        stats = db.get_stats(pid)
        st.markdown(f"""
        <div style="font-family:'JetBrains Mono',monospace;font-size:10px;
                    color:#5C5849;letter-spacing:0.14em;text-transform:uppercase;
                    margin-bottom:14px">Quick Stats</div>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:15px;color:#9A9486">🟡 In Progress</span>
            <b style="font-family:'Cormorant Garamond',serif;font-size:22px;color:#E8A838">{stats['in_progress']}</b>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:15px;color:#9A9486">🔴 Review</span>
            <b style="font-family:'Cormorant Garamond',serif;font-size:22px;color:#E05252">{stats['review']}</b>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:15px;color:#9A9486">🟢 Done</span>
            <b style="font-family:'Cormorant Garamond',serif;font-size:22px;color:#52B788">{stats['done']}</b>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:15px;color:#9A9486">⚪ Pending</span>
            <b style="font-family:'Cormorant Garamond',serif;font-size:22px;color:#5C5849">{stats['pending']}</b>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:15px;color:#9A9486">⏸ Hold</span>
            <b style="font-family:'Cormorant Garamond',serif;font-size:22px;color:#7A6230">{stats['hold']}</b>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding-top:32px;font-family:'JetBrains Mono',monospace;
                font-size:10px;color:#5C5849;letter-spacing:0.06em">
      session: nitya_prod_01
    </div>
    """, unsafe_allow_html=True)

project_id: int | None = st.session_state.get("project_id")


# ═════════════════════════════════════════════════════════════════════════════
# PAGE: PROJECTS
# ═════════════════════════════════════════════════════════════════════════════

if page == "▦  Projects":
    section_header("Projects", "All <em style='color:#C9A84C'>Productions</em>",
                   "Browse, edit, and manage every active production at a glance.")

    projects = db.get_projects()

    if not projects:
        st.info("No projects yet — create one below.")
    else:
        for proj in projects:
            artists = db.get_artists(proj["id"])
            stats   = db.get_stats(proj["id"])

            with st.expander(
                f"**{proj['name']}**   ·   {stats['total']} shots   "
                f"·   ✅ {stats['done']} done   🟡 {stats['in_progress']} in progress",
                expanded=(proj["id"] == project_id),
            ):
                # Description
                st.markdown(
                    f'<div style="font-family:\'Outfit\',sans-serif;font-size:17px;'
                    f'color:#9A9486;font-weight:300;margin-bottom:18px;line-height:1.6">'
                    f'{proj["description"] or "<em>No description.</em>"}</div>',
                    unsafe_allow_html=True,
                )

                # Artist pills
                if artists:
                    pills = "".join(
                        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:11px;'
                        f'border:0.5px solid rgba(201,168,76,0.25);padding:4px 12px;'
                        f'color:#7A6230;margin-right:6px;margin-bottom:6px;display:inline-block">'
                        f'{a["name"]}</span>'
                        for a in artists
                    )
                    st.markdown(
                        f'<div style="margin-bottom:20px"><span style="font-family:\'JetBrains Mono\','
                        f'monospace;font-size:10px;color:#5C5849;letter-spacing:0.12em;'
                        f'text-transform:uppercase;margin-right:10px">Artists</span>{pills}</div>',
                        unsafe_allow_html=True,
                    )

                with st.form(f"edit_proj_{proj['id']}"):
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        new_name = st.text_input("Project Name", value=proj["name"],
                                                 key=f"pn_{proj['id']}")
                        new_desc = st.text_area("Description", value=proj["description"],
                                                key=f"pd_{proj['id']}", height=90)
                    with c2:
                        st.write("")
                        st.write("")
                        st.write("")
                        if st.form_submit_button("💾  Save"):
                            db.update_project(proj["id"], new_name, new_desc)
                            st.success("Saved ✓")
                            st.rerun()

                if st.button("🗑  Delete Project", key=f"del_proj_{proj['id']}"):
                    db.delete_project(proj["id"])
                    st.warning("Project deleted.")
                    st.rerun()

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:36px 0 24px'/>",
                unsafe_allow_html=True)
    st.markdown(mono_label("New Project"), unsafe_allow_html=True)

    with st.form("new_project_form"):
        c1, c2 = st.columns([2, 3])
        with c1:
            np_name = st.text_input("Project Name *")
        with c2:
            np_desc = st.text_area("Description", height=80)
        if st.form_submit_button("＋  Create Project"):
            if np_name.strip():
                new_id = db.create_project(np_name.strip(), np_desc.strip())
                st.success(f"'{np_name}' created!")
                st.session_state["project_id"] = new_id
                st.rerun()
            else:
                st.error("Project name is required.")


# ═════════════════════════════════════════════════════════════════════════════
# PAGE: SHOTS
# ═════════════════════════════════════════════════════════════════════════════

elif page == "◫  Shots":
    if not project_id:
        st.warning("Select a project from the sidebar first.")
        st.stop()

    proj  = db.get_project(project_id)
    shots = db.get_shots(project_id)
    stats = db.get_stats(project_id)

    section_header("Shots", f"<em style='color:#C9A84C'>{proj['name']}</em>",
                   "All shots sorted by priority. Click Edit to open the detail view.")

    # ── Dashboard metrics ──
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Shots",  stats["total"])
    c2.metric("Done",         stats["done"])
    c3.metric("In Progress",  stats["in_progress"])
    c4.metric("Review",       stats["review"])
    c5.metric("Hold",         stats["hold"])

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    # ── Filters ──
    f1, f2, f3 = st.columns([2, 2, 4])
    with f1:
        filter_status = st.selectbox("Filter by Status",
                                     ["All"] + STATUS_OPTIONS, key="shot_filter")
    with f2:
        sort_by = st.selectbox("Sort by",
                               ["Priority ↓", "Name ↑", "Status"], key="shot_sort")

    filtered = shots
    if filter_status != "All":
        filtered = [s for s in filtered if s["status"] == filter_status]
    if sort_by == "Name ↑":
        filtered = sorted(filtered, key=lambda x: x["name"])
    elif sort_by == "Status":
        filtered = sorted(filtered, key=lambda x: x["status"])

    st.markdown("<hr style='border-color:rgba(201,168,76,0.1);margin:16px 0'/>",
                unsafe_allow_html=True)

    if not filtered:
        st.info("No shots match the current filter.")
    else:
        # Column header
        st.markdown("""
        <div style="display:grid;
                    grid-template-columns:2.2fr 1.4fr 1fr 1.2fr 1fr 0.8fr;
                    gap:10px;padding:8px 16px 10px;
                    font-family:'JetBrains Mono',monospace;font-size:10px;
                    color:#5C5849;letter-spacing:0.12em;text-transform:uppercase;
                    border-bottom:0.5px solid rgba(201,168,76,0.15);margin-bottom:4px">
          <div>Shot</div><div>Status</div><div>Priority</div>
          <div>Artist</div><div>Frames</div><div>Action</div>
        </div>
        """, unsafe_allow_html=True)

        for shot in filtered:
            desc_short = shot["description"][:48] + "…" if len(shot["description"]) > 48 else shot["description"]
            frames = f"{shot['frame_start']}–{shot['frame_end']}"

            # Row card
            st.markdown(f"""
            <div style="display:grid;
                        grid-template-columns:2.2fr 1.4fr 1fr 1.2fr 1fr 0.8fr;
                        gap:10px;align-items:center;
                        padding:16px 16px;
                        background:#0E1118;
                        border:0.5px solid rgba(255,255,255,0.05);
                        border-left:2px solid rgba(201,168,76,0.15);
                        margin-bottom:6px;
                        transition:border-color 0.2s">
              <div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:11px;
                            color:#C9A84C;margin-bottom:4px">{shot['name']}</div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:19px;
                            font-weight:600;color:#F0EDE4;line-height:1.2">{desc_short or shot['name']}</div>
              </div>
              <div>{status_badge(shot['status'], '11px')}</div>
              <div>{prio_bar(shot['priority'])}<div style="font-family:'JetBrains Mono',monospace;
                   font-size:11px;color:#7A6230;margin-top:5px">{shot['priority']} / 5</div></div>
              <div style="font-size:16px;color:#9A9486">{shot['artist'] or '—'}</div>
              <div style="font-family:'JetBrains Mono',monospace;font-size:12px;
                          color:#5C5849">{frames}</div>
              <div></div>
            </div>
            """, unsafe_allow_html=True)

            # Edit button below each row — Streamlit buttons can't go inside markdown
            if st.button("✏  Edit", key=f"edit_{shot['id']}"):
                st.session_state["shot_id"] = shot["id"]
                st.session_state["nav_page"] = "≡  Shot Detail"
                st.rerun()

    # ── New Shot ──
    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:36px 0 24px'/>",
                unsafe_allow_html=True)
    st.markdown(mono_label("Add New Shot"), unsafe_allow_html=True)

    with st.form("new_shot_form"):
        r1, r2, r3 = st.columns(3)
        with r1:
            ns_name   = st.text_input("Shot Name * (e.g. SH_070)")
        with r2:
            ns_artist = st.text_input("Artist")
        with r3:
            ns_status = st.selectbox("Status", STATUS_OPTIONS)

        r4, r5, r6, r7 = st.columns(4)
        with r4:
            ns_priority = st.slider("Priority", 1, 5, 3)
        with r5:
            ns_fs = st.number_input("Frame Start", value=1001, step=1)
        with r6:
            ns_fe = st.number_input("Frame End",   value=1100, step=1)

        ns_desc = st.text_area("Description", height=70)

        if st.form_submit_button("＋  Add Shot"):
            if ns_name.strip():
                db.create_shot(project_id, ns_name.strip(), ns_desc.strip(),
                               ns_status, ns_priority,
                               int(ns_fs), int(ns_fe), ns_artist.strip())
                st.success(f"Shot '{ns_name}' added!")
                st.rerun()
            else:
                st.error("Shot name is required.")


# ═════════════════════════════════════════════════════════════════════════════
# PAGE: SHOT DETAIL
# ═════════════════════════════════════════════════════════════════════════════

elif page == "≡  Shot Detail":
    if not project_id:
        st.warning("Select a project from the sidebar first.")
        st.stop()

    proj  = db.get_project(project_id)
    shots = db.get_shots(project_id)

    if not shots:
        st.info("No shots in this project yet. Go to Shots to add some.")
        st.stop()

    shot_options = {
        f"{s['name']}  —  {s['description'][:45] if s['description'] else s['name']}": s["id"]
        for s in shots
    }
    saved_id     = st.session_state.get("shot_id")
    default_lbl  = next(
        (lbl for lbl, sid in shot_options.items() if sid == saved_id),
        list(shot_options.keys())[0]
    )

    chosen_lbl = st.selectbox(
        "Select Shot", list(shot_options.keys()),
        index=list(shot_options.keys()).index(default_lbl),
        key="detail_shot_sel",
    )
    shot_id = shot_options[chosen_lbl]
    st.session_state["shot_id"] = shot_id
    shot = db.get_shot(shot_id)

    # ── Big shot header ──
    st.markdown(f"""
    <div style="margin:20px 0 32px;padding:28px 32px;
                background:#0E1118;
                border:0.5px solid rgba(201,168,76,0.18);
                border-left:3px solid #C9A84C">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;
                  color:#7A6230;letter-spacing:0.16em;text-transform:uppercase;
                  margin-bottom:8px">{proj['name']}</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:52px;
                  font-weight:600;color:#F0EDE4;line-height:1;margin-bottom:10px">
        {shot['name']}
      </div>
      <div style="font-size:17px;color:#9A9486;font-weight:300;margin-bottom:14px">
        {shot['description'] or '—'}
      </div>
      <div style="display:flex;gap:24px;align-items:center;flex-wrap:wrap">
        {status_badge(shot['status'], '13px')}
        <span style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5C5849">
          frames {shot['frame_start']}–{shot['frame_end']}
        </span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5C5849">
          artist: {shot['artist'] or '—'}
        </span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5C5849">
          priority: {shot['priority']} / 5
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics row
    cm1, cm2, cm3, cm4 = st.columns(4)
    cm1.metric("Status",       shot["status"])
    cm2.metric("Priority",     f"{shot['priority']} / 5")
    cm3.metric("Frames",       f"{shot['frame_end'] - shot['frame_start']} fr")
    cm4.metric("History",      f"{len(shot['history'])} entries")

    if shot.get("folder_link"):
        st.markdown(
            f'<div style="margin-top:12px">'
            f'<a href="{shot["folder_link"]}" target="_blank" style="font-family:\'JetBrains Mono\','
            f'monospace;font-size:13px;color:#C9A84C;text-decoration:none">'
            f'📁 {shot["folder_link"]}</a></div>',
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:28px 0'/>",
                unsafe_allow_html=True)
    st.markdown(mono_label("Edit Shot"), unsafe_allow_html=True)

    # ── Edit Form ──
    with st.form("shot_detail_form"):
        row1c1, row1c2 = st.columns(2)
        with row1c1:
            new_status = st.selectbox("Status", STATUS_OPTIONS,
                                      index=STATUS_OPTIONS.index(shot["status"])
                                      if shot["status"] in STATUS_OPTIONS else 0)
            new_artist = st.text_input("Artist", value=shot["artist"] or "")
        with row1c2:
            new_folder = st.text_input("Folder Link", value=shot["folder_link"] or "")
            new_prio   = st.slider("Priority (1–5)", 1, 5, shot["priority"])

        row2c1, row2c2 = st.columns(2)
        with row2c1:
            new_fs = st.number_input("Frame Start", value=shot["frame_start"], step=1)
        with row2c2:
            new_fe = st.number_input("Frame End",   value=shot["frame_end"],   step=1)

        new_notes = st.text_area(
            "Notes", value=shot["notes"] or "",
            height=120, placeholder="Production notes…"
        )
        new_hist = st.text_input(
            "New History Entry", placeholder="Describe what changed…"
        )

        sc1, sc2, _ = st.columns([1.2, 1.2, 4])
        with sc1:
            saved = st.form_submit_button("💾  Save Changes")
        with sc2:
            deleted = st.form_submit_button("🗑  Delete Shot")

        if saved:
            db.update_shot(
                shot_id,
                status=new_status, priority=int(new_prio),
                notes=new_notes, folder_link=new_folder,
                artist=new_artist,
                frame_start=int(new_fs), frame_end=int(new_fe),
            )
            if new_hist.strip():
                db.append_history(shot_id, new_hist)
            st.success("Shot updated ✓")
            st.rerun()

        if deleted:
            db.delete_shot(shot_id)
            st.warning("Shot deleted.")
            st.session_state.pop("shot_id", None)
            st.rerun()

    # ── History ──
    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:32px 0 20px'/>",
                unsafe_allow_html=True)
    st.markdown(mono_label(f"History Log — last 15 entries"), unsafe_allow_html=True)

    history = shot["history"]
    if not history:
        st.markdown(
            '<div style="font-size:16px;color:#5C5849;font-style:italic;padding:12px 0">'
            'No history entries yet.</div>',
            unsafe_allow_html=True,
        )
    else:
        rows_html = "".join(hist_row(item["date"], item["entry"]) for item in history)
        st.markdown(
            f'<div style="background:#0E1118;border:0.5px solid rgba(255,255,255,0.06);'
            f'padding:4px 20px 4px">{rows_html}</div>',
            unsafe_allow_html=True,
        )


# ═════════════════════════════════════════════════════════════════════════════
# PAGE: ARTISTS
# ═════════════════════════════════════════════════════════════════════════════

elif page == "◎  Artists":
    if not project_id:
        st.warning("Select a project from the sidebar first.")
        st.stop()

    proj    = db.get_project(project_id)
    artists = db.get_artists(project_id)

    section_header("Artists", f"<em style='color:#C9A84C'>{proj['name']}</em> Roster",
                   "Manage names, roles, and contacts for every team member on this production.")

    if not artists:
        st.info("No artists on this project yet. Add one below.")
    else:
        for i, artist in enumerate(artists):
            color    = AVATAR_COLORS[i % len(AVATAR_COLORS)]
            initials = "".join(w[0].upper() for w in artist["name"].split()[:2])

            with st.expander(f"**{artist['name']}**  ·  {artist['role']}"):
                # Avatar + info header
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:20px;
                            margin-bottom:20px;padding-bottom:18px;
                            border-bottom:0.5px solid rgba(255,255,255,0.06)">
                  <div style="width:56px;height:56px;border:0.5px solid {color};
                              display:flex;align-items:center;justify-content:center;
                              font-family:'Cormorant Garamond',serif;font-size:22px;
                              font-weight:600;color:{color};flex-shrink:0">{initials}</div>
                  <div>
                    <div style="font-family:'Cormorant Garamond',serif;font-size:26px;
                                font-weight:600;color:#F0EDE4;line-height:1">{artist['name']}</div>
                    <div style="font-size:16px;color:#9A9486;font-weight:300;margin-top:4px">{artist['role']}</div>
                    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;
                                color:#5C5849;margin-top:4px">{artist['email']}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                with st.form(f"artist_form_{artist['id']}"):
                    fc1, fc2, fc3 = st.columns(3)
                    with fc1:
                        a_name  = st.text_input("Name",  value=artist["name"])
                    with fc2:
                        a_role  = st.text_input("Role",  value=artist["role"])
                    with fc3:
                        a_email = st.text_input("Email", value=artist["email"])

                    bc1, bc2, _ = st.columns([1, 1, 4])
                    with bc1:
                        if st.form_submit_button("💾  Save"):
                            db.update_artist(artist["id"], a_name, a_role, a_email)
                            st.success("Saved ✓")
                            st.rerun()
                    with bc2:
                        if st.form_submit_button("🗑  Remove"):
                            db.delete_artist(artist["id"])
                            st.warning(f"{artist['name']} removed.")
                            st.rerun()

    st.markdown("<hr style='border-color:rgba(201,168,76,0.18);margin:36px 0 24px'/>",
                unsafe_allow_html=True)
    st.markdown(mono_label("Add Artist"), unsafe_allow_html=True)

    with st.form("new_artist_form"):
        na1, na2, na3 = st.columns(3)
        with na1:
            na_name  = st.text_input("Name *")
        with na2:
            na_role  = st.text_input("Role")
        with na3:
            na_email = st.text_input("Email")

        if st.form_submit_button("＋  Add Artist"):
            if na_name.strip():
                db.create_artist(project_id, na_name.strip(),
                                 na_role.strip(), na_email.strip())
                st.success(f"{na_name} added to {proj['name']}!")
                st.rerun()
            else:
                st.error("Name is required.")
