import pytest
from pathlib import Path

def test_competition_package_completeness():
    """
    [IMPLEMENTED] Phase 95: Validates all 17 competition package chapters exist,
    contain required provenance blocks, and are non-empty.
    """
    package_dir = Path(__file__).resolve().parent.parent / "docs" / "evidence" / "competition_package"
    assert package_dir.exists(), "competition_package directory must exist"

    expected_chapters = [
        "01_problem_definition.md",
        "02_system_architecture.md",
        "03_dataset_provenance.md",
        "04_classical_baseline.md",
        "05_router.md",
        "06_classical_controls.md",
        "07_quantum_method.md",
        "08_budget_sweep.md",
        "09_statistics.md",
        "10_temporal_robustness.md",
        "11_quantum_geometry.md",
        "12_noise.md",
        "13_hardware_gate.md",
        "14_economics.md",
        "15_limitations.md",
        "16_reproducibility.md",
        "17_final_verdict.md"
    ]

    for chapter in expected_chapters:
        p = package_dir / chapter
        assert p.exists(), f"Missing required competition chapter: {chapter}"
        content = p.read_text(encoding="utf-8")
        assert len(content) > 200, f"Chapter {chapter} is too short"
        assert "Dataset Provenance" in content, f"Chapter {chapter} missing provenance block"
        assert "Experiment ID" in content, f"Chapter {chapter} missing experiment ID"
        assert "Metric Definition" in content, f"Chapter {chapter} missing metric definition"
