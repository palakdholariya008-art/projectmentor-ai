import pytest
from pydantic import ValidationError
from app.schemas.models import GenerateIdeasRequest, DeepDiveRequest, MentorChatRequest, sanitize_text

def test_sanitize_text():
    raw = "<script>alert('xss')</script>Hello <b>World</b>"
    clean = sanitize_text(raw)
    assert "<script>" not in clean
    assert "<b>" not in clean
    assert clean == "alert('xss')Hello World"

def test_generate_ideas_valid_request():
    req = GenerateIdeasRequest(
        skills=["Python", "FastAPI", "Docker"],
        domain="Artificial Intelligence",
        difficulty="intermediate",
        teamSize=3,
        timelineWeeks=12,
        academicPreferences="Focus on Cloud Run"
    )
    assert len(req.skills) == 3
    assert req.domain == "Artificial Intelligence"
    assert req.teamSize == 3

def test_generate_ideas_empty_skills_fails():
    with pytest.raises(ValidationError):
        GenerateIdeasRequest(
            skills=[],
            domain="Web Development"
        )

def test_generate_ideas_invalid_difficulty():
    with pytest.raises(ValidationError):
        GenerateIdeasRequest(
            skills=["React"],
            domain="Web Dev",
            difficulty="impossible"  # type: ignore
        )

def test_deep_dive_valid_request():
    req = DeepDiveRequest(
        ideaId="idea-101",
        title="AI Medical Triage Assistant",
        problemStatement="Emergency rooms lack rapid automated diagnostic sorting for non-critical incoming patients.",
        techStack=["React", "FastAPI", "Gemini 2.5 Flash"],
        domain="Healthcare AI",
        difficulty="advanced",
        timelineWeeks=16
    )
    assert req.ideaId == "idea-101"
    assert req.difficulty == "advanced"

def test_deep_dive_short_problem_statement_fails():
    with pytest.raises(ValidationError):
        DeepDiveRequest(
            ideaId="idea-101",
            title="Short Problem",
            problemStatement="Too short",
            techStack=["Python"],
            domain="AI"
        )

def test_mentor_chat_valid_request():
    req = MentorChatRequest(
        projectTitle="Smart Parking Edge System",
        domain="IoT & Cloud",
        message="How do I connect MQTT sensors to Cloud Run?",
        techStack=["Python", "MQTT", "Cloud Run"]
    )
    assert req.projectTitle == "Smart Parking Edge System"
    assert "MQTT" in req.message
