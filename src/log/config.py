"""配置管理模块

继承 dong.config.Config，管理 log-cli 的用户配置。
"""

from dong.config import Config


class LogConfig(Config):
    """
    记咚咚配置类

    管理用户配置，如默认分组、默认限制等。

    配置文件路径: ~/.log/config.json
    """

    @classmethod
    def get_name(cls) -> str:
        """返回 CLI 名称"""
        return "log"

    @classmethod
    def get_defaults(cls) -> dict:
        """返回默认配置"""
        return {
            # 默认分组
            "default_group": "default",
            # 默认列表数量限制
            "default_limit": 20,
            # 预设分组
            "preset_groups": ["default", "work", "life", "indie", "family"],
            # 日期格式
            "date_format": "%Y-%m-%d",
        }


# ============================================================================
# 便捷函数
# ============================================================================

def get_config() -> dict:
    """获取配置（便捷函数）"""
    return LogConfig.load()


def get_default_group() -> str:
    """获取默认分组"""
    return LogConfig.get("default_group", "default")


def set_default_group(group: str) -> None:
    """设置默认分组"""
    LogConfig.set("default_group", group)


def get_default_limit() -> int:
    """获取默认列表限制"""
    return LogConfig.get("default_limit", 20)


def get_preset_groups() -> list:
    """获取预设分组列表"""
    return LogConfig.get("preset_groups", ["default", "work", "life", "indie", "family"])


# ============================================================================
# 从 const.py 迁移的常量
# ============================================================================

# 预设分组常量（向后兼容）
GROUP_WORK = "work"
GROUP_LIFE = "life"
GROUP_INDIE = "indie"
GROUP_FAMILY = "family"
DEFAULT_GROUP = "default"
PRESET_GROUPS = [DEFAULT_GROUP, GROUP_WORK, GROUP_LIFE, GROUP_INDIE, GROUP_FAMILY]
