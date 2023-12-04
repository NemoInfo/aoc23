use day_04::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day-04/inputs/input.txt")
        .expect("ERROR: day-04/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
