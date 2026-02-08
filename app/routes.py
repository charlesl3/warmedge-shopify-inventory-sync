from fastapi import APIRouter, Request
from datetime import datetime
import json
from pathlib import Path

router = APIRouter()

DATA_FILE = Path("data/inventory_events.jsonl")

@router.post("/webhooks/inventory")
async def inventory_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = None

    event = {
        "received_at": datetime.utcnow().isoformat(),
        "payload": payload
    }

    # Persist event
    DATA_FILE.parent.mkdir(exist_ok=True)
    with DATA_FILE.open("a") as f:
        f.write(json.dumps(event) + "\n")

    print("Inventory event recorded")

    return {"ok": True}
