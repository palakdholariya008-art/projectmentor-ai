# CapstonAI - AI Project Idea Generator & Engineering Mentor
*PromptWars x Parul University Hackathon*

CapstonAI is an intelligent, accessible, production-grade AI mentor specifically engineered to guide final-year engineering students through their entire capstone journey.

---

## 🌟 Key Features
1. **Intelligent Idea Generator (Stage 1)**: Generates 3-5 distinct, academically rigorous capstone project proposals matching student skills, team size, difficulty, and timeline.
2. **Deep-Dive Engineering Dossier (Stage 2)**: Produces an exhaustive execution blueprint including Modular System Architecture, 12-Week Milestone Sprint Roadmap, Viva/Defense Q&A, and Engineering Failure Modes & Mitigations.
3. **Interactive AI Project Mentor**: Context-aware follow-up assistant answering technical, architectural, and debugging questions.
4. **Academic Proposal Export**: Instant 1-click Print-to-PDF proposal formatting for project guide approvals.
5. **Session Caching & Resilience**: Client-side session caching with automatic deterministic academic fallbacks for 100% uptime.

---

## 🚀 Google Cloud & Services Architecture
- **AI Engine**: Google Gemini 2.5 Flash via official `@google/genai` Python SDK.
- **Serverless Hosting**: Google Cloud Run with single container deployment, auto-scaling to zero, and built-in healthcheck probes.
- **Security & A11y**: WCAG 2.1 AA compliant semantic HTML, rate-limiting (`slowapi`), XSS/Injection sanitization (`pydantic`), and security headers (`nosniff`, `DENY`).

---

## 🛠️ Local Development & Testing

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file:
```env
PORT=8080
ENVIRONMENT=development
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

### 3. Run Application
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
Open `http://localhost:8080` in your browser.

### 4. Run Automated Test Suite
```bash
pytest tests -v
```

---

## ☁️ Google Cloud Run Deployment Steps

### One-Command Deploy:
```bash
gcloud run deploy capstonai \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY="YOUR_API_KEY",ENVIRONMENT="production",GEMINI_MODEL="gemini-2.5-flash"
```