from abc import ABC, abstractmethod, abstractproperty


class UnitSkill(ABC):
    user = None
    target = None


@property
@abstractmethod
def name():
    pass


@property
@abstractmethod
def damage():
    pass


@abstractmethod
def skill_effect():
    pass


@abstractmethod
def use(user, targer):
    pass
