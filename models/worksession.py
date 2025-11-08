# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 22:37:07 2025

@author: Chex
"""

from database import Database

class Worksession:
    def __init__(self, start_time, project_id, end_time=None, description=None, id=None,):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.project_id = project_id
        self.description = description
        
    def start_session(self, db: Database):
        query = "INSERT INTO worksessions (start_time, project_id, description) VALUES (?, ?, ?)"
        db.execute(query, (self.start_time, self.project_id, self.description))
        
    def end_session(self, db: Database):
        query = "UPDATE worksessions SET end_time = ?, description = ? WHERE id = ?"
        db.execute(query, (self.end_time, self.description, self.id))
        
    @classmethod
    def from_row(cls, row):
        return cls(*row)
    
    @classmethod
    def all(cls, db:Database):
        rows = db.execute("SELECT id, start_time, end_time, project_id, description FROM worksessions", fetch=True)
        return [cls.from_row(row) for row in rows]
    
    @classmethod
    def get_by_id(cls, db:Database, project_id: int):
        row = db.execute("SELECT id, start_time, end_time, project_id, description FROM worksessions WHERE id = ?", (project_id,), fetch=True)
        return cls.from_row(row[0]) if row else None
    
    def __str__(self):
        return f"[{self.id}] {self.start_time} -> {self.end_time} ({self.project_id}: {self.description})"