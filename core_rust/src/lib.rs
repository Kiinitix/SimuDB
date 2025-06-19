use pyo3::prelude::*;

#[pyfunction]
fn is_quorum_met(n: usize, w: usize, r: usize) -> bool {
    w + r > n
}

#[pymodule]
fn quorum_core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_quorum_met, m)?)?;
    Ok(())
}
