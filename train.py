"""
通用训练脚本模板（可按需修改）
"""
from __future__ import annotations

import argparse
import os
import random
import time
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("请先安装 PyYAML: pip install pyyaml") from exc


@dataclass
class Config:
    seed: int
    data_dir: Path
    model_dir: Path
    num_epochs: int
    learning_rate: float
    batch_size: int
    device: str


def set_seed(seed: int) -> None:
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def load_config(path: Path) -> Config:
    with path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return Config(
        seed=int(raw["seed"]),
        data_dir=Path(raw["data_dir"]),
        model_dir=Path(raw["model_dir"]),
        num_epochs=int(raw["num_epochs"]),
        learning_rate=float(raw["learning_rate"]),
        batch_size=int(raw["batch_size"]),
        device=str(raw["device"]),
    )


def train(cfg: Config) -> None:
    # TODO: 替换为你的数据加载与模型训练逻辑
    print("[INFO] 开始训练")
    print(cfg)
    cfg.model_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(1, cfg.num_epochs + 1):
        start = time.time()
        # 训练一个 epoch 的占位逻辑
        time.sleep(0.1)
        elapsed = time.time() - start
        print(f"[INFO] Epoch {epoch}/{cfg.num_epochs} - {elapsed:.2f}s")

    # 占位保存
    (cfg.model_dir / "model.bin").write_bytes(b"")
    print("[INFO] 训练完成，模型已保存")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="训练脚本")
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
    set_seed(cfg.seed)
    train(cfg)


if __name__ == "__main__":
    main()
