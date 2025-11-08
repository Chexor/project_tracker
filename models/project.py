# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 22:36:58 2025

@author: Chex
"""

from database import Database

class Project:
    def __init__(self, name, id=None, description=None, is_active=True):
        self.id = id
        self.name = name
        self.description = description
        self.is_active = is_active
    
    def save(self, db: Database):
        query = "INSERT INTO projects (name, description, is_active) VALUES (?, ?, ?)"
        db.execute(query, (self.name, self.description, self.is_active))
        
    def update(self, db: Database):
        query = "UPDATE projects SET name = ?, description = ?, is_active = ? WHERE id = ?"
        db.execute(query, (self.name, self.description, self.is_active, self.id))
    
    @classmethod
    def from_row(cls, row):
        return cls(*row)
    
    @classmethod
    def all(cls, db:Database):
        rows = db.execute("SELECT id, name, description, is_active FROM projects", fetch=True)
        return [cls.from_row(row) for row in rows]
    
    @classmethod
    def get_by_id(cls, db:Database, project_id: int):
        row = db.execute("SELECT id, name, description, is_active FROM projects WHERE id = ?", (project_id,), fetch=True)
        return cls.from_row(row[0]) if row else None
    
    def __str__(self):
        return f"[{self.id}] {self.name} ({self.is_active})"
    
    