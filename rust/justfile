default:
  just --list
run part day=`date +day-%d` release="":
	cargo run -p {{day}} --bin part{{part}} {{release}}
test part="" day=`date +day-%d`:
	cargo test -p {{day}} {{part}}
create name=`date +day-%d`:
	cargo generate --path ./template --name {{name}}
