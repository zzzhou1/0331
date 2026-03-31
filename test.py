"""
通用测试脚本模板（可按需修改）
"""
from __future__ import annotations

import argparse
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("请先安装 PyYAML: pip install pyyaml") from exc


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test(cfg: dict) -> None:
    # TODO: 替换为你的模型加载与评估逻辑
    print("[INFO] 开始测试")
    print(cfg)
    print("[INFO] 测试完成")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="测试脚本")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="配置文件路径",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)
    test(cfg)


if __name__ == "__main__":
    main()
