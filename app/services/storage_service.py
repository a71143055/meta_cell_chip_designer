from storage import local_fs, schema

class StorageService:
    def __init__(self, logger=None):
        self.logger = logger

    def save_json(self, path: str, obj: dict) -> bool:
        try:
            local_fs.save_json(path, obj)
            if self.logger:
                self.logger.info(f"Saved JSON to {path}")
            return True
        except Exception as e:
            if self.logger:
                self.logger.warning(f"Error saving JSON, but continuing: {e}")
            return False

    def get_project_ext(self) -> str:
        return schema.PROJECT_EXT

    def get_spice_ext(self) -> str:
        return schema.SPICE_EXT

