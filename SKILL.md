---
name: image-material-master
description: 图片素材生成大师 - 整合即梦 AI、Nano Banana Pro、Seedance Director 的完整素材生成工作流
---

# 图片素材生成大师 (Image Material Master)

## 🎯 技能概述

整合火山引擎即梦 AI、Google Nano Banana Pro、Seedance 导演系统的**全能图片素材生成技能**。

**核心定位**：一键生成电商/营销/社交媒体所需的图片、视频、文案素材

**适用场景**：
- 电商产品图生成
- 社交媒体配图制作
- 营销海报设计
- 视频封面生成
- 产品视频创作
- 口播视频剪辑

---

## 🚀 核心功能

### 1️⃣ 多引擎图片生成

| 引擎 | 优势 | 适用场景 | 分辨率 |
|------|------|----------|--------|
| **即梦 AI** | 中文理解好、风格多样 | 电商图、场景图 | 最高 2K |
| **Nano Banana Pro** | 高质量、支持编辑 | 精修图、创意图 | 最高 4K |
| **Seedance** | 视频生成、动态效果 | 产品视频、口播视频 | 720p/1080p |

### 2️⃣ 智能工作流

```
用户输入 → 需求分析 → 引擎选择 → 素材生成 → 后处理 → 归档存储
   │           │           │           │           │           │
   │           │           │           │           │           └─→ 飞书云盘
   │           │           │           │           └─→ rembg 去背/滤镜
   │           │           │           └─→ 图片/视频/文案
   │           │           └─→ 即梦/Nano/Seedance
   │           └─→ 产品类型/风格/用途
   └─→ "生成产品图"/"做海报"
```

### 3️⃣ 八大场景模板

| 场景 | 描述 | 推荐引擎 |
|------|------|----------|
| **种草流** | 真实分享感，高转化 | 即梦 AI |
| **直播间切片** | 高留存，电商转化 | Seedance |
| **街拍流** | 品牌调性展示 | Nano Banana |
| **吃播流** | 食品专用 | 即梦 AI |
| **TVC 大片** | 品牌溢价，高端 | Nano Banana 4K |
| **变装流** | 爆款变装 | Seedance |
| **一镜到底** | 高级创意 | Seedance |
| **视觉奇观** | 投流首秒吸引 | 即梦 AI + Nano |

---

## 📦 安装

本技能已发布到 GitHub，使用以下命令安装：

```bash
npx skills add jiebao360/image-material-master -g -y
```

### 配置 API 密钥

创建 `~/.openclaw/workspace-main/agents/image/.env` 文件：

```bash
# 火山引擎即梦 AI
JIMENG_API_KEY="your_jimeng_key"
VOLC_ACCESS_KEY="your_volc_access_key"
VOLC_SECRET_KEY="your_volc_secret_key"

# Google Nano Banana Pro
GEMINI_API_KEY="your_gemini_key"

# 飞书 API（自动归档）
FEISHU_APP_ID="your_app_id"
FEISHU_APP_SECRET="your_app_secret"
```

---

## 💡 使用方式

### 模式 1：快速生成（默认）

```bash
# 生成产品图
python3 scripts/generate.py --prompt "菲诗蔻护发精油产品图，白色背景，高端质感" --type product

# 生成营销海报
python3 scripts/generate.py --prompt "双 11 促销海报，红色主题，大字报风格" --type poster

# 生成社交媒体配图
python3 scripts/generate.py --prompt "小红书风格护肤教程封面，清新明亮" --type social
```

### 模式 2：交互式生成

```bash
python3 scripts/interactive.py
```

**交互流程**：
1. 输入产品类型
2. 输入核心卖点
3. 选择场景风格（推荐 3 个）
4. 选择生成引擎
5. 生成并预览
6. 迭代优化或导出

### 模式 3：批量生成

```bash
# 批量生成产品图（多尺寸）
python3 scripts/batch.py --product "护发精油" --features "72 小时留香，修复受损" --count 10

# 批量生成视频封面
python3 scripts/batch.py --input videos/ --output covers/ --type cover
```

### 模式 4：API 调用

```python
from image_material_master import MaterialGenerator

generator = MaterialGenerator()

# 生成图片
result = generator.generate_image(
    prompt="高端护肤品产品图",
    engine="jimeng",  # or "nano", "seedance"
    resolution="2K",
    output_path="output/product.png"
)

# 生成视频
result = generator.generate_video(
    prompt="产品展示视频，15 秒",
    engine="seedance",
    duration=15,
    output_path="output/product.mp4"
)

# 智能选择引擎
result = generator.auto_generate(
    prompt="小红书风格护肤教程封面",
    auto_optimize=True
)
```

---

## 🛠️ 脚本说明

### `scripts/generate.py` - 快速生成

**参数**：
- `--prompt`：生成提示词（必填）
- `--type`：类型 [product|poster|social|cover|video]（默认：product）
- `--engine`：引擎 [jimeng|nano|seedance|auto]（默认：auto）
- `--resolution`：分辨率 [1K|2K|4K]（默认：2K）
- `--output`：输出路径（默认：output/yyyy-mm-dd-hh-mm-ss-{name}.png）
- `--edit`：编辑模式，需配合 `--input-image`
- `--input-image`：输入图片路径（编辑模式必填）

**示例**：
```bash
# 生成产品图
python3 scripts/generate.py --prompt "菲诗蔻护发精油，白色背景" --type product

# 编辑图片
python3 scripts/generate.py --prompt "让背景更简洁" --input-image input.png --edit

# 生成视频封面
python3 scripts/generate.py --prompt "产品视频封面，大字标题" --type cover
```

### `scripts/interactive.py` - 交互式生成

**功能**：
- 引导式输入产品信息
- 智能推荐场景和引擎
- 实时预览和迭代
- 一键归档到飞书

**使用**：
```bash
python3 scripts/interactive.py
```

### `scripts/batch.py` - 批量生成

**参数**：
- `--product`：产品名称
- `--features`：产品卖点（逗号分隔）
- `--count`：生成数量（默认：5）
- `--input`：输入目录（批量编辑时使用）
- `--output`：输出目录
- `--type`：生成类型

**示例**：
```bash
# 批量生成 10 个产品图变体
python3 scripts/batch.py --product "护发精油" --features "72 小时留香，修复受损" --count 10

# 批量生成视频封面
python3 scripts/batch.py --input videos/ --output covers/ --type cover
```

### `scripts/archive.py` - 归档到飞书

**功能**：将生成的素材自动上传到飞书云盘并记录到多维表格

**参数**：
- `--input`：输入文件或目录
- `--category`：分类 [product|poster|video|cover]
- `--tags`：标签（逗号分隔）
- `--bitable-app`：多维表格 App Token

**示例**：
```bash
# 上传单个文件
python3 scripts/archive.py --input output/product.png --category product --tags "护发，精油，产品图"

# 上传整个目录
python3 scripts/archive.py --input output/ --category product --tags "批量导入"
```

---

## 📋 输出规范

### 文件命名

```
{日期}-{时间}-{类型}-{描述}.{扩展名}
```

**示例**：
- `2026-03-26-14-30-00-product-hufajingyou.png`
- `2026-03-26-15-00-00-cover-hufajingyou-promo.png`
- `2026-03-26-16-00-00-video-product-showcase.mp4`

### 输出目录结构

```
output/
├── 2026-03-26/
│   ├── product/
│   │   ├── 2026-03-26-14-30-00-product-hufajingyou.png
│   │   └── 2026-03-26-14-35-00-product-hufajingyou-v2.png
│   ├── poster/
│   │   └── 2026-03-26-15-00-00-poster-shuang11.png
│   └── video/
│       └── 2026-03-26-16-00-00-video-showcase.mp4
└── archive/
    └── ...
```

### 元数据记录

每个生成的素材自动记录以下信息到飞书多维表格：

| 字段 | 说明 |
|------|------|
| 素材 ID | 唯一标识符 |
| 素材名称 | 文件名 |
| 素材类型 | product/poster/video/cover |
| 生成引擎 | jimeng/nano/seedance |
| 提示词 | 使用的生成提示词 |
| 分辨率 | 1K/2K/4K/720p/1080p |
| 生成时间 | ISO 8601 时间戳 |
| 飞书链接 | 云盘文件链接 |
| 标签 | 逗号分隔的标签 |
| 使用次数 | 被引用次数 |
| 效果数据 | 播放量/点赞等（后续填充） |

---

## 🔧 高级功能

### 1️⃣ 智能引擎选择

```python
def auto_select_engine(prompt, type):
    """
    根据提示词和类型自动选择最佳引擎
    """
    if type == "video":
        return "seedance"
    elif "编辑" in prompt or "修改" in prompt:
        return "nano"  # Nano 支持图片编辑
    elif "电商" in prompt or "产品" in prompt:
        return "jimeng"  # 即梦电商效果好
    else:
        return "nano"  # 默认高质量
```

### 2️⃣ 提示词优化

```python
def optimize_prompt(base_prompt, type):
    """
    根据类型自动优化提示词
    """
    templates = {
        "product": "专业产品摄影，{prompt}, 纯白背景，商业级质感，4K 高清",
        "poster": "营销海报设计，{prompt}, 醒目大字，促销氛围，高对比度",
        "social": "社交媒体风格，{prompt}, 清新明亮，ins 风，适合小红书",
        "cover": "视频封面，{prompt}, 大标题位置，吸引点击，高饱和度"
    }
    return templates.get(type, "{prompt}").format(prompt=base_prompt)
```

### 3️⃣ 自动后处理

```python
def post_process(image_path, operations):
    """
    自动后处理：去背、滤镜、调整尺寸等
    """
    from rembg import remove
    from PIL import Image
    
    img = Image.open(image_path)
    
    if "remove_background" in operations:
        img = remove(img)  # 去背
    
    if "resize_1080" in operations:
        img = img.resize((1080, 1080))  # 调整尺寸
    
    img.save(image_path)
```

---

## 📊 性能指标

| 指标 | 即梦 AI | Nano Banana | Seedance |
|------|---------|-------------|----------|
| 生成速度 | 10-30 秒 | 30-60 秒 | 60-120 秒 |
| 最佳分辨率 | 2K | 4K | 1080p |
| 中文理解 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 图片质量 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 视频能力 | ⭐⭐⭐ | ❌ | ⭐⭐⭐⭐⭐ |
| 编辑能力 | ❌ | ⭐⭐⭐⭐⭐ | ❌ |
| 成本 | 中 | 高 | 中 |

---

## ⚠️ 注意事项

### API 限制

| 引擎 | 每日配额 | 并发限制 | 超时时间 |
|------|----------|----------|----------|
| 即梦 AI | 1000 次 | 5 请求/秒 | 60 秒 |
| Nano Banana | 500 次 | 3 请求/秒 | 120 秒 |
| Seedance | 200 次 | 2 请求/秒 | 180 秒 |

### 最佳实践

1. **先用低分辨率测试**：1K 测试 → 满意后再生成 4K
2. **批量生成时错峰**：避免同时发起大量请求
3. **保存原始提示词**：方便后续迭代和复用
4. **定期归档**：避免本地文件堆积

### 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `API key not found` | 未配置环境变量 | 检查 `.env` 文件 |
| `Quota exceeded` | 超出每日配额 | 等待次日或升级套餐 |
| `Timeout` | 网络超时 | 重试或切换引擎 |
| `Invalid prompt` | 提示词违规 | 修改提示词，避免敏感内容 |

---

## 🔗 相关技能

- **jimeng-ai**：火山引擎即梦 AI 集成
- **nano-banana-pro**：Google Nano Banana Pro 图像生成
- **seedance-director**：Seedance 电商视频提示词生成
- **material-shrimp**：Seedance 提示词生成器
- **video-clip-auto**：视频自动剪辑
- **rembg**：背景移除工具

---

## 📝 更新日志

### v1.0.0 (2026-03-26)
- ✨ 初始版本发布
- 🎨 整合即梦 AI、Nano Banana Pro、Seedance
- 📦 支持图片/视频/文案生成
- 🗂️ 飞书云盘自动归档
- 📊 多维表格状态追踪

---

## 📄 许可证

MIT License

## 👥 维护者

OpenClaw 图片素材生成虾团队

---

*最后更新：2026-03-26*
