# 图片素材生成大师 - 学习指南

## 🎯 技能定位

整合多 AI 引擎的**全能图片素材生成工具**，一键生成电商/营销/社交媒体所需的图片、视频、文案素材。

## 📚 学习路径

### Level 1: 新手入门 (1-2 小时)

**目标**：能够使用命令行生成基础图片

**学习内容**：
1. 安装技能和配置 API 密钥
2. 使用 `generate.py` 生成产品图
3. 理解提示词的基本结构
4. 查看生成的图片文件

**实践任务**：
```bash
# 任务 1：生成一个简单的产品图
python3 scripts/generate.py --prompt "白色背景上的咖啡杯" --type product

# 任务 2：生成社交媒体配图
python3 scripts/generate.py --prompt "清新风格的护肤教程封面" --type social

# 任务 3：尝试不同分辨率
python3 scripts/generate.py --prompt "产品图" --resolution 1K
python3 scripts/generate.py --prompt "产品图" --resolution 4K
```

### Level 2: 进阶使用 (3-5 小时)

**目标**：掌握多引擎选择和提示词优化

**学习内容**：
1. 理解三大引擎的特点和适用场景
2. 学习提示词优化技巧
3. 使用编辑功能修改图片
4. 批量生成多个变体

**实践任务**：
```bash
# 任务 1：对比不同引擎的效果
python3 scripts/generate.py --prompt "护肤品产品图" --engine jimeng
python3 scripts/generate.py --prompt "护肤品产品图" --engine nano

# 任务 2：编辑现有图片
python3 scripts/generate.py --prompt "让背景更简洁" --input-image input.png --edit

# 任务 3：批量生成 5 个变体
python3 scripts/batch.py --product "护发精油" --features "72 小时留香" --count 5
```

### Level 3: 高级应用 (5-10 小时)

**目标**：完整工作流和自动化集成

**学习内容**：
1. 飞书云盘自动归档
2. 多维表格状态追踪
3. 交互式生成模式
4. 与其他技能集成

**实践任务**：
```bash
# 任务 1：完整工作流
python3 scripts/generate.py --prompt "产品图" --type product
python3 scripts/archive.py --input output/ --category product --tags "产品图"

# 任务 2：交互式生成
python3 scripts/interactive.py

# 任务 3：集成到日常工作流
# 将技能集成到 daily-orchestrator 或 make-contents
```

## 🔧 核心概念

### 1. 引擎选择

| 引擎 | 何时使用 |
|------|----------|
| **即梦 AI** | 电商产品图、中文场景、快速生成 |
| **Nano Banana** | 高质量精修、图片编辑、4K 输出 |
| **Seedance** | 视频生成、动态效果、口播视频 |

### 2. 提示词公式

```
【主体描述】+【场景/背景】+【风格/氛围】+【技术参数】

示例：
"菲诗蔻护发精油产品图，白色背景，高端质感，4K 高清，商业级摄影"
```

### 3. 工作流最佳实践

```
1. 1K 分辨率测试提示词
2. 调整优化提示词
3. 2K/4K 正式生成
4. 后处理（去背/滤镜）
5. 归档到飞书云盘
6. 记录到多维表格
```

## 💡 实战案例

### 案例 1：电商产品图批量生成

**需求**：为 10 款护肤品生成产品图

**步骤**：
```bash
# 1. 准备产品列表
products=(
  "菲诗蔻护发精油"
  "兰蔻小黑瓶"
  "雅诗兰黛小棕瓶"
  # ... 更多产品
)

# 2. 批量生成
for product in "${products[@]}"; do
  python3 scripts/batch.py --product "$product" --count 3
done

# 3. 归档
python3 scripts/archive.py --input output/ --category product
```

### 案例 2：社交媒体内容创作

**需求**：为一周的小红书内容生成配图

**步骤**：
```bash
# 周一：护肤教程
python3 scripts/generate.py --prompt "护肤教程封面，清新明亮，ins 风" --type social

# 周三：产品测评
python3 scripts/generate.py --prompt "产品测评封面，对比图，专业感" --type social

# 周五：好物推荐
python3 scripts/generate.py --prompt "好物推荐封面，温馨场景，种草感" --type social
```

### 案例 3：营销海报设计

**需求**：双 11 促销活动海报

**步骤**：
```bash
# 生成主海报
python3 scripts/generate.py --prompt "双 11 促销海报，红色主题，5 折大字，紧迫感" --type poster

# 生成变体
python3 scripts/batch.py --product "双 11 海报" --features "红色，促销，5 折" --count 5

# 选择最佳版本并归档
python3 scripts/archive.py --input output/ --category poster --tags "双 11，促销"
```

## ⚠️ 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| API key not found | 未配置 .env | 检查环境变量 |
| Quota exceeded | 超出配额 | 等待次日或升级 |
| Timeout | 网络超时 | 重试或切换引擎 |
| Invalid prompt | 提示词违规 | 修改提示词 |

## 📖 进阶阅读

- [SKILL.md](SKILL.md) - 完整技能文档
- [架构设计](../../../knowledge-base/系统架构/架构设计.md) - 系统架构
- [即梦 AI 文档](../../jimeng-ai/README.md)
- [Nano Banana Pro 文档](../../nano-banana-pro/README.md)
- [Seedance 文档](../../seedance-director/README.md)

## 🎓 认证任务

完成以下任务获得"图片素材生成大师"认证：

- [ ] 生成 10 张不同类别的图片
- [ ] 使用所有 3 个引擎各至少 1 次
- [ ] 完成 1 次批量生成（5 个以上）
- [ ] 完成 1 次飞书归档
- [ ] 创建 1 个自定义提示词模板

---

*最后更新：2026-03-26*
