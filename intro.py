from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI

app = FastAPI()

class Data(BaseModel):
    """request data用の型ヒントがされたクラス"""
    string: str
    default_none: Optional[int] = None
    lists: List[int]


@app.post('/post')
async def declare_request_body(data: Data):
    return {"text": f"hello, {data.string}, {data.default_none}, {data.lists}"}