 AI 使用说明（按题目划分）

 题目一：客户筛选逻辑实现（Rule Engine）

AI 辅助部分：

协助理解题目需求，明确需要实现“多条件筛选”
提供基础的条件判断代码思路（如 >=、<= 等操作）
 给出初步函数结构示例

本人完成部分：

独立实现核心筛选逻辑（matcher.py）
实现失败原因（reasons）输出逻辑
 完成测试数据验证功能正确性

---

 题目二：YAML 配置驱动（Config Driven）

AI 辅助部分：

提供 YAML 读取方式（pyyaml 使用）
给出配置结构示例（eligibility → conditions）
协助解析 YAML 到 Python 数据结构

本人完成部分：
将规则从代码中抽离，改为 YAML 配置驱动
实现 conditions 动态加载逻辑
完成代码与配置解耦设计
验证不同规则配置的可用性

---

 题目三：API 封装（FastAPI）

AI 辅助部分：

 提供 FastAPI 基础接口模板
 协助定义请求模型（Pydantic）
 给出接口调用示例（/filter）

本人完成部分：

 将筛选逻辑封装为 API 服务
 实现接口与 YAML 配置联动（自动加载规则）
 完成接口测试（Swagger / curl）
 优化返回结构，使其具备可解释性

---

 总结

AI 主要用于：

 提高开发效率
提供代码示例与调试思路

本人主要负责：

核心逻辑实现
系统设计（Rule Engine + Config Driven）
API 整合与测试验证





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
