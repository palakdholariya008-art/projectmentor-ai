import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_health_check():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "CapstonAI" in data["service"]

@pytest.mark.asyncio
async def test_generate_ideas_endpoint_stateless_fallback():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "skills": ["React", "Node.js", "PostgreSQL"],
            "domain": "FinTech & Security",
            "difficulty": "intermediate",
            "teamSize": 2,
            "timelineWeeks": 12
        }
        response = await client.post("/api/generate-ideas", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert len(data["ideas"]) >= 3
        first = data["ideas"][0]
        assert "title" in first
        assert "problemStatement" in first
        assert "techStack" in first
        assert "academicImpactScore" in first

@pytest.mark.asyncio
async def test_deep_dive_endpoint_stateless_fallback():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "ideaId": "idea-test-01",
            "title": "SmartAudit: Decentralized AI Academic Credential Verifier",
            "problemStatement": "Institutions spend weeks verifying academic credentials manually.",
            "techStack": ["React", "FastAPI", "Gemini 2.5 Flash", "Cloud Run"],
            "domain": "Education & Security",
            "difficulty": "intermediate",
            "timelineWeeks": 12
        }
        response = await client.post("/api/deep-dive", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        bp = data["blueprint"]
        assert "systemArchitecture" in bp
        assert len(bp["sprintRoadmap"]) >= 4
        assert len(bp["vivaDefensePrep"]) >= 3
        assert len(bp["failureModesAndMitigations"]) >= 3

@pytest.mark.asyncio
async def test_mentor_chat_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "projectTitle": "SmartAudit",
            "domain": "Education & Security",
            "techStack": ["FastAPI", "Cloud Run"],
            "message": "What is the best way to handle certificate hashing?"
        }
        response = await client.post("/api/mentor-chat", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert len(data["reply"]) > 20

@pytest.mark.asyncio
async def test_security_headers_present():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
        assert response.headers.get("X-Content-Type-Options") == "nosniff"
        assert response.headers.get("X-Frame-Options") == "DENY"
        assert "1; mode=block" in response.headers.get("X-XSS-Protection", "")
