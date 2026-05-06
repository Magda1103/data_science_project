import pytest
import pandas as pd
import numpy as np
from src.processing import FeatureSelector, DelayCombiner


@pytest.fixture
def sample_data():
    """Sample test data."""
    return pd.DataFrame({
        'Gender': ['Male', 'Female'],
        'Age': [25, 30],
        'Departure Delay in Minutes': [10.0, 0.0],
        'Arrival Delay in Minutes': [20.0, np.nan],
        'Extra_Column': [1, 2]
    })


def test_feature_selector_selects_correct_columns(sample_data):
    # GIVEN
    features = ['Gender', 'Age']
    selector = FeatureSelector(features=features)

    # WHEN
    result = selector.transform(sample_data)

    # THEN
    assert result.shape[1] == 2
    assert list(result.columns) == features
    assert 'Extra_Column' not in result.columns


def test_delay_combiner_logic(sample_data):
    # GIVEN
    combiner = DelayCombiner(drop_originals=True)

    # WHEN
    result = combiner.transform(sample_data)

    # THEN
    # 10 + 20 = 30
    assert result['Total_Delay'].iloc[0] == 30.0
    # 0 + NaN (0) = 0
    assert result['Total_Delay'].iloc[1] == 0.0
    assert 'Departure Delay in Minutes' not in result.columns
    assert 'Arrival Delay in Minutes' not in result.columns


def test_delay_combiner_keeps_originals_if_requested(sample_data):
    # GIVEN
    combiner = DelayCombiner(drop_originals=False)

    # WHEN
    result = combiner.transform(sample_data)

    # THEN
    assert 'Departure Delay in Minutes' in result.columns
    assert 'Total_Delay' in result.columns