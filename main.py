from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.database import engine, Base
from backend.app.routers import health, emotion, conversation, rewrite, evaluation

# Initialize SQLite database schemas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for EmpathAI - Emotion Drift Assisted Communication System powered by Hugging Face Transformers and Generative AI."
)

# Configure Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local development flexibility
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(health.router, prefix="/api/v1")
app.include_router(emotion.router, prefix="/api/v1/emotion")
app.include_router(conversation.router, prefix="/api/v1/conversation")
app.include_router(rewrite.router, prefix="/api/v1/rewrite")
app.include_router(evaluation.router, prefix="/api/v1/evaluation")

@app.get("/")
def root():
    return {
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs_url": "/docs",
        "api_prefix": "/api/v1",
        "status": "online"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
