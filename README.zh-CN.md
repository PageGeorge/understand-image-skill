# Understand Image

一个 Claude Code Skill，通过兼容 OpenAI Responses API 的视觉模型实现图片理解。

## API

使用 OpenAI Responses API 格式（`client.responses.create`），兼容所有提供此端点的服务商。

## 配置

使用前，替换 `understand_image/scripts/vision.py` 中的占位符：

| 占位符 | 说明 |
|---|---|
| `{API_KEY}` | 你的 API 密钥 |
| `{BASE_URL}` | API 请求地址（如 `https://ark.cn-beijing.volces.com/api/v3`） |
| `{MODEL_NAME}` | 模型名称（如 `doubao-seed-2-0-pro-260215`） |

## 安装

将 `understand_image` 文件夹复制到 Claude Code 的 skills 目录：

```bash
# 个人级别（所有项目可用）
cp -r understand_image ~/.claude/skills/

# 或项目级别
cp -r understand_image .claude/skills/
```

然后重启 Claude Code。当你提供图片并提问时，Skill 会自动触发；也可以手动调用 `/understand_image`。

## 使用

提供一张图片（本地路径或 URL）并提问，Claude 会根据你的意图自动构造合适的问题发送给视觉模型。

## 支持格式

PNG、JPG、GIF、WebP。
