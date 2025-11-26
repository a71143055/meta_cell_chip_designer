"""
StorageService
--------------
서비스 계층에서 스토리지 모듈(local_fs, schema 등)을 쉽게 사용할 수 있도록 래퍼 제공.
"""

from storage import local_fs, schema

class StorageService:
    def __init__(self, logger=None):
        self.logger = logger

    def save_project_json(self, path: str, obj: dict) -> bool:
        try:
            local_fs.save_json(path, obj)
            if self.logger:
                self.logger.info(f"Saved JSON to {path}")
            return True
        except Exception as e:
            if self.logger:
                self.logger.exception(e)
            return False

    def get_project_ext(self) -> str:
        return schema.PROJECT_EXT

    def get_spice_ext(self) -> str:
        return schema.SPICE_EXT
