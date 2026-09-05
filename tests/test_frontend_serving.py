import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_frontend_serving_index():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert "<title>CapstonAI" in response.text
        assert "Google Cloud Run" in response.text
        assert "Gemini 2.5" in response.text

@pytest.mark.asyncio
async def test_frontend_accessibility_elements():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        # Check skip-link
        assert "Skip to main content" in response.text
        # Check ARIA live announcer
        assert 'aria-live="polite"' in response.text
        # Check semantic elements
        assert "<header" in response.text
        assert "<main" in response.text
        assert "<footer" in response.text