"""导出器模块

实现 log-cli 的数据导出功能。
"""

from typing import Any
from dong.io import BaseExporter, ExporterRegistry
from .db.connection import LogDatabase


class LogExporter(BaseExporter):
    """日志导出器"""
    
    name = "log"
    
    def fetch_all(self) -> list[dict[str, Any]]:
        """
        获取所有日志数据
        
        Returns:
            日志列表
        """
        with LogDatabase.get_cursor() as cur:
            cur.execute("""
                SELECT 
                    id,
                    log_group,
                    content,
                    date,
                    created_at
                FROM logs
                ORDER BY created_at DESC
            """)
            rows = cur.fetchall()
            
            return [
                {
                    "id": row[0],
                    "group": row[1],
                    "content": row[2],
                    "date": row[3],
                    "created_at": row[4],
                }
                for row in rows
            ]
    
    def to_markdown(self) -> str:
        """导出为 Markdown 格式"""
        data = self.fetch_all()
        lines = ["# 记咚咚 - 日志导出\n"]
        
        # 按组分组
        groups: dict[str, list] = {}
        for item in data:
            group = item.get("group") or "default"
            if group not in groups:
                groups[group] = []
            groups[group].append(item)
        
        # 输出
        for group_name, items in groups.items():
            lines.append(f"\n## {group_name}\n")
            for item in items:
                tags_str = " ".join(f"#{t}" for t in item.get("tags", []))
                lines.append(f"- {item['content']} {tags_str}")
                lines.append(f"  - 创建: {item['created_at']}")
        
        return "\n".join(lines)


# 注册到 dong.io
ExporterRegistry.register(LogExporter())
