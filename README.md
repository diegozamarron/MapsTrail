# MapsTrail

MapsTrail is a Python-based, terminal adventure game that simulates a journey between two real-world locations. It combines geographic distance calculations with AI-generated narration to create an Oregon Trail–style experience.

## What It Does

- Calculates real distance between two locations using latitude and longitude  
- Breaks the journey into day-by-day progress  
- Uses an AI narrator to describe events, challenges, or uneventful travel  
- Runs entirely in the terminal with user interaction  

## How It Works

MapsTrail uses the Haversine formula to calculate the distance between two cities. Each in-game day reduces the remaining distance, while an AI model generates narration and events based on the current journey state and user input.

## Built With

- Python  
- Google Gemini API (AI narration)  
- Environment variables for API security  
- Basic math and geographic logic  

## Purpose

This project explores how real-world data and AI-generated storytelling can be combined into a simple, interactive Python program.
