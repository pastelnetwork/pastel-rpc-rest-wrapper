import asyncio
import fastapi
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from data.opennode_fastapi import ValidationError
import uvloop
from uvicorn import Config, Server
from decouple import Config as DecoupleConfig
from logger_config import setup_logger

config = DecoupleConfig(".env")
UVICORN_PORT = config.get("UVICORN_PORT", cast=int)
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
logger = setup_logger()

description_string = """
🎢 Pastel RPC Rest Wrapper: Easily access fully documented endpoints for all of the RPC methods exposed by the `pasteld` daemon. 💸
"""


app = fastapi.FastAPI(
    title="Pastel-RPC-REST-Wrapper",
    description="🎢 Easily access fully documented endpoints for all RPC methods exposed by the `pasteld` daemon. 💸",
    docs_url="/",
    redoc_url="/redoc"
)

# Custom Exception Handling Middleware
@app.middleware("http")
async def custom_exception_handling(request: Request, call_next):
    try:
        return await call_next(request)
    except ValidationError as ve:
        logger.error(f"Validation error: {ve}")
        return JSONResponse(status_code=ve.status_code, content={"detail": ve.error_msg})
    except RequestValidationError as re:
        logger.error(f"Request validation error: {re}")
        return JSONResponse(status_code=422, content={"detail": re.errors()})
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        return JSONResponse(status_code=500, content={"detail": str(e)})

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=["Authorization"]
)

async def main():
    uvicorn_config = Config(
        "main:app",
        host="0.0.0.0",
        port=UVICORN_PORT,
        loop="uvloop",
    )
    server = Server(uvicorn_config)
    await server.serve()
    

if __name__ == "__main__":
    asyncio.run(main())

