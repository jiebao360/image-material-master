#!/usr/bin/env python3
"""
图片素材生成大师 - 快速生成脚本
支持即梦 AI、Nano Banana Pro、Seedance 多引擎
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

def generate_filename(prompt, type="product"):
    """生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # 从提示词提取关键词
    words = prompt.split()[:3]
    name = "-".join(words).lower()[:30]
    return f"{timestamp}-{type}-{name}.png"

def auto_select_engine(prompt, type):
    """根据提示词和类型自动选择最佳引擎"""
    if type == "video":
        return "seedance"
    elif any(word in prompt for word in ["编辑", "修改", "remove", "edit"]):
        return "nano"
    elif any(word in prompt for word in ["电商", "产品", "product", "ecommerce"]):
        return "jimeng"
    else:
        return "nano"

def optimize_prompt(base_prompt, type):
    """根据类型自动优化提示词"""
    templates = {
        "product": "专业产品摄影，{prompt}, 纯白背景，商业级质感，4K 高清",
        "poster": "营销海报设计，{prompt}, 醒目大字，促销氛围，高对比度",
        "social": "社交媒体风格，{prompt}, 清新明亮，ins 风，适合小红书",
        "cover": "视频封面，{prompt}, 大标题位置，吸引点击，高饱和度",
        "video": "产品展示视频，{prompt}, 专业拍摄，电影感，1080p"
    }
    template = templates.get(type, "{prompt}")
    return template.format(prompt=base_prompt)

def generate_with_jimeng(prompt, output_path, resolution="2K"):
    """调用即梦 AI 生成图片"""
    print(f"🎨 使用即梦 AI 生成...")
    print(f"   提示词：{prompt}")
    print(f"   分辨率：{resolution}")
    print(f"   输出：{output_path}")
    
    # TODO: 集成即梦 AI API
    # from jimeng_adapter import JimengAdapter
    # adapter = JimengAdapter()
    # result = adapter.generate_image(prompt=prompt, output_path=output_path, resolution=resolution)
    
    # 模拟输出
    print(f"✅ 即梦 AI 生成完成（模拟）")
    return {"status": "success", "path": output_path, "engine": "jimeng"}

def generate_with_nano(prompt, output_path, resolution="2K", input_image=None):
    """调用 Nano Banana Pro 生成/编辑图片"""
    print(f"🍌 使用 Nano Banana Pro 生成...")
    print(f"   提示词：{prompt}")
    print(f"   分辨率：{resolution}")
    print(f"   输出：{output_path}")
    
    if input_image:
        print(f"   编辑模式：{input_image}")
        cmd = f"uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt '{prompt}' --filename '{output_path}' --input-image '{input_image}' --resolution {resolution}"
    else:
        cmd = f"uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt '{prompt}' --filename '{output_path}' --resolution {resolution}"
    
    print(f"   命令：{cmd}")
    
    # TODO: 执行命令
    # import subprocess
    # result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # 模拟输出
    print(f"✅ Nano Banana Pro 生成完成（模拟）")
    return {"status": "success", "path": output_path, "engine": "nano"}

def generate_with_seedance(prompt, output_path, duration=15):
    """调用 Seedance 生成视频"""
    print(f"🎬 使用 Seedance 生成视频...")
    print(f"   提示词：{prompt}")
    print(f"   时长：{duration}秒")
    print(f"   输出：{output_path}")
    
    # TODO: 集成 Seedance API
    # from seedance_adapter import SeedanceAdapter
    # adapter = SeedanceAdapter()
    # result = adapter.generate_video(prompt=prompt, output_path=output_path, duration=duration)
    
    # 模拟输出
    output_video = output_path.replace(".png", ".mp4")
    print(f"✅ Seedance 生成完成（模拟）")
    return {"status": "success", "path": output_video, "engine": "seedance"}

def main():
    parser = argparse.ArgumentParser(description="图片素材生成大师 - 快速生成脚本")
    parser.add_argument("--prompt", type=str, required=True, help="生成提示词")
    parser.add_argument("--type", type=str, default="product", 
                       choices=["product", "poster", "social", "cover", "video"],
                       help="生成类型")
    parser.add_argument("--engine", type=str, default="auto",
                       choices=["jimeng", "nano", "seedance", "auto"],
                       help="生成引擎")
    parser.add_argument("--resolution", type=str, default="2K",
                       choices=["1K", "2K", "4K"],
                       help="分辨率")
    parser.add_argument("--output", type=str, default=None, help="输出路径")
    parser.add_argument("--edit", action="store_true", help="编辑模式")
    parser.add_argument("--input-image", type=str, default=None, help="输入图片路径（编辑模式）")
    parser.add_argument("--duration", type=int, default=15, help="视频时长（秒）")
    
    args = parser.parse_args()
    
    # 优化提示词
    optimized_prompt = optimize_prompt(args.prompt, args.type)
    print(f"📝 优化后提示词：{optimized_prompt}")
    
    # 选择引擎
    engine = args.engine if args.engine != "auto" else auto_select_engine(args.prompt, args.type)
    print(f"🔧 选择引擎：{engine}")
    
    # 生成输出路径
    if args.output:
        output_path = args.output
    else:
        output_dir = Path("output") / datetime.now().strftime("%Y-%m-%d") / args.type
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = str(output_dir / generate_filename(args.prompt, args.type))
    
    # 根据引擎生成
    if engine == "jimeng":
        result = generate_with_jimeng(optimized_prompt, output_path, args.resolution)
    elif engine == "nano":
        result = generate_with_nano(optimized_prompt, output_path, args.resolution, 
                                   args.input_image if args.edit else None)
    elif engine == "seedance":
        result = generate_with_seedance(optimized_prompt, output_path, args.duration)
    
    # 输出结果
    print(f"\n✅ 生成完成！")
    print(f"   文件：{result['path']}")
    print(f"   引擎：{result['engine']}")
    print(f"   状态：{result['status']}")
    
    return 0 if result['status'] == 'success' else 1

if __name__ == "__main__":
    sys.exit(main())
