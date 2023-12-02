use day_03::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day_03/inputs/input.txt")
        .expect("ERROR: day_03/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
