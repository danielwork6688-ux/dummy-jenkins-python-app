# Dummy Jenkins Python App

App Flask đơn giản để học Jenkins pipeline, chạy test tự động và build Docker image.

## Chạy local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Mở:

- `http://localhost:5000/`
- `http://localhost:5000/health`
- `http://localhost:5000/api/greet?name=Jenkins`

Trên Windows PowerShell, kích hoạt môi trường ảo bằng:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Chạy test

```bash
pytest -v
```

## Chạy bằng Docker

```bash
docker build -t dummy-jenkins-python-app .
docker run --rm -p 5000:5000 dummy-jenkins-python-app
```

## Gợi ý Jenkins

1. Push repo này lên GitHub.
2. Tạo Jenkins Pipeline job.
3. Chọn `Pipeline script from SCM`.
4. SCM: Git.
5. Repository URL: URL GitHub repo của bạn.
6. Branch: `main` hoặc branch bạn dùng.
7. Script Path: `Jenkinsfile`.

Pipeline hiện tại gồm:

- Checkout source code.
- Tạo Python virtual environment.
- Cài dependencies.
- Chạy `pytest`.
- Build Docker image.

Lưu ý: stage build Docker cần Jenkins agent có Docker CLI và quyền chạy Docker.
