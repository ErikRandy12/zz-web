from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

api = FastAPI()

# Allow cross-origin requests from your Mini App frontend
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/api/posts")
def get_posts():
    conn = sqlite3.connect("/tmp/posted_metadata.db")
    cursor = conn.cursor()
    # Pull metadata stored from scraper
    cursor.execute("SELECT video_id, title, duration, models, thumbnail FROM full_posts ORDER BY rowid DESC LIMIT 30")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": r[0],
            "title": r[1],
            "duration": r[2],
            "models": r[3],
            "thumbnail": r[4]
        }
        for r in rows
    ]
