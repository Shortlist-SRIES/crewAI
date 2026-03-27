# SRIES crewAI Provider Service

## Run
```bash
cd sries_provider_service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export SRIES_PROVIDER_API_KEY="change-me"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Test
```bash
curl -s http://localhost:8000/health -H "X-SRIES-API-KEY: change-me"
curl -s http://localhost:8000/sync -H "X-SRIES-API-KEY: change-me"
curl -s "http://localhost:8000/intelligence?limit=50" -H "X-SRIES-API-KEY: change-me"
curl -s -X POST http://localhost:8000/config \
  -H "content-type: application/json" \
  -H "X-SRIES-API-KEY: change-me" \
  -d '{"enabled": true, "polling_interval_seconds": 300}'
```

## SRIES backend env
- `CREWAI_BASE_URL=http://localhost:8000`
- `CREWAI_API_KEY=change-me`

SRIES backend sends:
- `X-SRIES-API-KEY: ${CREWAI_API_KEY}`
