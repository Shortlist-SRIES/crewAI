from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

API_KEY = os.getenv('SRIES_PROVIDER_API_KEY')

# Pydantic Models
class NormalizedIntelligenceRecord(BaseModel):
    data: str

class ProviderHealth(BaseModel):
    status: str

class SyncMetadata(BaseModel):
    last_sync: str

# Middleware for API Key
async def api_key_required(x_sries_api_key: str = Depends()):
    if x_sries_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

@app.get('/health', dependencies=[Depends(api_key_required)])
async def health():
    return ProviderHealth(status='healthy')

@app.get('/sync', dependencies=[Depends(api_key_required)])
async def sync():
    return SyncMetadata(last_sync='2026-03-27T12:28:52')

@app.get('/intelligence', dependencies=[Depends(api_key_required)])
async def intelligence(limit: Optional[int] = None, since: Optional[str] = None):
    return NormalizedIntelligenceRecord(data='Sample data')

@app.post('/config', dependencies=[Depends(api_key_required)])
async def config(record: NormalizedIntelligenceRecord):
    return {'message': 'Config updated'}
