use std::collections::{HashMap, HashSet, VecDeque};

fn parse_graph(input: &str) -> HashMap<String, Vec<String>> {
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();

    for row in input.lines() {
        let row = row.replace(":", "");
        let mut iter = row.split(" ").map(|s| s.to_string());
        let node = iter.next().unwrap();

        for next in iter {
            graph.entry(next.clone()).or_default().push(node.clone());
            graph.entry(node.clone()).or_default().push(next);
        }
    }

    graph
}

fn count_edges(graph: &HashMap<String, Vec<String>>) -> HashMap<[String; 2], u32> {
    let mut edges: HashMap<[String; 2], u32> = HashMap::new();

    for start in graph.keys() {
        let mut queue = VecDeque::from_iter([start]);
        let mut seen: HashSet<&String> = HashSet::from_iter([start]);
        let mut prev: HashMap<&String, &String> = HashMap::new();

        while let Some(node) = queue.pop_front() {
            for next in graph.get(node).unwrap() {
                if seen.contains(next) {
                    continue;
                }

                seen.insert(next);
                queue.push_back(next);
                prev.insert(next, node);
            }
        }

        for mut node in graph.keys() {
            while node != start {
                let next = prev.get(node).unwrap();
                *edges
                    .entry([
                        node.to_string().min(next.to_string()),
                        node.to_string().max(next.to_string()),
                    ])
                    .or_default() += 1;
                node = next;
            }
        }
    }

    edges
}

pub fn count_connected(graph: &HashMap<String, Vec<String>>) -> u32 {
    let start = graph.keys().collect::<Vec<_>>()[0];
    let mut queue = VecDeque::from_iter([start]);
    let mut seen: HashSet<&String> = HashSet::from_iter([start]);

    while let Some(node) = queue.pop_front() {
        for next in graph.get(node).unwrap() {
            if seen.contains(next) {
                continue;
            }

            seen.insert(next);
            queue.push_back(next);
        }
    }

    seen.len() as u32
}

pub fn solve(input: &str) -> u32 {
    let mut graph = parse_graph(input);
    let edges = count_edges(&graph);
    let mut edges_vec = edges.iter().collect::<Vec<_>>();
    edges_vec.sort_by_key(|(_, &count)| -(count as i64));

    for ([a, b], _) in edges_vec.iter().take(3) {
        graph.get_mut(a).unwrap().retain(|x| x != b);
        graph.get_mut(b).unwrap().retain(|x| x != a);
    }

    let con1 = count_connected(&graph);

    (graph.len() as u32 - con1) * con1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 54);
    }
}
