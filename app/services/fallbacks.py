from typing import List
from app.schemas.models import ProjectIdea, TechStackDetail, DeepDiveBlueprint, SystemArchitecture, SprintPhase, VivaQuestion, FailureMode, EvaluationRubric

def get_fallback_ideas(domain: str, skills: List[str]) -> List[ProjectIdea]:
    return [
        ProjectIdea(
            id="idea-fallback-1",
            title="Fake Degree & Certificate Detector (AI Document Verifier)",
            tagline="Instantly scans uploaded marksheets & certificates using AI to catch forged signatures, altered grades, and fake college seals.",
            problemStatement="Institutions and tech recruiters waste hundreds of hours manually verifying academic certificates and transcripts, risking fake resume submissions and credential forgery.",
            solutionOverview="A zero-trust platform combining cryptographic certificate hashing on an immutable ledger with Google Gemini Multimodal OCR to instantly detect manipulated seals, altered grades, and fraudulent signatures.",
            noveltyUSP="Combines decentralized hash attestation with automated multi-modal vision anomaly grading for instant zero-knowledge employer checks.",
            techStack=TechStackDetail(
                frontend=["React", "TailwindCSS", "TypeScript"],
                backend=["FastAPI / Node.js", "Python / TypeScript"],
                database=["PostgreSQL", "Cloud Firestore"],
                aiCloud=["Google Gemini 2.5 Flash", "Google Cloud Run"]
            ),
            complexity="Intermediate",
            estimatedTimeline="12 Weeks",
            recommendedTeamSize="2 - 4 Students",
            academicImpactScore=94,
            keyFeatures=[
                "Instant cryptographic credential issuance and QR-code verification portal",
                "Gemini Multimodal OCR visual tamper and signature forgery detection",
                "Role-based dashboards for University Registrars, Students, and Enterprise Recruiters",
                "Public verification REST API with rate-limiting and audit logging"
            ]
        ),
        ProjectIdea(
            id="idea-fallback-2",
            title="AI Mock Viva Examiner & Voice Interview Coach",
            tagline="Practice your final-year college viva exam with an AI examiner that asks real technical questions, grades your answers, and points out weak areas.",
            problemStatement="Engineering students frequently suffer high anxiety and poor performance in final-year viva defense sessions due to lack of realistic, personalized mock examination practice.",
            solutionOverview="An intelligent examiner engine that ingests syllabus outcomes and capstone project blueprints to conduct adaptive Socratic cross-examinations, pinpointing conceptual weak spots in real time.",
            noveltyUSP="Dynamic Bloom-Taxonomy difficulty adjustment with real-time scoring rubrics tailored specifically to Indian university examination guidelines.",
            techStack=TechStackDetail(
                frontend=["React / Vite", "TailwindCSS", "Web Speech API"],
                backend=["FastAPI", "Python 3.14"],
                database=["SQLite / PostgreSQL"],
                aiCloud=["Google Gemini 2.5 Flash", "Google Cloud Run"]
            ),
            complexity="Intermediate",
            estimatedTimeline="10 Weeks",
            recommendedTeamSize="2 - 3 Students",
            academicImpactScore=91,
            keyFeatures=[
                "Interactive voice and text mock viva simulation with structured rubric scoring",
                "Real-time student knowledge-gap heatmaps based on Bloom's Cognitive Taxonomy",
                "Instant weakness remediation sprint generator with curated learning links",
                "Faculty / Guide progress monitoring dashboard for student cohorts"
            ]
        ),
        ProjectIdea(
            id="idea-fallback-3",
            title="Smart College Electricity & AC Power Saver (IoT + AI)",
            tagline="Automatically turns off empty classroom lights and ACs using sensors and AI predictions to cut college electricity bills by 30%.",
            problemStatement="Academic institutions waste up to 35% of power annually through unmanaged laboratory air conditioning, auditorium lighting, and idle computing clusters.",
            solutionOverview="A unified edge-IoT telemetry network feeding real-time occupancy and power metrics into a predictive AI model that automates HVAC schedules and detects electrical anomalies.",
            noveltyUSP="Hybrid edge-to-cloud computing pipeline featuring sub-second sensor anomaly classification and Gemini natural language root-cause explanation reports.",
            techStack=TechStackDetail(
                frontend=["React", "Chart.js", "TailwindCSS"],
                backend=["FastAPI / Python", "MQTT Broker"],
                database=["TimescaleDB / PostgreSQL"],
                aiCloud=["Google Cloud Run", "Google Cloud Logging", "Gemini Flash"]
            ),
            complexity="Advanced",
            estimatedTimeline="14 Weeks",
            recommendedTeamSize="3 - 4 Students",
            academicImpactScore=96,
            keyFeatures=[
                "Sub-second IoT telemetry ingestion pipeline with live energy telemetry stream",
                "Automated AI load scheduling algorithm reducing peak power charges by 20%+",
                "Automated ESG and Carbon footprint compliance report generator for academic audits",
                "Fault predictive maintenance alerts with severity ranking and action guides"
            ]
        )
    ]

def get_fallback_deep_dive(idea_title: str, domain: str) -> DeepDiveBlueprint:
    return DeepDiveBlueprint(
        ideaId="deep-dive-verified-plan",
        title=idea_title or "Enterprise AI Capstone Engineering Dossier",
        executiveSummary=f"An academically rigorous and industry-aligned 12-week blueprint engineered to design, build, test, and defend '{idea_title}' within the {domain or 'Computer Engineering'} domain.",
        systemArchitecture=SystemArchitecture(
            overview="A highly resilient, containerized micro-architecture deployed on Google Cloud Run with automated horizontal scaling, zero-trust input sanitization, and structured AI response pipelines.",
            frontendArchitecture="Component-driven Single Page Application built with React, Vite, and WCAG 2.1 AA accessible Tailwind styling, featuring client-side session caching to eliminate redundant API calls.",
            backendArchitecture="High-performance asynchronous REST API built on FastAPI / Python 3.14 with Pydantic v2 data validation, slowapi rate-limiting, and comprehensive error masking.",
            databaseDesign="Normalized relational schema with indexing on foreign keys and audit logs, ensuring ACID compliance and zero data leakage.",
            securityAndAuth="Stateless security architecture with helmet headers, CORS restrictions, strict prompt-injection delimiters, and zero client-side API key leakage.",
            cloudServices=["Google Cloud Run (Serverless Hosting)", "Google Gemini API (Flash Model)", "Google Cloud Build (CI/CD)", "Google Cloud Logging & Monitoring"]
        ),
        sprintRoadmap=[
            SprintPhase(
                phase="Phase 1: Research, Architecture & Prototyping",
                weeks="Weeks 1 - 3",
                title="SRS Specification, Database Design & Cloud Run Baseline",
                deliverables=[
                    "Complete IEEE Software Requirements Specification (SRS) document",
                    "Entity-Relationship (ER) diagram and OpenAPI 3.0 contract specification",
                    "Cloud Run Docker container deployment with live /api/health probe"
                ],
                milestoneVerification="Working skeleton API running live on Google Cloud Run with automated CI/CD and passing healthcheck."
            ),
            SprintPhase(
                phase="Phase 2: Core Engineering & AI Engine Integration",
                weeks="Weeks 4 - 7",
                title="Business Logic Implementation & Gemini API Integration",
                deliverables=[
                    "Core database migrations and CRUD service layer implementation",
                    "Structured Google Gemini API integration with JSON schema enforcement and backoff retries",
                    "Responsive frontend interface with accessible keyboard navigation and state management"
                ],
                milestoneVerification="End-to-end user workflow validated with automated unit tests achieving >85% code coverage."
            ),
            SprintPhase(
                phase="Phase 3: Hardening, Rate-Limiting & Security Audit",
                weeks="Weeks 8 - 10",
                title="Security Hardening, Session Caching & Performance Tuning",
                deliverables=[
                    "Input sanitization filters preventing prompt injection and XSS exploits",
                    "Client-side caching layer preventing redundant AI token usage",
                    "Comprehensive load testing and sub-800ms response time optimization"
                ],
                milestoneVerification="Clean OWASP security audit, zero high-severity vulnerabilities, robust rate-limiting active."
            ),
            SprintPhase(
                phase="Phase 4: Academic Defense, Viva Prep & Documentation",
                weeks="Weeks 11 - 12",
                title="Viva Mock Defense, IEEE Report & Live Demonstration",
                deliverables=[
                    "Final University Capstone Project Report following academic IEEE guidelines",
                    "Examiner slide deck with live Cloud Run URL demo and benchmark charts",
                    "Viva Q&A rehearsal dossier addressing theoretical and architectural inquiries"
                ],
                milestoneVerification="Flawless live demonstration on public Google Cloud Run link and high rubric scoring alignment."
            )
        ],
        vivaDefensePrep=[
            VivaQuestion(
                question="What architectural advantages does your Google Cloud Run deployment offer over traditional VM or hosting providers?",
                suggestedAnswer="Google Cloud Run provides serverless container execution that scales to zero when idle (eliminating ongoing compute costs) and rapidly scales out during traffic bursts. It enforces HTTPS, integrates natively with Google Cloud IAM and Logging, and isolates every request inside a gVisor sandboxed container for superior security.",
                examinerFocus="Assessing understanding of modern cloud infrastructure, scalability, cost optimization, and virtualization security."
            ),
            VivaQuestion(
                question="How does your system prevent Prompt Injection and ensure deterministic JSON responses from Gemini?",
                suggestedAnswer="We apply a defense-in-depth approach: (1) Inputs are sanitized using Pydantic regex filters, (2) User parameters are enclosed in strict delimiters with system-level instruction guarding, (3) The Gemini SDK is configured with strict responseSchema parameters, and (4) Responses are validated against Pydantic models before rendering.",
                examinerFocus="Evaluating modern LLM security knowledge (OWASP LLM Top 10) and robust defensive software engineering."
            ),
            VivaQuestion(
                question="How do you handle external AI service latency or quota exhaustion during peak usage?",
                suggestedAnswer="We engineered a dual-tier resilience strategy: client-side session caching completely prevents duplicate API calls for previously inspected projects, while our backend features an automatic exponential backoff retry loop coupled with an instant deterministic academic fallback engine.",
                examinerFocus="Testing system reliability, fault-tolerance, and graceful degradation principles."
            )
        ],
        failureModesAndMitigations=[
            FailureMode(
                risk="Gemini API Rate Limit (HTTP 429) or Service Outage during final viva demonstration",
                severity="High",
                mitigationStrategy="Automated fallback to verified offline academic blueprint repository ensures 100% uptime with clear indicator badge."
            ),
            FailureMode(
                risk="Cold-start container latency on serverless hosting",
                severity="Medium",
                mitigationStrategy="Lightweight container image with pre-warmed dependencies and efficient async event loop keeps startup latency under 800ms."
            ),
            FailureMode(
                risk="Malicious or oversized input payload attempting Denial of Service",
                severity="Medium",
                mitigationStrategy="Slowapi rate-limiter (30 requests / 15 mins) and strict Pydantic max_length constraints reject oversized inputs immediately at the gateway layer."
            )
        ],
        evaluationRubricMatch=[
            EvaluationRubric(
                criteria="Problem Definition, Novelty & Industry Relevance",
                targetScore="10 / 10",
                howToScoreMax="Clearly demonstrate why existing approaches fall short and how the multi-modal Gemini AI integration delivers measurable efficiency gains."
            ),
            EvaluationRubric(
                criteria="Software Architecture, Testing & Code Quality",
                targetScore="20 / 20",
                howToScoreMax="Showcase modular codebase, comprehensive automated test suite (>85% coverage), and clean separation of concerns."
            ),
            EvaluationRubric(
                criteria="Google Cloud Services Integration & Production Deployment",
                targetScore="20 / 20",
                howToScoreMax="Demonstrate live, responsive execution on Google Cloud Run with zero-downtime healthcheck probes and secure environment management."
            )
        ]
    )
