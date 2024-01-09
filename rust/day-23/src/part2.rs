use std::collections::{HashMap, HashSet, VecDeque};

/// Compute the cost of the maximum cost path from the `start` node to the `end` node
///
/// > **panics** if there is no path from `start` to `end`
fn _find_max_cost(
    graph: &HashMap<[usize; 2], HashMap<[usize; 2], u32>>,
    start: [usize; 2],
    end: [usize; 2],
    mut visited: HashSet<[usize; 2]>,
    path_cost: u32,
    mut max_cost: u32,
) -> u32 {
    visited.insert(start);

    if start == end {
        return max_cost.max(path_cost);
    }

    for (&neighbour, &cost) in graph.get(&start).unwrap() {
        if visited.contains(&neighbour) {
            continue;
        }

        let new_path_cost = path_cost + cost;
        let new_max_cost = _find_max_cost(
            graph,
            neighbour,
            end,
            visited.clone(),
            new_path_cost,
            max_cost,
        );

        max_cost = max_cost.max(new_max_cost);
    }

    return max_cost;
}

fn find_max_cost(
    graph: &HashMap<[usize; 2], HashMap<[usize; 2], u32>>,
    start: [usize; 2],
    end: [usize; 2],
) -> u32 {
    _find_max_cost(graph, start, end, HashSet::new(), 0, 0)
}

/// Compute maze intersection graph from maze grid from `start` to `end`
fn compute_graph(
    grid: &Vec<Vec<char>>,
    start: [usize; 2],
    end: [usize; 2],
) -> HashMap<[usize; 2], HashMap<[usize; 2], u32>> {
    let mut queue: VecDeque<([usize; 2], [isize; 2])> = VecDeque::from_iter([(start, [1, 0])]);
    let mut visited: HashSet<([usize; 2], [isize; 2])> = HashSet::new();
    let mut graph: HashMap<[usize; 2], HashMap<[usize; 2], u32>> = HashMap::new();

    while let Some(([nr, nc], [mut dr, mut dc])) = queue.pop_front() {
        visited.insert(([nr, nc], [dr, dc]));

        let (mut pr, mut pc) = (nr, nc);
        let (Some(mut cr), Some(mut cc)) = (nr.checked_add_signed(dr), nc.checked_add_signed(dc))
        else {
            continue;
        };

        let mut length = 1;

        let mut dirs: Vec<[isize; 2]> = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            .iter()
            .filter(
                |[dr, dc]| match (cr.checked_add_signed(*dr), cc.checked_add_signed(*dc)) {
                    (Some(nr), Some(nc))
                        if nr < grid.len()
                            && nc < grid[0].len()
                            && grid[nr][nc] != '#'
                            && [nr, nc] != [pr, pc] =>
                    {
                        true
                    }
                    _ => false,
                },
            )
            .cloned()
            .collect::<Vec<_>>();

        while dirs.len() == 1 {
            length += 1;
            [dr, dc] = dirs[0];
            [pr, pc] = [cr, cc];
            [cr, cc] = [(cr as isize + dr) as usize, (cc as isize + dc) as usize];

            dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                .iter()
                .filter(
                    |[dr, dc]| match (cr.checked_add_signed(*dr), cc.checked_add_signed(*dc)) {
                        (Some(nr), Some(nc))
                            if nr < grid.len()
                                && nc < grid[0].len()
                                && grid[nr][nc] != '#'
                                && [nr, nc] != [pr, pc] =>
                        {
                            true
                        }
                        _ => false,
                    },
                )
                .cloned()
                .collect::<Vec<_>>();
        }

        if dirs.len() == 0 {
            if [cr, cc] == end {
                graph.entry([nr, nc]).or_default().insert([cr, cc], length);
                graph.entry([cr, cc]).or_default().insert([nr, nc], length);
            }
            continue;
        }

        graph.entry([nr, nc]).or_default().insert([cr, cc], length);
        graph.entry([cr, cc]).or_default().insert([nr, nc], length);

        for [dr, dc] in dirs {
            if !visited.contains(&([cr, cc], [dr, dc])) {
                queue.push_back(([cr, cc], [dr, dc]));
            }
        }
    }

    graph
}

pub fn solve(input: &str) -> u32 {
    let grid: Vec<Vec<char>> = input.lines().map(|row| row.chars().collect()).collect();

    let start: [usize; 2] = [0, 1];
    let end: [usize; 2] = [grid.len() - 1, grid.len() - 2];

    let graph = compute_graph(&grid, start, end);

    find_max_cost(&graph, start, end)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 154);
    }
}
