from abc import ABC, abstractmethod


class GoodPractice(ABC):
    @abstractmethod
    def evaluate(self):
        return

    @abstractmethod
    def parse(self):
        return


