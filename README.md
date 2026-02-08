# Shopify Inventory Sync – Quick Runbook

This file is the **only thing you need** if you forget how to run or verify the system.

---

## Run the backend

From project root:

```bash
uvicorn app.main:app --port 8000
```

Leave this terminal open.

---

## Expose to Shopify

In a second terminal:

```bash
ngrok http 8000
```

Copy the HTTPS ngrok URL.

---

## Shopify webhook URL

Update the Shopify webhook to:

```
https://<ngrok-url>/webhooks/inventory
```

Event: **Inventory level update**

---

## How to trigger events

- Shopify → Settings → Notifications → Webhooks → **Send test**
OR
- Shopify → Products → Inventory → **Adjust quantity**

---

## Where data is recorded

Inventory events are saved to:

```
data/inventory_events.jsonl
```

If this file grows → **it is working**.

---

## If nothing happens

Check in order:

1. uvicorn is running
2. ngrok is running
3. ngrok URL matches Shopify webhook
4. Inventory is adjusted (not product name)

---

## Success criteria

You see lines like:

```json
{"inventory_item_id":123,"location_id":456,"available":9}
```

---

## Memory hook

**Run server → run ngrok → update webhook → adjust inventory → check data file**
