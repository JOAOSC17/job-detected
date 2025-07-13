# 👀 Job Detected

**Your AI-powered remote job discovery tool — built for devs, by a dev.**  
Forget scrolling job boards. *Real jobs live in posts, niche platforms, and Google search hacks.*  
**Job Detected finds them for you.**

---

## 🧠 What is Job Detected?

**Job Detected** is a SaaS platform designed for remote developers (especially from Latin America or underrepresented regions) who are tired of:

- ❌ Fake job listings on major sites  
- ⌛ Wasting hours digging through LinkedIn posts, Lever, Workable, and obscure company pages  
- 🧠 Copy-pasting boolean search operators into Google every day  

**So I automated it.**

Job Detected scans **hidden job sources** using advanced search queries, parses job listings from platforms like Lever, Workable, Greenhouse, etc., and brings them together in a single beautiful UI — optionally helping you auto-generate a tailored cover letter with AI.

---

## ✅ Key Highlights

- 🔍 Smart Google & LinkedIn search automation  
  `site:lever.co "react" remote`
- 🧠 AI cover letter generation (trained with your GitHub, CV, or portfolio links)
- 📬 Email digests
- 📈 Insights on companies hiring remote devs by tech stack, country, salary range
- 📎 Save & track jobs you’ve applied to
- 🌐 Built with love using Django, React, AWS, and TypeScript

---

## ⚙️ Tech Stack

| Layer        | Stack                                   |
|--------------|-----------------------------------------|
| Frontend     | React + Tailwind CSS + TypeScript       |
| Backend      | Django + Django Rest Framework (DRF)    |
| AI Layer     | OpenAI GPT + prompt engineering         |
| Infra/Cloud  | AWS (Lambda, S3, CloudWatch, SES, etc.) |
| Data Store   | PostgreSQL + Redis                      |
| CI/CD        | GitHub Actions + AWS CodePipeline       |

---

## 🚀 Why I Built This

I’m a remote dev who realized that the **best remote jobs are buried deep** in:

- 🔍 LinkedIn posts with no job tab
- 🔗 Pages like [jobs.lever.co](https://jobs.lever.co) or [apply.workable.com](https://apply.workable.com)
- 🧠 Random Google queries like:  
  `site:jobs.lever.co "remote" "senior react developer"`

Doing this daily was painful and repetitive. So, I'm turning it into a product.  
This project is part of my **build in public** journey — follow along, contribute, or just use it!

---

## 🧪 Early Preview

The project is in active development. Here's what to expect soon:

- 🔐 Auth system (Cognito/GitHub/Google)
- 💡 Saved search filters & alerts
- ⚡ Real-time scraping via AWS Lambda + CloudWatch
- 📊 Dashboard with job insights per tech stack
- 📎 AI-powered cover letter assistant (beta)

---

## ✍️ Getting Started (Dev Setup)

```bash
# Clone repo (coming soon)
git clone https://github.com/yourusername/job-detected.git

# Backend (Django)
cd backend/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (React + Vite + Tailwind)
cd frontend/
npm install
npm run dev

```

## 💬 Community & Feedback

- 🐦 Twitter: [@jobdetected](https://twitter.com/jobdetected) (launching soon)
- 💬 Discussions: [GitHub Discussions](https://github.com/JOAOSC17/job-detected/discussions)
- 💬 Chat: Discord (coming soon)

---

## 🧩 Inspired by

- Boolean job hunting techniques
- My own frustration finding remote React + Python jobs
- Gitpod & open dev tooling
- Indie hacking + building in public community

---

## 📌 License

This project is licensed under the [MIT License](LICENSE).


Made with ❤️ by [@João Costa][https://x.com/itsjovi_dev] — from Latin America, for global devs 🌎