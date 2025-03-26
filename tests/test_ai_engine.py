import pytest
from src.ai_engine import AIDiagnosticEngine

def test_ai_engine_initialization():
    engine = AIDiagnosticEngine()
    assert len(engine.conversation_history) == 0
    assert engine.question_count == 0

def test_process_input():
    engine = AIDiagnosticEngine()
    response = engine.process_input("I have a headache", "en")
    assert response.endswith("?")  # Should ask a follow-up question
