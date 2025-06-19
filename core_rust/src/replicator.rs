use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct Replica {
    pub id: usize,
    pub data: HashMap<String, (String, f64)>, // key -> (value, timestamp)
}

impl Replica {
    pub fn new(id: usize) -> Self {
        Self {
            id,
            data: HashMap::new(),
        }
    }

    pub fn write(&mut self, key: &str, value: &str, timestamp: f64) {
        self.data.insert(key.to_string(), (value.to_string(), timestamp));
    }

    pub fn read(&self, key: &str) -> Option<(String, f64)> {
        self.data.get(key).cloned()
    }
}

pub fn write_to_quorum(
    replicas: &mut [Replica],
    key: &str,
    value: &str,
    timestamp: f64,
    w: usize,
) -> bool {
    if w > replicas.len() {
        return false;
    }

    for i in 0..w {
        replicas[i].write(key, value, timestamp);
    }
    true
}

pub fn read_from_quorum(
    replicas: &[Replica],
    key: &str,
    r: usize,
) -> Option<(String, f64)> {
    let mut results = vec![];

    for i in 0..r.min(replicas.len()) {
        if let Some(data) = replicas[i].read(key) {
            results.push(data);
        }
    }

    results.into_iter().max_by(|a, b| a.1.partial_cmp(&b.1).unwrap())
}
