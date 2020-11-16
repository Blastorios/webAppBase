from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    """The Pydantic validation model for class User.
    id: User's id-hash to identify its database storage.
    name: Default display name on the web page.
    signup: Date Time record of its first signup to the webpage
    groups: A list with the ids of the group.
    """
    id:int
    name:str = 'Regular'
    _editor:bool = False
    signup:Optional[datetime] = None
    groups:List[int] = []
    friends:List[int] = []

class Admin(BaseModel):
    """The Pydantic validation model for class Admin.
    id: The Admin's id-hash used to identify its database storage.
    
    """
    id:int
    name:str = 'Special Regular'
    _editor:bool = True
    _sysEditor:bool = False
    signup:Optional[datetime] = None
    groups:List[int] = []
    friends:List[int] = []

class SysAdmin(BaseModel):
    """The Pydantic validation model for class Admin.
    id: The Admin's id-hash used to identify its database storage.
    
    """
    id:int
    name:str = 'Maestro'
    _editor:bool = True
    _sysEditor:bool = True
    signup:Optional[datetime] = None
    groups:List[int] = []
    friends:List[int] = []