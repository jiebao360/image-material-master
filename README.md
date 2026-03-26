# 图片素材生成大师 (Image Material Master)

🎨 **全能图片素材生成工具** - 整合即梦 AI、Nano Banana Pro、Seedance 的完整工作流

## ✨ 特性

- 🚀 **多引擎支持**：即梦 AI / Nano Banana Pro / Seedance 智能切换
- 🎯 **八大场景模板**：种草流/直播间/街拍/TVC 大片等
- 📦 **一键生成**：图片/视频/文案全自动
- 🗂️ **自动归档**：飞书云盘 + 多维表格状态追踪
- 🔄 **迭代优化**：低分辨率测试 → 高分辨率输出

## 📦 安装

本技能已发布到 GitHub，使用以下命令安装：

```bash
npx skills add jiebao360/image-material-master -g -y
```

### 配置 API 密钥

```bash
cp .env.example .env
# 编辑 .env 填入你的 API 密钥
```

## 🚀 快速开始

### 生成产品图

```bash
python3 scripts/generate.py --prompt "菲诗蔻护发精油产品图，白色背景，高端质感" --type product
```

### 生成营销海报

```bash
python3 scripts/generate.py --prompt "双 11 促销海报，红色主题，大字报风格" --type poster
```

### 生成视频封面

```bash
python3 scripts/generate.py --prompt "产品视频封面，大字标题" --type cover
```

### 编辑图片

```bash
python3 scripts/generate.py --prompt "让背景更简洁" --input-image input.png --edit
```

## 📖 文档

- [技能说明](SKILL.md) - 完整功能和使用方式
- [架构设计](../../../knowledge-base/系统架构/架构设计.md) - 系统架构和待补充能力

## 🛠️ 脚本说明

| 脚本 | 用途 |
|------|------|
| `scripts/generate.py` | 快速生成（命令行） |
| `scripts/interactive.py` | 交互式生成（引导式） |
| `scripts/batch.py` | 批量生成 |
| `scripts/archive.py` | 归档到飞书 |

## 📊 引擎对比

| 引擎 | 优势 | 最佳场景 | 分辨率 |
|------|------|----------|--------|
| 即梦 AI | 中文理解好 | 电商图 | 2K |
| Nano Banana | 高质量 | 精修图 | 4K |
| Seedance | 视频生成 | 产品视频 | 1080p |

## 📝 使用示例

```bash
# 快速生成
python3 scripts/generate.py --prompt "小红书风格护肤教程封面" --type social

# 批量生成 10 个变体
python3 scripts/batch.py --product "护发精油" --features "72 小时留香" --count 10

# 归档到飞书
python3 scripts/archive.py --input output/ --category product --tags "护发，精油"
```

## 🔗 相关项目

- [jimeng-ai](../../jimeng-ai) - 火山引擎即梦 AI 集成
- [nano-banana-pro](../../nano-banana-pro) - Google Nano Banana Pro
- [seedance-director](../../seedance-director) - Seedance 电商视频提示词

## 📄 许可证

MIT License

## 👥 维护者

OpenClaw 图片素材生成虾团队

---

*最后更新：2026-03-26*
