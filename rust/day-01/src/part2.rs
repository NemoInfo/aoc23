use regex::Regex;

static TABLE: [&'static str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn to_digit(input: &str) -> u32 {
    match input.parse::<u32>() {
        Ok(d) => d,
        Err(_) => TABLE.iter().position(|&s| s == input).unwrap() as u32 + 1,
    }
}

pub fn solve(input: &str) -> u32 {
    let mut sum: u32 = 0;

    let re =
        Regex::new("(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)|[1-9]")
            .unwrap();

    for line in input.lines() {
        let mi = re.find(line).unwrap().as_str();
        let mj = re.find_iter(line).last().unwrap().as_str();

        sum += to_digit(mi) * 10 + to_digit(mj);
    }

    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test2.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 281);
    }
}
