pub fn is_quorum_met(n: usize, w: usize, r: usize) -> bool {
    w + r > n
}
