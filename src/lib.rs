use pyo3::prelude::*;
use strsim::damerau_levenshtein as damerau_levenshtein_rust;
use strsim::hamming as hamming_rust;
use strsim::jaro as jaro_rust;
use strsim::jaro_winkler as jaro_winkler_rust;
use strsim::levenshtein as levenshtein_rust;
use strsim::normalized_damerau_levenshtein as normalized_damerau_levenshtein_rust;
use strsim::normalized_levenshtein as normalized_levenshtein_rust;
use strsim::osa_distance as osa_distance_rust;
use strsim::sorensen_dice as sorensen_dice_rust;

#[pyfunction]
fn damerau_levenshtein(a: &str, b: &str) -> PyResult<usize> {
    Ok(damerau_levenshtein_rust(a, b))
}

#[pyfunction]
fn hamming(a: &str, b: &str) -> PyResult<usize> {
    Ok(hamming_rust(a, b).unwrap())
}

#[pyfunction]
fn jaro(a: &str, b: &str) -> PyResult<f64> {
    Ok(jaro_rust(a, b))
}

#[pyfunction]
fn jaro_winkler(a: &str, b: &str) -> PyResult<f64> {
    Ok(jaro_winkler_rust(a, b))
}

#[pyfunction]
fn levenshtein(a: &str, b: &str) -> PyResult<usize> {
    Ok(levenshtein_rust(a, b))
}

#[pyfunction]
fn normalized_damerau_levenshtein(a: &str, b: &str) -> PyResult<f64> {
    Ok(normalized_damerau_levenshtein_rust(a, b))
}

#[pyfunction]
fn normalized_levenshtein(a: &str, b: &str) -> PyResult<f64> {
    Ok(normalized_levenshtein_rust(a, b))
}

#[pyfunction]
fn osa_distance(a: &str, b: &str) -> PyResult<usize> {
    Ok(osa_distance_rust(a, b))
}

#[pyfunction]
fn sorensen_dice(a: &str, b: &str) -> PyResult<f64> {
    Ok(sorensen_dice_rust(a, b))
}

#[pymodule]
fn pystrsim(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(damerau_levenshtein, m)?)?;
    m.add_function(wrap_pyfunction!(hamming, m)?)?;
    m.add_function(wrap_pyfunction!(jaro, m)?)?;
    m.add_function(wrap_pyfunction!(jaro_winkler, m)?)?;
    m.add_function(wrap_pyfunction!(levenshtein, m)?)?;
    m.add_function(wrap_pyfunction!(normalized_damerau_levenshtein, m)?)?;
    m.add_function(wrap_pyfunction!(normalized_levenshtein, m)?)?;
    m.add_function(wrap_pyfunction!(osa_distance, m)?)?;
    m.add_function(wrap_pyfunction!(sorensen_dice, m)?)?;
    Ok(())
}
