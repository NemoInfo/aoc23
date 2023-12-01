pub fn solve(input: &str) -> u32 {
    let mut sum: u32 = 0;

    for line in input.lines() {
        let Some(i) = line.chars().find(|c: &char| c.is_digit(10)) else {
            panic!()
        };
        let Some(j) = line.chars().rfind(|c: &char| c.is_digit(10)) else {
            panic!()
        };

        let d = i.to_string() + &j.to_string();
        sum += d.parse::<u32>().unwrap();
    }

    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test1.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 142);
    }
}
