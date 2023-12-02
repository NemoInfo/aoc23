use {{crate_name}}::part1::solve;

fn main() {
    let input = std::fs::read_to_string("{{crate_name}}/inputs/input.txt")
        .expect("ERROR: {{crate_name}}/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
