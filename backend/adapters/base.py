from abc import ABC, abstractmethod
from models import Job


class BaseAdapter(ABC):

    @abstractmethod
    def extract_job(self, page) -> Job:
        pass