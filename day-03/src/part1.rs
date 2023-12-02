pub fn solve(input: &str) -> u32 {
    todo!("day-03 part1")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 0);
    }
}
