run:
	python3 cli/main.py --run

build-rust:
	cd core_rust && maturin develop

benchmark:
	python3 scripts/benchmark_runner.py
