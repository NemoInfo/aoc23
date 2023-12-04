pub mod part1;
pub mod part2;

pub fn bench<F: FnOnce()>(f: F) {
    let start_time = std::time::Instant::now();
    f();
    let elapsed = start_time.elapsed();
    println!("Δt: {:.2?}", elapsed);
}
