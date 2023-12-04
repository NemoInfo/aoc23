use day_04::bench;
use day_04::part2::solve;

fn main() {
    let input = std::fs::read_to_string("day-04/inputs/input.txt")
        .expect("ERROR: day-04/inputs/input.txt file not found");

    bench(|| println!("Result: {}", solve(&input)));
}
