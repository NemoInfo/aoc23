run day part:
	cargo run -p {{day}} --bin {{part}}
test day part="":
	cargo test -p {{day}} {{part}}
