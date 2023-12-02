use day_02::part1::solve;

fn main() {
    let input = std::fs::read_to_string("day-02/inputs/input.txt")
        .expect("ERROR: day-2/inputs/input.txt file not found");

    println!("Result: {}", solve(&input))
}
