# Understand Image

一个 Claude Code Skill，让 Agent 可以使用兼容 OpenAI Responses API 的视觉模型来查看图片，并回答关于图片的问题。

这个仓库的设计目标是让 Agent 自己安装。作为人类用户，你通常只需要把下面这个仓库地址交给 Agent，并让它安装这个 Skill：

```text
https://github.com/PageGeorge/understand-image-skill
```

安装过程中，Agent 应该向你询问所需的 API key、base URL 和模型名称，然后把这些值写入本地安装后的 Skill 副本。

## 功能

- 接受本地图片路径或 HTTP(S) 图片 URL。
- 将图片和自然语言问题发送给视觉模型。
- 将模型回答返回给 Agent。
- 兼容提供 OpenAI Responses API 格式端点的服务商。

支持的图片格式：PNG、JPG、JPEG、GIF、WebP。

## 给用户

请让你的 Agent 使用上面的仓库地址安装这个 Skill。

Agent 会需要你提供三个值：

| 值 | 说明 |
|---|---|
| API key | 你的服务商 API key |
| Base URL | 兼容 OpenAI 的 API 端点，例如 `https://ark.cn-beijing.volces.com/api/v3` |
| 模型名称 | 支持视觉输入的模型标识，例如 `doubao-seed-2-0-pro-260215` |

安装完成后，你只需要提供图片并提出问题。当 Agent 看到图片路径或 URL，并且任务需要理解图片内容时，这个 Skill 应该会自动触发。

## 给 Agent

将 `understand-image` 文件夹安装到用户的 Claude Code skills 目录。

个人级安装：

```bash
cp -r understand-image ~/.claude/skills/
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -r understand-image .claude/skills/
```

如果 Python 依赖尚未安装，请安装 OpenAI SDK：

```bash
python3 -m pip install openai
```

如果用户电脑上只有 `python`，并且它指向 Python 3，可以把下面命令中的 `python3` 替换为 `python`。

然后配置本地已安装的副本，替换 `understand-image/scripts/vision.py` 中的这些占位符：

| 占位符 | 替换为 |
|---|---|
| `{API_KEY}` | 用户的 API key |
| `{BASE_URL}` | 用户的 OpenAI 兼容 base URL |
| `{MODEL_NAME}` | 用户的视觉模型名称 |

写入凭据后，不要提交或发布用户本地配置过的 `vision.py`。

安装完成后重启 Claude Code，让 Skill 被重新发现。

## 验证

配置完成后运行：

```bash
python3 ~/.claude/skills/understand-image/scripts/vision.py "IMAGE_PATH_OR_URL" "Describe this image."
```

如果是项目级安装，请调整路径：

```bash
python3 .claude/skills/understand-image/scripts/vision.py "IMAGE_PATH_OR_URL" "Describe this image."
```

如果 `python3` 不可用，请先确认 `python` 是 Python 3，再用 `python` 替代 `python3`。

如果脚本返回了图片描述，说明 Skill 已经可以使用。

## 工作方式

这个 Skill 提供了一个小型 Python 辅助脚本：

```text
understand-image/scripts/vision.py
```

对于本地文件，脚本会将图片编码为 base64，并以 data URL 的形式发送给模型。对于 HTTP(S) URL，脚本会直接将图片 URL 传给模型。请求使用 OpenAI Python SDK 的 `client.responses.create(...)`。

## 安全提醒

- 只在用户本地安装后的副本中配置凭据。
- 不要把配置后的 API key 推送回 GitHub。
- 如果模型调用失败，请确认所选模型是否支持通过 Responses API 输入图片。
