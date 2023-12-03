use {{crate_name}}::part2::solve;

fn main() {
    let input = std::fs::read_to_string("{{project-name}}/inputs/input.txt")
        .expect("ERROR: {{project-name}}/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
