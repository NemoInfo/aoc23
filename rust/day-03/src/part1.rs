use std::collections::HashSet;

fn checked_add_signed_bounded(a: usize, b: isize, bound: usize) -> Option<usize> {
    match a.checked_add_signed(b) {
        Some(s) if s < bound => Some(s),
        _ => None,
    }
}

pub fn solve(input: &str) -> u32 {
    let grid = input
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut parts: HashSet<[usize; 2]> = HashSet::new();

    for (r, row) in grid.iter().enumerate() {
        for (c, &ch) in row.iter().enumerate() {
            if ch == '.' || ch.is_digit(10) {
                continue;
            }

            #[rustfmt::skip]
            (-1..=1).flat_map(|dr| (-1..=1).map(move |dc| [dr, dc]))
                .filter_map(|[dr, dc]| {
                    checked_add_signed_bounded(r, dr, grid.len())
                        .zip(
                    checked_add_signed_bounded(c, dc,  row.len()))})
                .for_each(|(cr, mut cc)| {
                    if !grid[cr][cc].is_digit(10) {
                        return;
                    }

                    while cc > 0 && grid[cr][cc - 1].is_digit(10) {
                        cc -= 1;
                    }

                    parts.insert([cr, cc]);
                });
        }
    }

    parts
        .iter()
        .map(|&[r, cs]| {
            let mut ce = cs + 1;

            while ce < grid[0].len() && grid[r][ce].is_digit(10) {
                ce += 1;
            }

            grid[r][cs..ce]
                .iter()
                .collect::<String>()
                .parse::<u32>()
                .unwrap()
        })
        .sum()
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
