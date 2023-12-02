run day part:
	cargo run -p {{day}} --bin {{part}}
test day part="":
	cargo test -p {{day}} {{part}}
create name:
	cargo generate --path ./template --name {{name}}
