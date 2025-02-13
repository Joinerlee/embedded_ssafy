from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI 인스턴스 생성
app = FastAPI()

# 데이터 모델 정의
class Item(BaseModel):
    name: str
    value: float

# GET 요청 처리
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# POST 요청 처리
@app.post("/items/")
async def create_item(item: Item):
    return {"received_item": item.dict()}

# 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)