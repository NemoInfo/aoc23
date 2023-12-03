fn is_symbol(c: char) -> bool {
    c.is_ascii_punctuation() && c != '.'
}

pub fn solve(input: &str) -> u32 {
    let m = input
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut sum = 0;

    for i in 0..m.len() {
        let mut j = 0;
        while j < m[0].len() {
            if m[i][j].is_digit(10) {
                let mut is_part = j >= 1
                    && (is_symbol(m[i][j - 1])
                        || (i >= 1 && is_symbol(m[i - 1][j - 1]))
                        || (i + 1 < m.len() && is_symbol(m[i + 1][j - 1])));
                let mut num = 0;
                while j < m[0].len() && m[i][j].is_digit(10) {
                    is_part = is_part
                        || (i >= 1 && is_symbol(m[i - 1][j]))
                        || (i + 1 < m.len() && is_symbol(m[i + 1][j]));
                    num = num * 10 + m[i][j].to_digit(10).unwrap();
                    j += 1;
                }
                is_part = is_part
                    || j < m[0].len()
                        && (is_symbol(m[i][j])
                            || (i >= 1 && is_symbol(m[i - 1][j]))
                            || (i + 1 < m.len() && is_symbol(m[i + 1][j])));

                if is_part {
                    sum += num;
                }
            } else {
                j += 1;
            }
        }
    }

    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 4361);
    }
}
