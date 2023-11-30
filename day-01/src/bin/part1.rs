use day_01::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day-01/inputs/input.txt")
        .expect("ERROR: day-1/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
