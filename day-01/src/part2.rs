pub fn solve(_input: &str) -> String {
    todo!("day 01 - part 02")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), "0");
    }
}
