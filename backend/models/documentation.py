"""
Documentation model.
"""

from typing import Dict
from pydantic import BaseModel, Field


class Documentation(BaseModel):
    """Generated project documentation."""

    documents: Dict[str, str] = Field(..., description="Generated documentation files")
