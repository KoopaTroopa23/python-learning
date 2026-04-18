# Python Learning Project

A professional Python learning project demonstrating backend API development, ETL data pipelines, automated testing, and full CI/CD deployment pipelines.

---

## 🚀 Live Deployment

| Service | URL |
|--------|-----|
| FastAPI REST API | https://python-learning-fpds.onrender.com |
| API Documentation (Swagger) | https://python-learning-fpds.onrender.com/docs |
| Health Check | https://python-learning-fpds.onrender.com/health |

---

## ⚙️ CI/CD Pipeline

### GitLab
- **Repository:** https://gitlab.com/DevOps-Kw/python-learning
- **Pipeline:** `.gitlab-ci.yml`
- **Stages:** Extract/Transform/Load → Test → Deploy
- Automatically triggers on every push to `main`

### Jenkins
- **Job:** `python-learning-multibranch` (Multibranch Pipeline)
- **Jenkinsfile:** Located in project root
- **Stages:** Extract Transform Load → Run Tests → Deploy to Render
- Monitors all branches automatically

### Render
- **Service:** `python-learning`
- **URL:** https://python-learning-fpds.onrender.com
- **Auto-deploys** on every successful pipeline run via deploy hook

---

## 📁 Project Structure

```
python-learning/
├── app/
│   ├── api/
│   │   ├── main.py          # FastAPI REST API
│   │   └── database.py      # SQLite database module
│   ├── basics/              # Python fundamentals practice
│   ├── etl/
│   │   └── 01_extract_transform_load_csv.py  # ETL pipeline
│   └── intermediate/        # Intermediate Python exercises
├── tests/
│   └── test_main.py         # PyTest test suite
├── terraform/               # Infrastructure as Code
├── Dockerfile               # Docker configuration
├── Jenkinsfile              # Jenkins CI/CD pipeline
├── .gitlab-ci.yml           # GitLab CI/CD pipeline
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info and available endpoints |
| GET | `/health` | Health check |
| GET | `/user/{name}` | Get user by name |
| POST | `/access` | Create user access record |
| GET | `/access` | Get all user access records |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** SQLite
- **Testing:** PyTest
- **CI/CD:** GitLab CI/CD, Jenkins
- **Deployment:** Render
- **Infrastructure:** Terraform
- **Containerization:** Docker

---

## 🏃 Run Locally

```bash
# Clone the repo
git clone https://gitlab.com/DevOps-Kw/python-learning.git
cd python-learning

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.api.main:app --reload

# Run tests
PYTHONPATH=. pytest tests/ -v

# Run ETL pipeline
python app/etl/01_extract_transform_load_csv.py
```

---

## 👤 Author

**Kevin Wingfield**
- GitLab: https://gitlab.com/DevOps-Kw
- Email: wingfield.ke@gmail.com