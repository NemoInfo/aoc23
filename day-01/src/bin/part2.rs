use day_01::part2::solve;

fn main() {
    let input = std::fs::read_to_string("day-01/inputs/input.txt")
        .expect("ERROR: inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
