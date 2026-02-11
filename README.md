# GitHub Manager (DevOps Mode)
AI-powered tool for sync and deployment.

## Setup
1. Copy `config.yaml.example` to `config.yaml`
2. Run `pip install -r requirements.txt`
3. Start: `python3 main.py`

## 🐳 Docker Deployment
- Build: `docker build -t github-manager .`
- Run: `docker run --env-file .env github-manager`

## 🛠️ CI/CD
- GitHub Actions automatically runs on every push to `master`.

## 🇨🇳 国产大模型适配 (Aliyun Bailian / Qwen)

The DevOps Agent supports seamless integration with domestic LLMs like Aliyun Bailian (Qwen).

### Configuration Example
1. Add Aliyun credentials to your `.env`:
   ```env
   ALIYUN_BAILIAN_API_KEY=your_sk_here
   OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
   ```
2. Check `examples/lightrag_aliyun_demo.py` for implementation details.
