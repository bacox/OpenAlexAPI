"""
Copyright 2022 Dennis Priskorn
"""
from typing import Optional

from pydantic import BaseModel
from .enums import OpenAccessStatus

class OpenAccess(BaseModel):
    is_oa: bool
    oa_status: Optional[str] #TODO: use class in enums
    oa_url: Optional[str]
