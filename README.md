# Rule-Based Customer Filtering API (AI Agent Style)

A production-style rule engine system for customer eligibility filtering, built with FastAPI and YAML-driven configuration.

Supports:

* Config-driven rules (YAML)
* Explainable filtering results
* API-based invocation (Agent-ready tool)
Architecture

Client Request
↓
FastAPI (/filter)
↓
Load Rules (skill.yaml)
↓
Rule Engine (matcher.py)
↓
Return Results (matched / unmatched + reasons)

markdown
# Customer Filter AI Agent
📌 基于规则引擎的客户筛选系统，YAML配置驱动 + FastAPI接口化。

## 技术栈
Python、FastAPI、PyYAML、Pydantic

## 项目结构
ai-customer-filter-agent/
├── api.py # FastAPI 接口服务
├── matcher.py # 规则引擎核心
├── skill.yaml # 筛选规则配置
├── test.py # 本地测试脚本
├── requirements.txt # 依赖清单
└── README.md # 项目说明
plaintext

## 启动方式
1. 安装依赖：pip install -r requirements.txt
2. 启动服务：uvicorn api:app --reload
3. 测试接口：http://127.0.0.1:8000/docs

## API调用示例
POST /filter
```json
{
  "customers": [
    {"name": "张三", "business_years": 3, "monthly_revenue": 250000},
    {"name": "李四", "business_years": 1, "monthly_revenue": 180000}
  ]
}
plaintext
- Ctrl+S保存。

### 📍 最终验证
打开`ai-customer-filter-agent`文件夹，确认有以下6个文件：
ai-customer-filter-agent/
├── api.py
├── matcher.py
├── skill.yaml
├── test.py
├── requirements.txt
└── README.md
