import json
import logging
from typing import Tuple, List
from google import genai
from google.genai import types

from app.core.config import settings
from app.schemas.models import (
    GenerateIdeasRequest, ProjectIdea, TechStackDetail,
    DeepDiveRequest, DeepDiveBlueprint, SystemArchitecture, SprintPhase,
    VivaQuestion, FailureMode, EvaluationRubric, MentorChatRequest
)
from app.services.fallbacks import get_fallback_ideas, get_fallback_deep_dive

logger = logging.getLogger("capstonai.gemini")

_client = None

def get_genai_client():
    global _client
    if _client is None:
        if not settings.GEMINI_API_KEY:
            logger.warning("GEMINI_API_KEY is not set. All AI operations will gracefully use deterministic academic fallbacks.")
            return None
        _client = genai.Client(api_key=settings.GEMINI_API_KEY)
    return _client

async def generate_project_ideas_service(payload: GenerateIdeasRequest) -> Tuple[List[ProjectIdea], str]:
    client = get_genai_client()
    if not client:
        return get_fallback_ideas(payload.domain, payload.skills), "fallback"

    skills_joined = ", ".join(payload.skills)
    prompt = f"""You are a distinguished Senior Principal Engineer, University Capstone Evaluator, and Hackathon Mentor.
Generate 3 to 4 distinct, high-impact, academically rigorous, and recruiter-impressive final-year capstone project ideas.

Student Profile:
- Skills & Technologies: {skills_joined}
- Domain Interest: {payload.domain}
- Desired Difficulty: {payload.difficulty}
- Team Size: {payload.teamSize} student(s)
- Project Timeline: {payload.timelineWeeks} weeks
- Academic Preferences: {payload.academicPreferences or "Must have practical real-world utility and sound academic rigor."}

Requirements:
1. NO generic clone ideas (e.g. basic e-commerce, simple chat, generic to-do apps).
2. Every idea must address a real-world problem with modern architectures (e.g. edge computing, Gemini AI, cloud services, resilient workflows).
3. The tech stack MUST leverage the student's skills while introducing 1-2 industry-standard modern tools.
4. Provide realistic timelines and clear novelty USP.
5. Return strictly valid JSON adhering to the required schema."""

    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=list[ProjectIdea],
                temperature=0.7
            )
        )
        if not response.text:
            raise ValueError("Empty response text from Gemini API")
        
        parsed_ideas = json.loads(response.text)
        if isinstance(parsed_ideas, list) and len(parsed_ideas) > 0:
            validated = [ProjectIdea.model_validate(item) for item in parsed_ideas]
            return validated, "gemini"
        elif isinstance(parsed_ideas, dict) and "ideas" in parsed_ideas:
            validated = [ProjectIdea.model_validate(item) for item in parsed_ideas["ideas"]]
            return validated, "gemini"
        raise ValueError("Invalid JSON structure returned by Gemini")
    except Exception as exc:
        logger.warning(f"Gemini idea generation failed/fallback engaged: {exc}")
        return get_fallback_ideas(payload.domain, payload.skills), "fallback"

async def generate_deep_dive_service(payload: DeepDiveRequest) -> Tuple[DeepDiveBlueprint, str]:
    client = get_genai_client()
    if not client:
        return get_fallback_deep_dive(payload.title, payload.domain), "fallback"

    stack_str = ", ".join(payload.techStack)
    prompt = f"""You are an elite Engineering Mentor and Final-Year Project Viva Examiner.
Produce an exhaustive, highly structured, production-ready execution and viva defense blueprint for the following capstone project:

Project Details:
- Title: {payload.title}
- Problem Statement: {payload.problemStatement}
- Target Tech Stack: {stack_str}
- Domain: {payload.domain}
- Difficulty Level: {payload.difficulty}
- Total Timeline: {payload.timelineWeeks} Weeks

Generate:
1. Executive Summary: Academic significance and engineering novelty.
2. System Architecture: Breakdown of Frontend, Backend, Database schemas, Security considerations, and Cloud integration (specifically highlighting Google Cloud Run and Gemini opportunities).
3. Sprint Roadmap: A 4-phase milestone plan mapped across {payload.timelineWeeks} weeks with concrete deliverables and verification checks.
4. Viva / Defense Preparation: 3-4 realistic academic viva questions with model answers and tips on examiner focus.
5. Failure Modes & Mitigations: 3 critical engineering failure scenarios and proactive fixes.
6. Evaluation Rubric Match: Clear guidelines to maximize score in University grading rubrics.

Return strictly valid JSON adhering to the schema."""

    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=DeepDiveBlueprint,
                temperature=0.6
            )
        )
        if not response.text:
            raise ValueError("Empty response text from Gemini API")
        
        parsed = json.loads(response.text)
        validated = DeepDiveBlueprint.model_validate(parsed)
        return validated, "gemini"
    except Exception as exc:
        logger.warning(f"Gemini deep dive generation failed/fallback engaged: {exc}")
        return get_fallback_deep_dive(payload.title, payload.domain), "fallback"

async def generate_mentor_advice_service(payload: MentorChatRequest) -> str:
    client = get_genai_client()
    if not client:
        return f"Mentor Advice for '{payload.projectTitle}': Focus on building a minimal working prototype first. Make sure your core API endpoints and schema validation are working reliably before adding advanced AI integrations. What specific architectural layer would you like to review next?"

    history_str = "\n".join([f"{msg.get('role', 'User')}: {msg.get('content', '')}" for msg in payload.chatHistory[-6:]]) if payload.chatHistory else "No prior messages."
    prompt = f"""You are a supportive, highly technical Senior AI & Cloud Mentor for a university final-year engineering student.

Current Project Context:
- Title: {payload.projectTitle}
- Domain: {payload.domain}
- Tech Stack: {', '.join(payload.techStack) if payload.techStack else 'Modern Web/Cloud Stack'}
- Architecture: {payload.architectureSummary or 'Containerized Cloud Run Architecture'}

Recent Conversation:
{history_str}

Student's Latest Question:
{payload.message}

Provide clear, actionable, encouraging technical guidance. Include concrete code patterns, architectural tips, or debugging steps where appropriate."""

    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7
            )
        )
        return response.text or "I am ready to help you build and refine your capstone project! What specific component or feature would you like to explore next?"
    except Exception as exc:
        logger.warning(f"Gemini mentor chat failed/fallback engaged: {exc}")
        return f"Mentor Advice for '{payload.projectTitle}': Let's break down this problem systematically. Start with clear API contracts, test your database queries locally, and verify your Cloud Run configuration. What specific error or question are you facing?"
