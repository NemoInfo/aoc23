use day_25::bench;
use day_25::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day-25/inputs/input.txt")
        .expect("ERROR: day-25/inputs/input.txt file not found");

    bench(|| println!("Result: {}", solve(&input)));
}
