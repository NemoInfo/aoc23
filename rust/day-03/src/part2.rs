fn checked_bounded_add_signed(a: usize, b: isize, bound: usize) -> Option<usize> {
    match a.checked_add_signed(b) {
        Some(s) if s < bound => Some(s),
        _ => None,
    }
}

fn get_parts(m: &Vec<Vec<char>>, [x, y]: [usize; 2]) -> Option<[u32; 2]> {
    let mut res: Vec<u32> = vec![];
    let mut visited: Vec<[usize; 2]> = vec![];

    let dx = [-1, 0, 1, 1, 1, 0, -1, -1];
    let dy = [-1, -1, -1, 0, 1, 1, 1, 0];

    let mut i = 0;
    while i < dx.len() {
        let Some(x) = checked_bounded_add_signed(x, dx[i], m.len()) else {
            i += 1;
            continue;
        };
        let Some(y) = checked_bounded_add_signed(y, dy[i], m[0].len()) else {
            i += 1;
            continue;
        };
        i += 1;
        if !m[x][y].is_digit(10) {
            continue;
        }
        if visited.iter().find(|&a| a == &[x, y]).is_some() {
            continue;
        }

        visited.push([x, y]);
        let mut num = m[x][y].to_digit(10).unwrap();
        let mut d = 1;
        // Add left
        let mut yy = y as isize - 1;
        while yy >= 0 && m[x][yy as usize].is_digit(10) {
            d *= 10;
            num += d * m[x][yy as usize].to_digit(10).unwrap();
            visited.push([x, yy as usize]);
            yy -= 1;
        }
        // Add right
        let mut yy = y + 1;
        while yy < m[0].len() && m[x][yy].is_digit(10) {
            num = num * 10 + m[x][yy].to_digit(10).unwrap();
            visited.push([x, yy]);
            yy += 1;
        }

        res.push(num);
    }

    match res.len() {
        2 => Some([res[0], res[1]]),
        1 | 0 => None,
        _ => unreachable!("{res:?} {visited:?}"),
    }
}

pub fn solve(input: &str) -> u32 {
    let m = input
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut sum = 0;

    for i in 0..m.len() {
        for j in 0..m[0].len() {
            if m[i][j] != '*' {
                continue;
            }

            if let Some([a, b]) = get_parts(&m, [i, j]) {
                sum += a * b;
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

        assert_eq!(solve(&input), 467835);
    }

    #[test]
    fn test_custom_solve() {
        let input = std::fs::read_to_string("inputs/custom.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 210);
    }
}
