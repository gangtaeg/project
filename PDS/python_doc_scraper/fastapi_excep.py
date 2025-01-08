import logging
from fastapi import FastAPI, HTTPException

# 로그 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/example")
async def read_example():
    try:
        result = some_function()
        return {"message": result}
    except SomeSpecificError as e:
        logger.error(f"Specific error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")