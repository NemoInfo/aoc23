use day_23::bench;
use day_23::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day-23/inputs/input.txt")
        .expect("ERROR: day-23/inputs/input.txt file not found");

    bench(|| println!("Result: {}", solve(&input)));
}
