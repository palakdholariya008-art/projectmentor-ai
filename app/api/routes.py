from fastapi import APIRouter, Request, HTTPException, status
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.config import settings
from app.schemas.models import (
    GenerateIdeasRequest, GenerateIdeasResponse,
    DeepDiveRequest, DeepDiveResponse,
    MentorChatRequest, MentorChatResponse
)
from app.services.gemini_service import (
    generate_project_ideas_service,
    generate_deep_dive_service,
    generate_mentor_advice_service
)

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix=settings.API_PREFIX)

@router.get("/health", tags=["Monitoring"])
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "geminiConfigured": bool(settings.GEMINI_API_KEY)
    }

@router.post("/generate-ideas", response_model=GenerateIdeasResponse, tags=["AI Capstone Engine"])
@limiter.limit(settings.RATE_LIMIT_GENERATE)
async def generate_ideas(request: Request, payload: GenerateIdeasRequest):
    try:
        ideas, source = await generate_project_ideas_service(payload)
        return GenerateIdeasResponse(
            success=True,
            source=source,
            ideas=ideas,
            count=len(ideas)
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate project ideas: {str(exc)}"
        )

@router.post("/deep-dive", response_model=DeepDiveResponse, tags=["AI Capstone Engine"])
@limiter.limit(settings.RATE_LIMIT_GENERATE)
async def deep_dive(request: Request, payload: DeepDiveRequest):
    try:
        blueprint, source = await generate_deep_dive_service(payload)
        return DeepDiveResponse(
            success=True,
            source=source,
            blueprint=blueprint
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate deep dive blueprint: {str(exc)}"
        )

@router.post("/mentor-chat", response_model=MentorChatResponse, tags=["AI Mentor Chat"])
@limiter.limit(settings.RATE_LIMIT_STANDARD)
async def mentor_chat(request: Request, payload: MentorChatRequest):
    try:
        reply = await generate_mentor_advice_service(payload)
        return MentorChatResponse(
            success=True,
            reply=reply
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch mentor advice: {str(exc)}"
        )
