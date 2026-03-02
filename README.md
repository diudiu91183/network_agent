# 网络故障诊断 Agent

一个基于 AI 的网络故障诊断系统，结合 LangChain 框架和大语言模型，能够理解和处理用户的自然语言网络问题描述，并通过模拟的网络工具进行诊断分析。

## 功能特性

- **自然语言交互**: 用户可以用日常语言描述网络问题，如"我无法访问 www.example.com"
- **智能诊断**: AI Agent 自动分析问题并决定使用合适的诊断工具
- **多工具集成**: 内置模拟的 `ping`, `dns`, `interface_check`, `log_analysis` 等网络诊断工具
- **可视化界面**: 提供 Streamlit Web 界面，实时显示诊断过程和最终结果

## 系统架构

- `network_diagnosis_agent.py`: 核心 AI Agent 逻辑，定义工具和诊断流程
- `main.py`: Streamlit Web 界面，提供用户交互入口
- `requirements.txt`: 项目 Python 依赖

## 依赖要求

- Python >= 3.8
- dashscope==1.22.1
- langchain==1.0.2
- langchain_community==0.4
- streamlit

## 安装部署

1. 克隆项目到本地
2. 安装依赖包：
```
pip install -r requirements.txt
```

3. 配置环境变量：
```
export DASHSCOPE_API_KEY="your_dashscope_api_key"
```

4. 启动 Web 界面：
```
streamlit run main.py
```

## 使用方法

1. 启动应用后，在浏览器打开 `http://localhost:8501`
2. 在文本框中输入你的网络问题描述
3. 点击"开始诊断"按钮
4. 观察实时诊断过程和最终结果

## 核心诊断工具

- **Ping Tool**: 检查网络连通性和延迟
- **DNS Tool**: 解析域名到 IP 地址
- **Interface Check Tool**: 检查本地网络接口状态
- **Log Analysis Tool**: 分析系统日志中的网络错误

## 技术栈

- LangChain: 构建 AI Agent 框架
- DashScope: 通义千问语言模型
- Streamlit: Web 界面框架