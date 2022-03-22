from datetime import datetime
from unicodedata import category
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

@dataclass()

#Construtor

class Category:
    
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())

#created_at = datetime.now()
#print(
    #Category('Movie', 'Um filme qq', True, created_at) == Category('Movie', 'Um filme qq', True, created_at)
#)
    
    # Depois que inseri o Decorator @dataclass(), nao foi mais necessário o constructor abaixo.
    ##def __init__(self, name: str, description: str = None , is_active: bool = True, created_at: datetime = datetime.now()) -> None:
    ##    self.name = name
    ##   self.description = description
    ##   self.is_active = is_active
    ##    self.created_at = created_at


