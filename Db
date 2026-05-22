"""
db.py — SQLite database layer for Nitya VFX Project Manager
Swap the connection in _connect() to use PostgreSQL or any other backend.
"""

import sqlite3
import json
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).parent / "nitya_vfx.db"
MAX_HISTORY = 15


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


# ─────────────────────────────────────────────────────────────
# INIT & SEED
# ─────────────────────────────────────────────────────────────

def init_db() -> None:
    """Create all tables and seed sample data on first run."""
    with _connect() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS projects (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT NOT NULL,
                description TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS artists (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
                name       TEXT NOT NULL,
                role       TEXT DEFAULT '',
                email      TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS shots (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id  INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
                name        TEXT NOT NULL,
                description TEXT DEFAULT '',
                status      TEXT DEFAULT 'Pending',
                priority    INTEGER DEFAULT 3,
                notes       TEXT DEFAULT '',
                folder_link TEXT DEFAULT '',
                frame_start INTEGER DEFAULT 1001,
                frame_end   INTEGER DEFAULT 1100,
                artist      TEXT DEFAULT '',
                history     TEXT DEFAULT '[]'
            );
        """)

        # Only seed when database is empty
        if conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0] == 0:
            _seed(conn)


def _seed(conn: sqlite3.Connection) -> None:
    """Insert sample projects, artists, and shots."""

    # ── Projects ──
    conn.execute("INSERT INTO projects (name, description) VALUES (?, ?)",
        ("Alpha Feature Film", "Wide-release VFX — 240 shots across 3 sequences. Delivery Q3."))
    conn.execute("INSERT INTO projects (name, description) VALUES (?, ?)",
        ("Beta Episodic", "8-episode series. Compositing and creature FX pipeline."))
    conn.execute("INSERT INTO projects (name, description) VALUES (?, ?)",
        ("Gamma Commercial", "30-second spot. Product viz + environment extension."))

    # ── Artists ──
    artists_p1 = [
        (1, "Jamie Lin",   "Senior Compositor",   "jamie.lin@nityavfx.com"),
        (1, "Priya Mehta", "FX Artist",            "priya.mehta@nityavfx.com"),
        (1, "Rohan Das",   "Creature FX Lead",     "rohan.das@nityavfx.com"),
        (1, "Carlos R.",   "Lighter / LookDev",    "carlos.r@nityavfx.com"),
        (1, "Ananya K.",   "FX / Simulation",      "ananya.k@nityavfx.com"),
    ]
    artists_p2 = [
        (2, "Carlos R.",   "Compositor",           "carlos.r@nityavfx.com"),
        (2, "Ananya K.",   "FX Artist",            "ananya.k@nityavfx.com"),
    ]
    artists_p3 = [
        (3, "Priya Mehta", "Lead Artist",          "priya.mehta@nityavfx.com"),
    ]
    conn.executemany(
        "INSERT INTO artists (project_id, name, role, email) VALUES (?,?,?,?)",
        artists_p1 + artists_p2 + artists_p3,
    )

    # ── Shots ──
    history_010 = json.dumps([
        {"date": "2026-05-22", "entry": "Lens flare comp updated per supervisor feedback. Frame 1080 isolated and re-rendered."},
        {"date": "2026-05-21", "entry": "Motion blur pass applied to debris layer. Intensity raised to 0.45."},
        {"date": "2026-05-20", "entry": "Grading pass aligned to sequence LUT v3. BG plates signed off."},
        {"date": "2026-05-19", "entry": "Initial comp delivery to internal review."},
    ])
    shots = [
        (1, "SH_010", "Wide shot of the hero explosion sequence.",      "In Progress", 4, "Check lens flare comp on frame 1080. Director wants extra motion blur on debris elements.", "/projects/alpha/sh_010", 1001, 1120, "Jamie Lin",  history_010),
        (1, "SH_020", "City skyline environment extension.",             "Done",        2, "Approved by director. Archive ready.",                                                       "/projects/alpha/sh_020", 1200, 1340, "Priya Mehta", "[]"),
        (1, "SH_030", "Creature attack — practical + CG composite.",    "Review",      5, "Supervisor review pending. Check edge matte on creature L shoulder.",                        "/projects/alpha/sh_030", 1400, 1520, "Rohan Das",   "[]"),
        (1, "SH_040", "Portal open — particle FX and lens distortion.", "Hold",        1, "On hold pending client approval of portal design.",                                          "/projects/alpha/sh_040", 1600, 1680, "Jamie Lin",   "[]"),
        (1, "SH_050", "Rain simulation over city block.",               "In Progress", 3, "Sim cache approved. Lighting pass in progress.",                                             "/projects/alpha/sh_050", 1700, 1820, "Ananya K.",   "[]"),
        (1, "SH_060", "Final wide establishing shot.",                  "Done",        4, "Delivered. Final grade signed off.",                                                         "/projects/alpha/sh_060", 1900, 2020, "Carlos R.",   "[]"),
        (2, "EP01_SH_010", "Title card reveal over city.",              "In Progress", 3, "Working on depth of field adjustments.",                                                     "/projects/beta/ep01_sh_010", 1001, 1080, "Carlos R.", "[]"),
        (2, "EP01_SH_020", "Interior control room background.",         "Pending",     2, "",                                                                                           "",                           1100, 1200, "Ananya K.", "[]"),
        (3, "COMM_010",    "Hero product floating in environment.",     "In Progress", 4, "Client approved v2. Refinements in progress.",                                              "/projects/gamma/comm_010",   1001, 1030, "Priya Mehta", "[]"),
    ]
    conn.executemany(
        """INSERT INTO shots
           (project_id, name, description, status, priority, notes, folder_link,
            frame_start, frame_end, artist, history)
           VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        shots,
    )


# ─────────────────────────────────────────────────────────────
# DATABASE CLASS
# ─────────────────────────────────────────────────────────────

class Database:

    # ── Projects ──────────────────────────────────────────────

    def get_projects(self) -> list[dict]:
        with _connect() as c:
            return [dict(r) for r in c.execute("SELECT * FROM projects ORDER BY id")]

    def get_project(self, pid: int) -> dict | None:
        with _connect() as c:
            r = c.execute("SELECT * FROM projects WHERE id=?", (pid,)).fetchone()
            return dict(r) if r else None

    def create_project(self, name: str, description: str = "") -> int:
        with _connect() as c:
            return c.execute(
                "INSERT INTO projects (name, description) VALUES (?,?)", (name, description)
            ).lastrowid

    def update_project(self, pid: int, name: str, description: str) -> None:
        with _connect() as c:
            c.execute("UPDATE projects SET name=?, description=? WHERE id=?",
                      (name, description, pid))

    def delete_project(self, pid: int) -> None:
        with _connect() as c:
            c.execute("DELETE FROM projects WHERE id=?", (pid,))

    # ── Artists ───────────────────────────────────────────────

    def get_artists(self, project_id: int) -> list[dict]:
        with _connect() as c:
            return [dict(r) for r in c.execute(
                "SELECT * FROM artists WHERE project_id=? ORDER BY name", (project_id,))]

    def get_artist(self, aid: int) -> dict | None:
        with _connect() as c:
            r = c.execute("SELECT * FROM artists WHERE id=?", (aid,)).fetchone()
            return dict(r) if r else None

    def create_artist(self, project_id: int, name: str, role: str = "", email: str = "") -> int:
        with _connect() as c:
            return c.execute(
                "INSERT INTO artists (project_id, name, role, email) VALUES (?,?,?,?)",
                (project_id, name, role, email)
            ).lastrowid

    def update_artist(self, aid: int, name: str, role: str, email: str) -> None:
        with _connect() as c:
            c.execute("UPDATE artists SET name=?, role=?, email=? WHERE id=?",
                      (name, role, email, aid))

    def delete_artist(self, aid: int) -> None:
        with _connect() as c:
            c.execute("DELETE FROM artists WHERE id=?", (aid,))

    # ── Shots ─────────────────────────────────────────────────

    def get_shots(self, project_id: int) -> list[dict]:
        with _connect() as c:
            rows = c.execute(
                "SELECT * FROM shots WHERE project_id=? ORDER BY priority DESC, id",
                (project_id,)
            ).fetchall()
            result = []
            for r in rows:
                d = dict(r)
                d["history"] = json.loads(d.get("history") or "[]")
                result.append(d)
            return result

    def get_shot(self, sid: int) -> dict | None:
        with _connect() as c:
            r = c.execute("SELECT * FROM shots WHERE id=?", (sid,)).fetchone()
            if not r:
                return None
            d = dict(r)
            d["history"] = json.loads(d.get("history") or "[]")
            return d

    def create_shot(self, project_id: int, name: str, description: str = "",
                    status: str = "Pending", priority: int = 3,
                    frame_start: int = 1001, frame_end: int = 1100,
                    artist: str = "") -> int:
        with _connect() as c:
            return c.execute(
                """INSERT INTO shots
                   (project_id, name, description, status, priority, frame_start, frame_end, artist)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (project_id, name, description, status, priority, frame_start, frame_end, artist)
            ).lastrowid

    def update_shot(self, sid: int, **kwargs) -> None:
        """Update any subset of shot fields. Pass only the fields to change."""
        allowed = {"status", "priority", "notes", "folder_link",
                   "frame_start", "frame_end", "artist", "description"}
        fields = {k: v for k, v in kwargs.items() if k in allowed}
        if not fields:
            return
        sets = ", ".join(f"{k}=?" for k in fields)
        with _connect() as c:
            c.execute(f"UPDATE shots SET {sets} WHERE id=?",
                      (*fields.values(), sid))

    def append_history(self, sid: int, entry: str) -> None:
        shot = self.get_shot(sid)
        if not shot or not entry.strip():
            return
        history: list[dict] = shot["history"]
        history.insert(0, {"date": str(date.today()), "entry": entry.strip()})
        history = history[:MAX_HISTORY]
        with _connect() as c:
            c.execute("UPDATE shots SET history=? WHERE id=?",
                      (json.dumps(history), sid))

    def delete_shot(self, sid: int) -> None:
        with _connect() as c:
            c.execute("DELETE FROM shots WHERE id=?", (sid,))

    # ── Stats (for dashboard) ──────────────────────────────────

    def get_stats(self, project_id: int) -> dict:
        shots = self.get_shots(project_id)
        total = len(shots)
        counts = {}
        for s in shots:
            counts[s["status"]] = counts.get(s["status"], 0) + 1
        return {
            "total": total,
            "done": counts.get("Done", 0),
            "in_progress": counts.get("In Progress", 0),
            "review": counts.get("Review", 0),
            "hold": counts.get("Hold", 0),
            "pending": counts.get("Pending", 0),
        }
