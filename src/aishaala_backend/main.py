import logging
import uvicorn

logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

def main():
    from aishaala_backend import settings
    port = settings.API_PORT
    logger.info(f"Running the FastAPI server on port {port}.")
    uvicorn.run("aishaala_backend.app:app", host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
