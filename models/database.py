# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 22:36:49 2025

@author: Chex
"""

import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
    
    def initialize(self):
        """Creëert nieuwe database en tabellen als die nog niet bestaan."""
        with self.connect() as conn:
            cursor = conn.cursor()
            
            # Tabel: projects
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS projects (
                               id INTEGER NOT NULL UNIQUE,
                               name TEXT NOT NULL,
                               description TEXT,
                               is_active INTEGER NOT NULL,
                               PRIMARY KEY("id" AUTOINCREMENT)
                               )
                           """)
                           
            # Tabel: worksessions
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS worksessions (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               start_time TEXT NOT NULL,
                               end_time TEXT NOT NULL,
                               project_id INTEGER NOT NULL,
                               comment TEXT,
                               PRIMARY KEY("id" AUTOINCREMENT),
                               FOREIGN KEY("project_id") REFERENCES "projects"("id")
                               )
                           """)
                           
            conn.commit()
            print("Database is geïnitialiseerd.")
            
            
            