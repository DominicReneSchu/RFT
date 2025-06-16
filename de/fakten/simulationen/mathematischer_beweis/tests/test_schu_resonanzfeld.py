# -*- coding: utf-8 -*-
# Unit-Tests für schu_resonanzfeld.py
# © Dominic Schu, 2025 – Alle Rechte vorbehalten.

import numpy as np
import pytest
from schu_resonanzfeld import (
    berechne_resonanzenergie,
    berechne_resonanzentropie,
)

def test_berechne_resonanzenergie_shape_and_values():
    A = np.array([0.5, 1.0, 2.0])
    T = np.array([0.5, 1.0])
    E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
    # Form prüfen
    assert E_res.shape == (3, 2)
    assert T_grid.shape == (3, 2)
    assert A_grid.shape == (3, 2)
    # Wertebereich prüfen (keine negativen oder null Werte)
    assert np.all(E_res > 0)

def test_berechne_resonanzenergie_physical_values():
    # Teste, dass höhere Amplitude zu höherer Resonanzenergie führt (bei konstantem T)
    A = np.array([0.5, 1.0, 2.0])
    T = np.array([1.0])
    E_res, _, _ = berechne_resonanzenergie(A, T)
    assert E_res[0, 0] < E_res[1, 0] < E_res[2, 0]

def test_berechne_resonanzenergie_invalid_inputs():
    # Negative A oder T → Fehler
    A_neg = np.array([-1.0, 1.0])
    T_pos = np.array([1.0, 2.0])
    with pytest.raises(ValueError):
        berechne_resonanzenergie(A_neg, T_pos)
    A_pos = np.array([1.0, 2.0])
    T_neg = np.array([-0.1, 0.5])
    with pytest.raises(ValueError):
        berechne_resonanzenergie(A_pos, T_neg)
    # Nicht-1D-Arrays
    A_2d = np.array([[1.0, 2.0]])
    with pytest.raises(ValueError):
        berechne_resonanzenergie(A_2d, T_pos)

def test_berechne_resonanzentropie_shape_and_values():
    # Entropie darf nie NaN sein, muss <= 0 für E_res=1 (maximale Ordnung)
    E_res = np.array([[0.5, 1.0], [2.0, 4.0]])
    S = berechne_resonanzentropie(E_res)
    assert S.shape == E_res.shape
    assert np.all(np.isfinite(S))

def test_berechne_resonanzentropie_invalid_input():
    # Negative oder Nullwerte geben Fehler
    E_res_bad = np.array([0.0, 1.0])
    with pytest.raises(ValueError):
        berechne_resonanzentropie(E_res_bad)

def test_berechne_resonanzentropie_monotonie():
    # Für zwei Werte gilt: höhere Energie → kleinere Entropie
    e1, e2 = 0.1, 0.9
    S = berechne_resonanzentropie(np.array([e1, e2]))
    assert S[0] > S[1]

# Optional: Test für save_path und show=False in plot_resonanzfeld (nur smoke test)
def test_plot_resonanzfeld_runs(tmp_path):
    from schu_resonanzfeld import plot_resonanzfeld
    A = np.linspace(0.1, 1, 10)
    T = np.linspace(0.1, 1, 10)
    E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
    S = berechne_resonanzentropie(E_res)
    savefile = tmp_path / "plot.png"
    # Sollte ohne Exception durchlaufen (kein Plot-Window)
    plot_resonanzfeld(T_grid, A_grid, E_res, S, save_path=str(savefile), show=False)
    assert savefile.exists()