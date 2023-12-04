use {{crate_name}}::bench;
use {{crate_name}}::part1::solve;

fn main() {
    let input = std::fs::read_to_string("{{project-name}}/inputs/input.txt")
        .expect("ERROR: {{project-name}}/inputs/input.txt file not found");

    bench(|| println!("Result: {}", solve(&input)));
}
