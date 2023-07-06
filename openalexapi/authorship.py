"""
Copyright 2022 Dennis Priskorn
"""
from typing import Optional, List

from pydantic import BaseModel

from .author import DehydratedAuthor
from .institution import DehydratedInstitution

class Authorship(BaseModel):
    author_position: str
    author: Optional[DehydratedAuthor]
    institutions: Optional[List[DehydratedInstitution]]
    raw_affiliation_string: Optional[str]
    