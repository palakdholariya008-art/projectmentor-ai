import re
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator

def sanitize_text(text: str) -> str:
    if not text:
        return ""
    sanitized = re.sub(r'<[^>]*?>', '', text)
    return sanitized.strip()

class TechStackDetail(BaseModel):
    frontend: List[str] = Field(..., description="Frontend frameworks/libraries")
    backend: List[str] = Field(..., description="Backend languages and frameworks")
    database: List[str] = Field(..., description="Database storage engines")
    aiCloud: List[str] = Field(..., description="Google Cloud / AI services")

class ProjectIdea(BaseModel):
    id: str
    title: str
    tagline: str
    problemStatement: str
    solutionOverview: str
    noveltyUSP: str
    techStack: TechStackDetail
    complexity: Literal["Beginner", "Intermediate", "Advanced"]
    estimatedTimeline: str
    recommendedTeamSize: str
    academicImpactScore: int = Field(..., ge=1, le=100)
    keyFeatures: List[str]

class GenerateIdeasRequest(BaseModel):
    skills: List[str] = Field(..., min_length=1, max_length=15, description="List of student technical skills")
    domain: str = Field(..., min_length=2, max_length=60, description="Domain area of interest")
    difficulty: Literal["beginner", "intermediate", "advanced"] = "intermediate"
    teamSize: int = Field(default=1, ge=1, le=8)
    timelineWeeks: int = Field(default=12, ge=4, le=24)
    academicPreferences: Optional[str] = Field(default="", max_length=300)

    @field_validator("skills")
    @classmethod
    def validate_skills(cls, v: List[str]) -> List[str]:
        cleaned = [sanitize_text(s) for s in v if s.strip()]
        if not cleaned:
            raise ValueError("At least one valid skill is required.")
        return cleaned[:15]

    @field_validator("domain", "academicPreferences")
    @classmethod
    def validate_strings(cls, v: Optional[str]) -> str:
        return sanitize_text(v or "")

class GenerateIdeasResponse(BaseModel):
    success: bool = True
    source: Literal["gemini", "fallback"]
    ideas: List[ProjectIdea]
    count: int

class DeepDiveRequest(BaseModel):
    ideaId: str = Field(..., min_length=1, max_length=50)
    title: str = Field(..., min_length=3, max_length=150)
    problemStatement: str = Field(..., min_length=10, max_length=1000)
    techStack: List[str] = Field(..., min_length=1)
    domain: str = Field(..., min_length=2, max_length=60)
    difficulty: Literal["beginner", "intermediate", "advanced"] = "intermediate"
    timelineWeeks: int = Field(default=12, ge=4, le=24)

    @field_validator("title", "problemStatement", "domain")
    @classmethod
    def validate_fields(cls, v: str) -> str:
        return sanitize_text(v)

class SystemArchitecture(BaseModel):
    overview: str
    frontendArchitecture: str
    backendArchitecture: str
    databaseDesign: str
    securityAndAuth: str
    cloudServices: List[str]

class SprintPhase(BaseModel):
    phase: str
    weeks: str
    title: str
    deliverables: List[str]
    milestoneVerification: str

class VivaQuestion(BaseModel):
    question: str
    suggestedAnswer: str
    examinerFocus: str

class FailureMode(BaseModel):
    risk: str
    severity: Literal["High", "Medium", "Low"]
    mitigationStrategy: str

class EvaluationRubric(BaseModel):
    criteria: str
    targetScore: str
    howToScoreMax: str

class DeepDiveBlueprint(BaseModel):
    ideaId: str
    title: str
    executiveSummary: str
    systemArchitecture: SystemArchitecture
    sprintRoadmap: List[SprintPhase]
    vivaDefensePrep: List[VivaQuestion]
    failureModesAndMitigations: List[FailureMode]
    evaluationRubricMatch: List[EvaluationRubric]

class DeepDiveResponse(BaseModel):
    success: bool = True
    source: Literal["gemini", "fallback"]
    blueprint: DeepDiveBlueprint

class MentorChatRequest(BaseModel):
    projectTitle: str = Field(..., min_length=1, max_length=150)
    domain: str = Field(..., min_length=1, max_length=60)
    techStack: Optional[List[str]] = Field(default_factory=list)
    architectureSummary: Optional[str] = Field(default="", max_length=1000)
    message: str = Field(..., min_length=2, max_length=1000)
    chatHistory: Optional[List[dict]] = Field(default_factory=list)

    @field_validator("projectTitle", "domain", "architectureSummary", "message")
    @classmethod
    def validate_chat_fields(cls, v: Optional[str]) -> str:
        return sanitize_text(v or "")

class MentorChatResponse(BaseModel):
    success: bool = True
    reply: str
